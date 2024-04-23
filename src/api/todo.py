# pylint: disable=W0622
"""
    API functionality for todo endpoints
"""

from fastapi import HTTPException
from src.db.todo import get_todo


def company_get_item(id: int):
    """ Get a todo by id """
    result = get_todo(id)
    if result:
        return result

    raise HTTPException(status_code=404, detail="Todo not found")
