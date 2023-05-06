from typing import List

from sqlalchemy import MetaData, Table, Column, ARRAY, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeMeta, declarative_base

Base: DeclarativeMeta = declarative_base()
metadata_auth = MetaData()

user = Table(
    "user",
    metadata_auth,
    Column("id", Integer, primary_key=True, autoincrement=True, unique=True),
    Column("email", String, unique=True, index=True, nullable=False),
    Column("username", String, nullable=False),
    Column("surname", String, nullable=False),
    Column("avatar", String),
    Column("info", String, nullable=False),
    Column("city", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("num_telephone", String, nullable=False),
    Column("friends", ARRAY(Integer)),
    Column("is_active", Boolean, nullable=False),
    Column("is_superuser", Boolean, nullable=False),
    Column("is_verified", Boolean, nullable=False)
)


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, unique=True
    )
    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
    )
    username: Mapped[str] = mapped_column(
        String(length=320), nullable=False
    )
    surname: Mapped[str] = mapped_column(
        String(length=320), nullable=False
    )
    avatar: Mapped[str] = mapped_column(
        String(length=1024)
    )
    info: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    city: Mapped[str] = mapped_column(
        String(length=320), nullable=False
    )
    friends: Mapped[List[int]] = mapped_column(
        ARRAY(Integer)
    )
    num_telephone: Mapped[str] = mapped_column(
        String(length=320), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
