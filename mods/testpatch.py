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
def thing(self: Hook, val: float, val2: Optional[float], msg: str, val3: Optional[TestClass]):
    print("Hook!")
    val = 2.0
    val2 = 1.0
    msg = "Hello, hlmod world!"
    assert val3 is not None
    print(val3.test)
    self.call_original(val, val2, msg, val3)

