
from pydantic import BaseModel


class Post(BaseModel):
    id: int
    user_id: int
    text: str
    count_likes: int
