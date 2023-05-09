from typing import Annotated

import fastapi
from fastapi import FastAPI, UploadFile, File
from fastapi_users import FastAPIUsers
from fastapi.middleware.cors import CORSMiddleware

from .auth.base_config import auth_backend
from .auth.manager import get_user_manager
from .auth.models import User
from .auth.schemas import UserRead, UserCreate, UserUpdate

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
app = FastAPI(
    title="VK TESt"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)


@app.post("/img/change")
def upload_file(file: UploadFile = File(...)):
    return file
