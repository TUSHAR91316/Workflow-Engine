from typing import Callable, Dict, Any
import asyncio

class Node:
    def __init__(self, name: str, func: Callable):
        self.name = name
        self.func = func

class Workflow:
    def __init__(self, nodes: Dict[str, Node], edges: Dict[str, str], start_node: str):
        self.nodes = nodes
        self.edges = edges
        self.start_node = start_node

    async def run_node(self, node: Node, state: Dict[str, Any]):
        result = node.func(state)
        if asyncio.iscoroutine(result):
            result = await result
        return result

    async def run(self, state: Dict[str, Any], log: list):
        current = self.start_node
        while current:
            log.append(f"Running node: {current}")

            node = self.nodes[current]
            output = await self.run_node(node, state)

            if output:
                state.update(output)

            if "next" in state:
                current = state.pop("next")
                continue

            if state.get("loop") is True:
                state.pop("loop")
                continue

            current = self.edges.get(current)
        return state, log
