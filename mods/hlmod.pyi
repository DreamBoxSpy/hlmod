from typing import Any, Callable

def register_hook(
    findex: int, 
    callback: Callable[[Any], Any]
) -> None:
    """
    Hooks a JIT-compiled Hashlink function, redirecting its call to a Python
    callback.

    Args:
        findex: The unique integer index of the Hashlink function to hook.
        callback: A Python function that will be executed when the hook is
                  triggered.
    """
    ...