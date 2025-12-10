# Mini Workflow Engine — AI Engineering Internship

This project implements a small workflow engine with FastAPI. It supports nodes, edges, branching, and looping, and includes an example Code Review workflow (rule-based).

## How to run

1. Create a virtual environment and install dependencies

For macOS / Linux:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Start the server

```bash
uvicorn app.main:app --reload
```

The server will be available at `http://127.0.0.1:8000` by default.

## Endpoints

- `POST /graph/create`
	- Body: `{"graph_name": "code_review"}`
	- Returns: `graph_id`

- `POST /graph/run`
	- Body example:
```json
{
	"graph_id": "<graph_id>",
	"initial_state": {
		"code": "def a():\n    pass",
		"threshold": 80,
	}
}
```
	- Returns: `run_id`

- `GET /graph/state/{run_id}`
	- Returns: status, state, and log for the run

## Example curl requests

Create a graph:
```bash
curl -X POST "http://127.0.0.1:8000/graph/create" -H "Content-Type: application/json" -d '{"graph_name":"code_review"}'
```

Start a run:
```bash
curl -X POST "http://127.0.0.1:8000/graph/run" -H "Content-Type: application/json" -d '{"graph_id":"<id>","initial_state":{"code":"def a():\\n    pass","threshold":80}}'
```

Get run state:
```bash
curl "http://127.0.0.1:8000/graph/state/<run_id>"
```
