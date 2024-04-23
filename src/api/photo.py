# pylint: disable=W0622
"""
    API functionality for photo endpoints
"""

from fastapi import HTTPException
from src.db.photo import get_photo


def photo_get_item(id: int):
    """ Get a photo by id """
    result = get_photo(id)
    if result:
        return result

    raise HTTPException(status_code=404, detail="Photo not found")
