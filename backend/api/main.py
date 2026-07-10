from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.models import ChatRequest
from backend.workflows.multi_agent_workflow import run_workflow

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return{
        "message":"Multi Agent AI API is running"
    }

@app.post("/chat")
def chat(request : ChatRequest):

    result  = run_workflow(
        request.query
    )

    return result