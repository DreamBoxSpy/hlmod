MOD_INFO = {
    "id": "testpatch",
    "name": "Test PatchMe",
    "description": "",
    "version": "0.0.1",
    "dependencies": ["modcore"]
}

from modcore import hook
from hlmod import get_obj_field, Hook

@hook(30)
def thing(self: Hook, *args):
    args = list(args)
    args[1] = None
    self.call_original(*args)