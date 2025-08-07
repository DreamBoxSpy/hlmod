MOD_INFO = {
    "id": "testpatch",
    "name": "Test PatchMe",
    "description": "",
    "version": "0.0.1",
    "dependencies": ["modcore"]
}

from modcore import log, hook

def initialize():
    """Called by hlmod when this mod is loaded."""
    log("testpatch", "Hello from modcore!")

@hook(29)
def hook_thing():
    print("Made it!")