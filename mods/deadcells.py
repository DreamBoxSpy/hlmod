MOD_INFO = {
    "id": "deadcells",
    "name": "Dead Cells hlmod Core",
    "description": "Core utilities for modding Dead Cells.",
    "version": "0.0.1",
    "dependencies": ["modcore"],
    "enabled": False
}

from hlmod import assert_code_sha, Hook
from modcore import hook
from stubs.en import Hero
from stubs.libs import S_GitVersion

def initialize() -> None:
    assert_code_sha("376564ab2173ddcbadf53d73baf2fc335793e4d14a637fc1829569c314f39667")
    
@hook(6248)
def hook_boot_main(self: Hook) -> None:
    print("[hlmod] Hooked Boot.main!")
    print(S_GitVersion.SHORT_HASH)
    return self.call_original()

