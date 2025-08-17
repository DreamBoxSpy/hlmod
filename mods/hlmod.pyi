"""
Internal, low-level module to interface more directly with hlmod. You should use `modcore` for 99% of cases, which provides much higher-level abstractions over this module!
"""

from typing import Any, Protocol

class HlPtr:
    """
    Light wrapper on a raw void* to an HL object.
    """
    
    @property
    def ptr(self) -> int:
        """
        The raw value of the pointer, as an int.
        """
        ...
        
    @property
    def kind(self) -> int:
        """
        The HL type kind of this pointer.
        """
        ...
    

class Hook:
    """
    Hook context object
    """
    
    findex: int
    """
    The function index this hook was invoked for.
    """
    
    def call_original(*args: Any) -> Any:
        """
        Calls the original function that was hooked.
        """
        ...

        
class HookCallback(Protocol):
    """
    Callback signature: (hook: hlmod.Hook, *args: Any)
    """
    def __call__(self, hook: Hook, *args: Any) -> Any:
        ...


def register_hook(
    findex: int, 
    callback: HookCallback
) -> None:
    """
    Hooks a JIT-compiled Hashlink function, redirecting its call to a Python
    callback.

    Args:
        findex: The unique integer index of the Hashlink function to hook.
        callback: A Python function that will be executed when the hook is
                  triggered. Will be passed an hlmod.Hook object and the original args from the function call.
    """
    ...

def get_obj_field(obj: HlPtr, field: int) -> Any:
    """
    Gets a field from a Obj* by index.
    """
    ...
    
def set_obj_field(obj: HlPtr, field: int, value: Any) -> None:
    """
    Sets a field in an Obj* by index.
    """
    ...
    
def get_fixed_prng() -> bool:
    """
    Gets if the HL PRNG is currently set to be fixed or not.
    """
    ...
    
def set_fixed_prng(value: bool) -> None:
    """
    Sets if the HL PRNG should be fixed or not.
    When fixed, the seed is set to 4644546 and the PID is spoofed to 0.
    """
    ...