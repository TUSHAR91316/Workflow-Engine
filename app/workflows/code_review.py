def extract_functions(state):
    code = state.get("code", "")
    return {"functions": code.count("def ")}

def check_complexity(state):
    code = state.get("code", "")
    functions = state.get("functions", 0)
    lines = len(code.splitlines())
    complexity = functions * 10 + max(0, lines - 50) // 5
    return {"complexity": complexity}

def detect_issues(state):
    code = state.get("code", "")
    todos = code.count("TODO")
    prints = code.count("print(")
    return {"issues": todos + prints}

def suggest_improvements(state):
    complexity = state.get("complexity", 0)
    issues = state.get("issues", 0)
    threshold = state.get("threshold", 80)

    score = max(0, 100 - (complexity + issues * 5))
    state["quality_score"] = score

    if score < threshold:
        state["complexity"] = max(0, complexity - 5)
        state["issues"] = max(0, issues - 1)
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
        "improve": None
    }
    return {"nodes": nodes, "edges": edges, "start": "extract"}
