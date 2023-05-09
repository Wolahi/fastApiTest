from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from starlette import status

from .base_config import SECRET
from .models import User
from src.database import get_async_session
from .schemas import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
ALGORITHM = "HS256"




async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
