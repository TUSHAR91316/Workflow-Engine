from fastapi import FastAPI
from app.routers.graph import router as graph_router
from app.engine.registry import registry

app = FastAPI(title="Mini Workflow Engine - AI Eng Assignment")

app.include_router(graph_router)

@app.on_event("startup")
def startup_event():
    # demo tool
    def dummy_tool(x):
        return {"result": x}
    registry.register("dummy", dummy_tool)

@app.get("/")
def hello():
    return {"msg": "Mini Workflow Engine - use /graph/create and /graph/run"}
