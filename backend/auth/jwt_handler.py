from jose import jwt
from datetime import datetime, timedelta
from backend.utils.env_loader import *
import os



SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("JWT_ALGORITHM")

if not SECRET_KEY:
    raise ValueError("JWT_SECRET_KEY environment variable is not set.")

if not ALGORITHM:
    raise ValueError("JWT_ALGORITHM environment variable is not set.")


def create_access_token(data: dict):

    payload = data.copy()

    payload["exp"] = datetime.utcnow() + timedelta(days=7)

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )

    return token


def verify_access_token(token: str):

    return jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM],
    )