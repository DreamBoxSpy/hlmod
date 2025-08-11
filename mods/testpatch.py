MOD_INFO = {
    "id": "testpatch",
    "name": "Test PatchMe",
    "description": "",
    "version": "0.0.1",
    "dependencies": ["modcore"]
}

from modcore import hook

@hook(29)
def hook_getval(hook, *args):
    return hook.call_original(*args) * 2

@hook(30)
def hook_print(hook, *args):
    print(args)
    return hook.call_original(*args)