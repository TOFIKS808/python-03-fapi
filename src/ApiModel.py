# pylint: disable = C0103
""" API Model """

from pydantic import BaseModel


class PostCreate(BaseModel):
    """ Post Model """
    user_id: int
    title: str
    body: str


class PostUpdate(BaseModel):
    """ Post Model """
    title: str
    body: str
