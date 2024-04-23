# pylint: disable=W0622
"""
    API functionality for album endpoints
"""

from fastapi import HTTPException
from src.db.album import get_album


def albums_get_item(id: int):
    """ Get a album by id """
    result = get_album(id)
    if result:
        return result

    raise HTTPException(status_code=404, detail="User not found")
