MOD_INFO = {
    "id": "dcmod",
    "name": "Dead Cells core for hlmod",
    "description": "Core utilities for modding Dead Cells.",
    "version": "0.0.1",
    "dependencies": ["modcore"],
    "enabled": True
}

from typing import Any, Optional
from hlmod import assert_code_sha, Hook
import hlmod
from modcore import hook
from stubs.en import Hero
from stubs.libs import S_GitVersion
from stubs.ui import Console
from stubs.h2d import Console as h2dConsole
from stubs.pr import TitleScreen

def initialize() -> None:
    assert_code_sha("376564ab2173ddcbadf53d73baf2fc335793e4d14a637fc1829569c314f39667") # TODO: support matching a list of hashes
    
# globals and whatnot
CONSOLE: Optional[Console] = None

# config for default tweaks. changeme!
PREDICTABLE_STAMP: bool = True # return a predictable stamp value from $PakUtils.getPakStampHash so changes to version info in the game don't invalidate your paks
IGNORE_STAMP: bool = True # ignore stamp checking altogether during pak load
INGAME_LOGS: bool = True
LOG_COLOR: int = 0xffffff
CUSTOM_BUILD_TEXT: bool = True
# TODO: config system

BUILD_TEXT = f"dcmod {MOD_INFO["version"]}, powered by hlmod {hlmod.version}"

def log(*args, **kwargs) -> None:
    global CONSOLE
    print("[dcmod] ", end="")
    print(*args, **kwargs)
    if CONSOLE is not None and INGAME_LOGS:
        CONSOLE.log(f"[dcmod] {' '.join(args)}", LOG_COLOR)

def set_build_text(text: str) -> None:
    global BUILD_TEXT
    BUILD_TEXT = text

@hook(5937)
def hook_console_ctor(self: Hook, this: Console):
    global CONSOLE
    CONSOLE = this
    self.call_original(this)
    this.activateDebug()
    log("Console initialized!")
    
@hook(5904)
def hook_console_log(self: Hook, this: Console, logText: str, color: Optional[int]):
    print(f"[dcmod] [Console] {logText}")
    h2dConsole.log(this, logText, color)

@hook(6469)
def hook_titlescreen_setMiscTexts(self: Hook, this: TitleScreen):
    self.call_original(this)
    if CUSTOM_BUILD_TEXT:
        this.build.set_text(BUILD_TEXT)

@hook("tools.pak.$PakUtils.getPakStampHash")
def hook_pakutils_getPakStampHash(self: Hook) -> str:
    if not PREDICTABLE_STAMP:
        return self.call_original()
    return "0022228129b0973a12d14548434b3741debcd3a38734f1e0dd1f3b3f7acdd91c" # for commit 50ed44f, latest v35. in case you fuck something up version-wise ;)

@hook(35983)
def hook_logutils_log(self: Hook, text: str, severity: Any, pos: Any):
    if CONSOLE:
        CONSOLE.log(text, 0xb8fcf7)
    self.call_original(text, severity, pos)