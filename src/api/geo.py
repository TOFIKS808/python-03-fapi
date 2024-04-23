# pylint: disable=W0622
"""
    API functionality for user endpoints
"""

from fastapi import HTTPException
from src.db.geo import get_geo


def geo_get_item(id: int):
    """ Get a geo by id """
    result = get_geo(id)
    if result:
        return result

    raise HTTPException(status_code=404, detail="Geo not found")
