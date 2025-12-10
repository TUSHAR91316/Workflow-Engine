from fastapi import APIRouter, HTTPException, BackgroundTasks
from uuid import uuid4
from pydantic import BaseModel
from typing import Dict, Any

from app.engine.workflow import Workflow, Node
from app.db.memory_store import graphs, runs
from app.workflows.code_review import build_code_review_graph

router = APIRouter()

class GraphCreateRequest(BaseModel):
    graph_name: str

class GraphRunRequest(BaseModel):
    graph_id: str
    initial_state: Dict[str, Any]


@router.post("/graph/create")
async def create_graph(req: GraphCreateRequest):
    if req.graph_name != "code_review":
        raise HTTPException(status_code=400, detail="Only 'code_review' supported")

    cfg = build_code_review_graph()

    nodes = {name: Node(name, func) for name, func in cfg["nodes"].items()}
    wf = Workflow(nodes, cfg["edges"], cfg["start"])

    graph_id = str(uuid4())
    graphs[graph_id] = wf
    return {"graph_id": graph_id}


@router.post("/graph/run")
async def run_graph(req: GraphRunRequest, background_tasks: BackgroundTasks):
    wf = graphs.get(req.graph_id)
    if wf is None:
        raise HTTPException(status_code=404, detail="Graph not found")

    run_id = str(uuid4())
    runs[run_id] = {
        "status": "running",
        "state": req.initial_state,
        "log": [],
    }

    async def _execute():
        try:
            final_state, log = await wf.run(req.initial_state, [])
            runs[run_id]["status"] = "completed"
            runs[run_id]["state"] = final_state
            runs[run_id]["log"] = log
        except Exception as e:
            runs[run_id]["status"] = "failed"
            runs[run_id]["log"] = [f"Execution error: {e}"]

    background_tasks.add_task(_execute)
    return {"run_id": run_id}


@router.get("/graph/state/{run_id}")
async def get_state(run_id: str):
    r = runs.get(run_id)
    if not r:
        raise HTTPException(status_code=404, detail="Run not found")
    return r
