# Mini Workflow Engine

This project is a minimal, yet extensible workflow and graph engine built with FastAPI. It's designed to showcase a clean backend architecture, asynchronous execution, and a modular design, inspired by graph-based execution engines like LangGraph.

At its core, the engine executes a series of nodes (Python functions) operating on a shared state. It manages the transitions, branching, looping, and logging of the entire workflow.

## Key Features

*   **Workflow Engine**:
    *   Nodes represented as standard Python functions.
    *   Directed edges define the execution order.
    *   A shared, mutable state is passed through the graph.
    *   Dynamic branching by setting `state["next"]`.
    *   Looping capabilities by repeating nodes until a condition is met.
    *   Detailed execution logs for traceability and debugging.
    *   Async-safe execution via background tasks.
*   **Tool Registry**:
    *   A simple registry for attaching callable tools and utilities.
    *   Easily extendable to add more agentic functionality.
*   **FastAPI Endpoints**:
    *   `POST /graph/create`: Creates a new workflow graph.
    *   `GET /graph/create`: A convenience endpoint for browser-based testing.
    *   `POST /graph/run`: Executes a workflow with an initial state.
    *   `GET /graph/state/{run_id}`: Retrieves the status and final state of a workflow run.
*   **Example Workflow: Code Review Agent**:
    *   A deterministic, rule-based workflow that analyzes Python code.
    *   It extracts functions, calculates complexity, detects basic issues, and suggests improvements.
    *   The workflow loops until the code's quality score meets a specified threshold.

## Project Structure

```
app/
├── main.py
├── routers/
│   └── graph.py
├── engine/
│   ├── workflow.py
│   └── registry.py
├── workflows/
│   └── code_review.py
└── db/
    └── memory_store.py
requirements.txt
README.md
```

This structure promotes modularity and separation of concerns, making the engine easy to extend and maintain.

## Getting Started

Follow these steps to get the workflow engine running on your local machine.

### 1. Set up the Environment

First, create and activate a virtual environment:

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies

Install the required Python packages using pip:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Start the Server

Launch the FastAPI application with Uvicorn:

```bash
uvicorn app.main:app --reload
```

The `--reload` flag enables hot-reloading for development.

### 4. Explore the API

Once the server is running, you can access the interactive API documentation at:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## API Usage

### 1. Create a Workflow Graph

Send a `POST` request to `/graph/create` to initialize a workflow.

**Request:**
```json
{
  "graph_name": "code_review"
}
```

**Response:**
```json
{
  "graph_id": "..."
}
```

For quick testing, you can also use the `GET /graph/create` endpoint in your browser.

### 2. Run the Workflow

Execute the created workflow by sending a `POST` request to `/graph/run`.

**Request Body:**
```json
{
  "graph_id": "<your_graph_id>",
  "initial_state": {
    "code": "def my_function():\n    pass",
    "threshold": 80
  }
}
```

**Response:**
```json
{
  "run_id": "..."
}
```

### 3. Retrieve the Run State

Check the status and result of a workflow run with a `GET` request to `/graph/state/<run_id>`.

The response will include the run's `status`, the `final_state`, and the full `execution_log`.

## Engine Capabilities

*   Graph-based processing
*   Dynamic branching
*   Conditional looping
*   Asynchronous background execution
*   Modular workflow definitions
*   Tool registry for extending functionality
*   In-memory task tracking
*   Clean, async-capable design

These features are designed to meet the core evaluation criteria of clarity, structure, state-driven transitions, async hygiene, and maintainability.

## Future Improvements

While this engine is a solid foundation, here are some potential enhancements:

*   **WebSocket Log Streaming**: Real-time streaming of execution logs.
*   **Persistent Storage**: Integration with SQLite or PostgreSQL for durable storage.
*   **Graph Inspector**: A visual inspector or metadata endpoint for graphs.
*   **Schema Validation**: Use Pydantic for input/output validation at each node.
*   **Workflow Registration API**: An endpoint to register multiple workflows.
*   **Containerization**: Docker support for production-ready deployments.
*   **CI/CD**: Unit tests and a CI pipeline with GitHub Actions.

## License

This project is submitted as part of an AI Engineering Internship assignment and is intended to demonstrate backend engineering principles and clean system design.
