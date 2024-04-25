# pylint: disable=W0622
"""
    API functionality for post endpoints
"""

from fastapi import HTTPException
from src.db.post import get_item, delete_item, create_item, update_item
from src.ApiModel import PostCreate


def posts_get_item(id: int):
    """ Get a post by id """
    result = get_item(id)
    if result:
        return result

    raise HTTPException(status_code=404, detail="Post not found")


def posts_delete_item(id: int):
    """ Delete a post by id """
    result = delete_item(id)

    if result:
        return ''

    raise HTTPException(status_code=404, detail="Post not found")


def posts_create_item(post: PostCreate):
    """ Create a new post """
    obj = create_item(post)

    if obj:
        return obj

    raise HTTPException(status_code=400)


def posts_update_item(id: int, post: PostCreate):
    """ Create a new post """
    obj = update_item(id, post)

    if obj:
        return obj

    raise HTTPException(status_code=400)
