MOD_INFO = {
    "id": "testpatch",
    "name": "Test PatchMe",
    "description": "",
    "version": "0.0.1",
    "dependencies": ["modcore"]
}

from modcore import hook

@hook(29)
def hook_thing(*args, **kwargs):
    print(args, kwargs)
    print("Made it!")