MOD_INFO = {
    "id": "testpatch",
    "name": "Test PatchMe",
    "description": "",
    "version": "0.0.1",
    "dependencies": ["modcore"]
}

from modcore import hook
from hlmod import get_obj_field


@hook(30)
def hook_print(hook, *args):
    print(args)
    return hook.call_original(2.0, 1.0, "Hello, world!", args[3])