from fastapi import Depends
from backend.auth.dependencies import get_current_user

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend.api.models import ChatRequest
from backend.workflows.multi_agent_workflow import run_workflow

from backend.auth.models import (
    RegisterRequest,
    LoginRequest,
)

from backend.auth.database import users_collection
from backend.auth.auth import (
    hash_password,
    verify_password,
)
from backend.auth.jwt_handler import create_access_token

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
    return {
        "message": "Multi Agent AI API is running"
    }


@app.post("/register")
def register(request: RegisterRequest):

    existing_user = users_collection.find_one(
        {
            "email": request.email
        }
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists",
        )

    users_collection.insert_one(
        {
            "username": request.username,
            "email": request.email,
            "password": hash_password(request.password),
        }
    )

    return {
        "message": "Registration successful"
    }


@app.post("/login")
def login(request: LoginRequest):

    user = users_collection.find_one(
        {
            "email": request.email
        }
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    if not verify_password(
        request.password,
        user["password"],
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    token = create_access_token(
        {
            "sub": user["email"],
            "user_id": str(user["_id"]),
        }
    )

    return {
        "access_token": token,
        "username": user["username"],
    }

@app.post("/chat")
def chat(
    request: ChatRequest,
    current_user: str = Depends(get_current_user)
):

    result = run_workflow(
        request.query,
        current_user
    )

    return {
        "user": current_user,
        "response": result
    }