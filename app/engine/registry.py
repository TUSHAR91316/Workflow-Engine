from typing import Callable, Dict

class ToolRegistry:
    def __init__(self):
        self.tools: Dict[str, Callable] = {}

    def register(self, name: str, func: Callable):
        self.tools[name] = func

    def get(self, name: str):
        return self.tools.get(name)

    def call(self, name: str, *args, **kwargs):
        fn = self.get(name)
        if fn is None:
            raise KeyError(f"Tool not found: {name}")
        return fn(*args, **kwargs)

# Singleton instance for simplicity
registry = ToolRegistry()