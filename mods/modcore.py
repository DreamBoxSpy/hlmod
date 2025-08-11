import inspect
import hlmod

MOD_INFO = {
    "id": "modcore",
    "name": "hlmod Modding Core",
    "description": "Core utilities, tools, and functions for instrumenting Hashlink.",
    "version": "0.0.1",
    "dependencies": []
}

def log(mod_id: str, *args):
    print(f"[{mod_id}] ", end="")
    print(*args)

def hook(findex: int):
    """
    A decorator that registers the decorated function as a hook for a given
    Hashlink function index (findex).

    Usage:
        @on_hook(296)
        def my_hook_callback(hook, *args):
            # ... your hook logic ...
            hook.call_original(*args)
    """
    if not isinstance(findex, int):
        raise TypeError("The @on_hook decorator requires an integer findex.")

    def decorator(func):
        hlmod.register_hook(findex, func)
        return func
    
    return decorator

def initialize():
    """Called by hlmod when this mod is loaded."""
    log("modcore", "hlmod modcore 0.0.1 initialized!")
    
    