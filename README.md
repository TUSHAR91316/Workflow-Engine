Mini Workflow Engine – AI Engineering Assignment

This project implements a minimal yet extensible workflow/graph engine using FastAPI.
It demonstrates clean backend architecture, async execution, modular design, and an example “Code Review Agent” workflow.
The system behaves like a simplified LangGraph-style execution engine, where nodes operate on shared state and the engine manages transitions, branching, looping, and logging.

Key Features
1. Workflow Engine

Nodes represented as Python functions

Directed edges defining execution order

Shared mutable state passed through the graph

Branching via setting state["next"]

Looping by repeating nodes until a computed condition is satisfied

Execution logs for debugging and traceability

Async-safe execution via background tasks

2. Tool Registry

Simple registry for attaching callable utilities or tools

Easily extendable for future agent functionality

3. FastAPI Endpoints

POST /graph/create

GET /graph/create (convenience for browser testing)

POST /graph/run

GET /graph/state/{run_id}

4. Example Workflow: Code Review Agent

A deterministic, rule-based workflow that:

Extracts functions from code

Calculates complexity

Detects basic issues

Suggests improvements

Loops until the quality score meets a threshold

Project Structure

app/
  main.py
  routers/
    graph.py
  engine/
    workflow.py
    registry.py
  workflows/
    code_review.py
  db/
    memory_store.py
requirements.txt
README.md

This structure keeps logic isolated, modular, and easy to extend.

How to Run
Step 1: Create virtual environment

Windows
python -m venv .venv
.venv\Scripts\activate

macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

Step 2: Install dependencies

pip install --upgrade pip
pip install -r requirements.txt

Step 3: Start the server

uvicorn app.main:app --reload

Step 4: Open API docs

http://127.0.0.1:8000/docs

API Usage
1. Create a Workflow Graph

POST /graph/create
Body:
{ "graph_name": "code_review" }
Response:
{ "graph_id": "..." }

For quick browser testing:
GET /graph/create

2. Run Workflow

POST /graph/run
Body example:
{
"graph_id": "<graph_id>",
"initial_state": {
"code": "def a(): pass",
"threshold": 80
}
}

Response:
{ "run_id": "..." }

3. Retrieve Run State

GET /graph/state/<run_id>
Returns:

status

final state

execution log

What the Engine Supports

Graph-based processing

Dynamic branching

Conditional looping

Background execution

Modular workflow definitions

Tool registry

In-memory task tracking

Clean async-capable design

This matches the expected core evaluation criteria for the assignment:
clarity, structure, state-driven transitions, async hygiene, and maintainability.

Future Improvements (If Time Allowed)

WebSocket log streaming for real-time node execution updates

Persistent storage using SQLite/PostgreSQL

Visual graph inspector or metadata endpoint

Node input/output validation using Pydantic models

Multiple workflow registration API

Docker support for production deployment

Unit tests and GitHub Actions continuous integration

These enhancements would elevate the engine from minimal demo to production-grade orchestration.

License

This project is submitted as part of an AI Engineering Internship assignment and is intended to demonstrate backend engineering principles and clean system design.