# pylint: disable=W0622
"""
    API functionality for post endpoints
"""

from fastapi import HTTPException
from src.db.post import get_post


def posts_get_item(id: int):
    """ Get a post by id """
    result = get_post(id)
    if result:
        return result

    raise HTTPException(status_code=404, detail="Post not found")
