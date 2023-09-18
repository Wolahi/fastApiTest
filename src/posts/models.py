from sqlalchemy import MetaData, Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import DeclarativeMeta, declarative_base
from src.auth.models import user

Base: DeclarativeMeta = declarative_base()
metadata_posts = MetaData()

post = Table(
    "post",
    metadata_posts,
    Column("id", Integer, primary_key=True, autoincrement=True, unique=True),
    Column('user_id', Integer, ForeignKey(user.c.id), nullable=False),
    Column('text', String , nullable=True),
    Column('count_likes', Integer, nullable=True),
)


class PostTable(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = Column('text', String , nullable=True),
    text = Column(Integer, ForeignKey(user.c.id), nullable=False),
    count_likes = Column(Integer, nullable=True),
