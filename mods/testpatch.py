MOD_INFO = {
    "id": "testpatch",
    "name": "Test PatchMe",
    "description": "",
    "version": "0.0.1",
    "dependencies": ["modcore"]
}

from modcore import hook
from hlmod import get_obj_field, Hook, assert_code_sha
from stubs import TestClass
from typing import Optional

def initialize():
    assert_code_sha("c5b81c94db4a9de0e78e8779adabddf6b4246fd1fc938307306c27271e2df826")

@hook(30)
def thing(self: Hook, *args):
    print("Hook!")
    self.call_original(*args)

