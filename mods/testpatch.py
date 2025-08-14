MOD_INFO = {
    "id": "testpatch",
    "name": "Test PatchMe",
    "description": "",
    "version": "0.0.1",
    "dependencies": ["modcore"]
}

from modcore import hook
from hlmod import get_obj_field

@hook(29)
def hook_getval(hook, *args):
    return hook.call_original(*args) * 2

@hook(30)
def hook_print(hook, *args):
    print(args[2])
    print(get_obj_field(args[2]._hlmod_ptr, "bytes"))
    return hook.call_original(*args)