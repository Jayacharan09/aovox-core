from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator import AOVOXOrchestrator


app = FastAPI()
orchestrator = AOVOXOrchestrator()


class UserRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(request: UserRequest):
    response = orchestrator.process(request.message)
    return {"response": response}
