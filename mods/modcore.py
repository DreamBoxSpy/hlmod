"""
Common modding routines for Hashlink games.
"""

import inspect
import hlmod
from typing import List
import stubs

MOD_INFO = {
    "id": "modcore",
    "name": "hlmod Modding Core",
    "description": "Core utilities, tools, and functions for instrumenting Hashlink.",
    "version": "0.0.1",
    "dependencies": []
}

def hook(fidx_or_name: str|int|List[int]):
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
    if not isinstance(fidx_or_name, (int, list, str)):
        raise TypeError("The @hook decorator requires an integer findex or a list of integer findexes.")

    def decorator(func):
        if isinstance(fidx_or_name, int):
            hlmod.register_hook(fidx_or_name, func) # pyright: ignore[reportAttributeAccessIssue]
        elif isinstance(fidx_or_name, str):
            fidx = hlmod.findex_for_name(fidx_or_name)
            # print(f"[hlmod] [DEBUG] Hooking {fidx_or_name} to {fidx} with {func.__name__}")
            hlmod.register_hook(fidx, func)
        else:
            for fidx in fidx_or_name:
                hlmod.register_hook(fidx, func) # pyright: ignore[reportAttributeAccessIssue]
        return func
    
    return decorator

