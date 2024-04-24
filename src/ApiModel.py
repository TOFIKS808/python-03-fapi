from pydantic import BaseModel


class PostCreate(BaseModel):
    user_id: int
    title: str
    body: str


class PostUpdate(BaseModel):
    title: str
    body: str
