import inspect

MOD_INFO = {
    "id": "modcore",
    "name": "hlmod Modding Core",
    "description": "Core utilities, tools, and functions for instrumenting Hashlink.",
    "version": "0.0.1",
    "dependencies": []
}

def log(mod_id: str, *args):
    print(f"[{mod_id}] ", end="")
    print(*args)

def initialize():
    """Called by hlmod when this mod is loaded."""
    log("modcore", "Hello from modcore!")