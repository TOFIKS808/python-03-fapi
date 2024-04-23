# pylint: disable=W0622
"""
    API functionality for user endpoints
"""

from fastapi import HTTPException
from src.db.users import get_user, get_users


def users_get_item(id: int):
    """ Get a user by id """
    result = get_user(id)
    if result:
        return result

    raise HTTPException(status_code=404, detail="User not found")


def users_get_collection():
    """ Get a users"""
    result = get_users()
    if result:
        return result

    raise HTTPException(status_code=404, detail="Users not found")
