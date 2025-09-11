MOD_INFO = {
    "id": "dcmod",
    "name": "Dead Cells core for hlmod",
    "description": "Core utilities for modding Dead Cells.",
    "version": "0.0.1",
    "dependencies": ["modcore"],
    "enabled": True
}

from typing import Optional
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

def log(*args, **kwargs) -> None:
    print("[dcmod] ", end="")
    print(*args, **kwargs)
    
# globals and whatnot
CONSOLE: Optional[Console] = None

# config for default tweaks. changeme!
PREDICTABLE_STAMP: bool = False # return a predictable stamp value from $PakUtils.getPakStampHash so changes to version info in the game don't invalidate your paks
IGNORE_STAMP: bool = True # ignore stamp checking altogether during pak load
# TODO: config system

@hook(5937)
def hook_console_ctor(self: Hook, this: Console):
    global CONSOLE
    log("Grabbed console!")
    CONSOLE = this
    self.call_original(this)
    this.activateDebug()
    
@hook(5904)
def hook_console_log(self: Hook, this: Console, logText: str, color: Optional[int]):
    log(f"[Console] {logText}")
    #self.call_original(this, logText, color)
    #dump_stack()
    h2dConsole.log(this, logText, color) # type: ignore
    
@hook(6469)
def hook_titlescreen_setMiscTexts(self: Hook, this: TitleScreen):
    self.call_original(this)
    this.build.set_text(f"dcmod {MOD_INFO["version"]}, powered by hlmod {hlmod.version}") # type: ignore
    #CONSOLE.log(f"dcmod {MOD_INFO["version"]}, powered by hlmod", None)

@hook(6418)
def hook_pakutils_getPakStampHash(self: Hook) -> str:
    if not PREDICTABLE_STAMP:
        return self.call_original()
    return "0022228129b0973a12d14548434b3741debcd3a38734f1e0dd1f3b3f7acdd91c" # for commit 50ed44f, latest v35. in case you fuck something up version-wise ;)
