import asyncio
from typing import Dict, Any
def extract_functions(state: Dict[str, Any]):
    code = state.get("code", "")
    functions = code.count("def ")
    return {"functions": functions}
def check_complexity(state: Dict[str, Any]):
    code = state.get("code", "")
    lines = len(code.splitlines())
    functions = state.get("functions", 0)
    complexity = functions * 10 + max(0, lines - 50) // 10
    return {"complexity": complexity}
def detect_issues(state: Dict[str, Any]):
    code = state.get("code", "")
    todos = code.count("TODO")
    prints = code.count("print(")
    issues = todos + prints
    return {"issues": issues}
def suggest_improvements(state: Dict[str, Any]):
    complexity = state.get("complexity", 0)
    issues = state.get("issues", 0)
    threshold = state.get("threshold", 80)
    quality_score = max(0, 100 - (complexity + issues * 5))
    state["quality_score"] = quality_score
    if quality_score < threshold:
        state["complexity"] = max(0, state.get("complexity", 0) - 5)
        state["issues"] = max(0, state.get("issues", 0) - 1)
        state["next"] = "extract"
    return {}
def build_code_review_graph():
    nodes = {
        "extract": extract_functions,
        "complexity": check_complexity,
        "issues": detect_issues,
        "improve": suggest_improvements,
    }
    edges = {
        "extract": "complexity",
        "complexity": "issues",
        "issues": "improve",
        "improve": None,
    }
    start = "extract"
    return {"nodes": nodes, "edges": edges, "start": start}