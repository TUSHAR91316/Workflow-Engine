from typing import Callable, Dict, Any, Optional
import asyncio
class Node:
    def __init__(self, name: str, func: Callable):
        self.name = name
        self.func = func
class Workflow:
    def __init__(self, nodes: Dict[str, Node], edges: Dict[str, Optional[str]], start_node: str):
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
        iteration = 0
        max_iterations = 1000
        while current:
            if iteration >= max_iterations:
                log.append("Max iterations reached, aborting")
                break
            iteration += 1
            node = self.nodes.get(current)
            if node is None:
                log.append(f"Node not found: {current}")
                break
            log.append(f"Running node: {current}")
            try:
                output = await self.run_node(node, state)
            except Exception as e:
                log.append(f"Exception in node {current}: {e}")
                break
            if output:
                if not isinstance(output, dict):
                    log.append(f"Warning: node {current} returned non-dict output; ignoring")
                else:
                    state.update(output)
            if "next" in state:
                next_node = state.pop("next")
                log.append(f"Branching to: {next_node}")
                current = next_node
                continue
            if state.get("loop") is True:
                log.append(f"Looping on node: {current}")
                state.pop("loop")
                continue
            current = self.edges.get(current)
        return state, log