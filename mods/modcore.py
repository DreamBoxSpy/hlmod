"""
Common modding routines for Hashlink games.
"""

import inspect
import hlmod
from typing import List

MOD_INFO = {
    "id": "modcore",
    "name": "hlmod Modding Core",
    "description": "Core utilities, tools, and functions for instrumenting Hashlink.",
    "version": "0.0.1",
    "dependencies": []
}

def hook(findex: int|List[int]):
    """
    A decorator that registers the decorated function as a hook for a given
    Hashlink function index (findex).

    Usage:
    ```
    @hook(296)
    def my_hook(hook, *args):
        # ... your hook logic ...
        hook.call_original(*args)
    ```
    """
    if not isinstance(findex, (int, list)):
        raise TypeError("The @hook decorator requires an integer findex or a list of integer findexes.")

    def decorator(func):
        if isinstance(findex, int):
            hlmod.register_hook(findex, func) # pyright: ignore[reportAttributeAccessIssue]
        else:
            for fidx in findex:
                hlmod.register_hook(fidx, func) # pyright: ignore[reportAttributeAccessIssue]
        return func
    
    return decorator

