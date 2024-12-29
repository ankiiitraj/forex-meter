from fastapi import FastAPI
from routers import ForexRouter
from service.runner.SchduleRunner import SchduleRunner
from service.adapter.HDFCAdapter.HDFCAdapter import HDFCAdapter

app = FastAPI()

app.include_router(ForexRouter.router)

@app.get("/ping")
def ping_poing():
    schdule_runner = SchduleRunner()
    schdule_runner.run(HDFCAdapter())
    return "pong"