from fastapi import FastAPI
from app.routers.graph import router as graph_router
from app.engine.registry import registry
from app.workflows.code_review import build_code_review_graph
app = FastAPI(title="Mini Workflow Engine - AI Eng Assignment")
app.include_router(graph_router)
@app.on_event("startup")
def startup_event():
    def dummy_tool(x):
        return {"result": x}
    registry.register("dummy", dummy_tool)
    cfg = build_code_review_graph()
    pass

@app.get("/")
def hello():
    return {"msg": "Mini Workflow Engine - use /graph/create and /graph/run"}