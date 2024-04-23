# pylint: disable=W0622
"""
    API functionality for address endpoints
"""

from fastapi import HTTPException
from src.db.address import get_address


def address_get_item(id: int):
    """ Get address by id """
    result = get_address(id)
    if result:
        return result

    raise HTTPException(status_code=404, detail="Address not found")
