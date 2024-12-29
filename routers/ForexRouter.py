from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/forex")

class ForexRouter:

    @router.get("/")
    def hello():
        return """Hello, world!"""