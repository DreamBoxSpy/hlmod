#!/usr/bin/env python3
import os
import re
import json
import argparse
from pathlib import Path
from typing import Dict, Any, Optional

# Captures: 1=doc comment, 2=type name
P_TYPE = re.compile(
    r"/\*\*(.*?)\*/\s*"
    r"(?:#if[^\n]+\n\s*)?"
    r"(?:extern\s+|private\s+)?(?:class|enum|abstract|interface)\s+([A-Za-z0-9_]+)",
    re.DOTALL
)

# Captures: 1=doc comment, 2=function name
P_FUNC = re.compile(
    r"/\*\*(.*?)\*/\s*"
    r"((?:@:[^\n]+\n\s*)|(?:#if[^\n]+\n\s*))*"  # Metas and conditionals
    r"(?:(?:public|private|static|inline|override)\s+)*" # Keywords
    r"function\s+([A-Za-z0-9_]+)",
    re.DOTALL
)

# Captures: 1=doc comment, 2=variable name
P_FIELD = re.compile(
    r"/\*\*(.*?)\*/\s*"
    r"(?:#if[^\n]+\n\s*)?"
    r"(?:(?:public|private|static|inline|final)\s+)*" # Keywords
    r"var\s+([A-Za-z0-9_]+)",
    re.DOTALL
)

def clean_doc_comment(raw_doc: str) -> str:
    """Cleans a raw doc comment string by removing comment markers."""
    lines = raw_doc.strip().split('\n')
    cleaned_lines = []
    for line in lines:
        # Remove leading whitespace and potential '*'
        clean_line = line.strip()
        if clean_line.startswith('*'):
            clean_line = clean_line[1:].strip()
        cleaned_lines.append(clean_line)
    return "\n".join(cleaned_lines)

def parse_haxe_file(file_path: Path) -> Optional[Dict[str, Any]]:
    """
    Parses a single Haxe file.
    """
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

    package_match = re.search(r"^\s*package\s+([\w.]+);", content, re.MULTILINE)
    package = package_match.group(1) if package_match else ""

    types = []
    for match in P_TYPE.finditer(content):
        doc, name = match.groups()
        q_name = f"{package}.{name}" if package else name
        types.append({
            'q_name': q_name,
            'doc': clean_doc_comment(doc),
            'start': match.start()
        })

    if not types:
        return None

    types.sort(key=lambda t: t['start'])
    types.append({'q_name': 'EOF', 'start': len(content)})

    functions = [
        {'name': m.groups()[-1], 'doc': clean_doc_comment(m.group(1)), 'start': m.start()}
        for m in P_FUNC.finditer(content)
    ]
    fields = [
        {'name': m.groups()[-1], 'doc': clean_doc_comment(m.group(1)), 'start': m.start()}
        for m in P_FIELD.finditer(content)
    ]

    result = {}
    for i in range(len(types) - 1):
        current_type = types[i]
        type_start_pos = current_type['start']
        type_end_pos = types[i+1]['start']
        
        q_name = current_type['q_name']
        result[q_name] = {
            "doc": current_type['doc'],
            "path": str(file_path),
            "functions": {},
            "fields": {}
        }

        for func in functions:
            if type_start_pos < func['start'] < type_end_pos:
                result[q_name]['functions'][func['name']] = func['doc']

        for field in fields:
            if type_start_pos < field['start'] < type_end_pos:
                result[q_name]['fields'][field['name']] = field['doc']

    return result

def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description="Parse Haxe std lib doc comments and generate a JSON file.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "-o", "--output",
        default="haxe_docs.json",
        help="Path to the output JSON file (default: haxe_docs.json)"
    )
    args = parser.parse_args()
        
    std_path = Path("haxe/std/")
    if not std_path.is_dir():
        print(f"Error: Path '{std_path}' is not a valid directory.")
        exit(1)

    print(f"Scanning Haxe standard library at: {std_path}")
    
    all_docs = {}
    file_count = 0
    
    for root, dirs, files in os.walk(std_path):
        if 'macros' in dirs:
            dirs.remove('macros')

        for filename in files:
            if filename.endswith(".hx"):
                file_path = Path(root) / filename
                print(f"  -> Parsing {file_path.relative_to(std_path)}...")
                file_docs = parse_haxe_file(file_path)
                if file_docs:
                    all_docs.update(file_docs)
                file_count += 1
    
    try:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(all_docs, f, indent=2, ensure_ascii=False)
        print(f"\nSuccessfully parsed {file_count} files.")
        print(f"Documentation saved to '{args.output}'")
    except Exception as e:
        print(f"\nError writing to output file: {e}")

if __name__ == "__main__":
    main()