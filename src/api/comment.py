# pylint: disable=W0622
"""
    API functionality for comment endpoints
"""

from fastapi import HTTPException
from src.db.comment import get_comment


def comments_get_item(id: int):
    """ Get a comment by id """
    result = get_comment(id)
    if result:
        return result

    raise HTTPException(status_code=404, detail="Comment not found")
