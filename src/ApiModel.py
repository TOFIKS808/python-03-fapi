from pydantic import BaseModel


class Post(BaseModel):
    user_id: int
    title: str
    body: str
