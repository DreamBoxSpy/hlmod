"""
Abstract base classes for accessing HL types in Python.
"""

from hlmod import HlPtr, register_hlobj, get_obj_field, set_obj_field # pyright: ignore[reportAttributeAccessIssue]
from typing import Any, Callable, Type, TypeVar

T = TypeVar("T", bound=object)

def hltype(idx: int) -> Callable[[Type[T]], Type[T]]:
    """
    A class decorator that registers a class in a global registry with a given index.
    """

    def decorator(cls: Type[T]) -> Type[T]:
        """The actual decorator that registers the class."""
        register_hlobj(idx, cls)
        return cls
        
    return decorator

class HlObject:
    __slots__ = ("_hlmod_ptr")
    _hlmod_ptr: HlPtr
    
    def __init__(self, ptr: HlPtr) -> None:
        # TODO: python-side instancing
        self._hlmod_ptr = ptr
    
    def _hlmod_get_field(self, name: str) -> Any:
        return get_obj_field(self._hlmod_ptr, name)

    def _hlmod_set_field(self, name: str, value: Any) -> None:
        set_obj_field(self._hlmod_ptr, name, value)

    def _hlmod_call_proto(self, name: str, *args: Any) -> Any:
        return NotImplemented
    
    def _hlmod_call_field(self, name: str, *args: Any) -> Any:
        return NotImplemented