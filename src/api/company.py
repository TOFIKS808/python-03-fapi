# pylint: disable=W0622
"""
    API functionality for company endpoints
"""

from fastapi import HTTPException
from src.db.company import get_company


def company_get_item(id: int):
    """ Get a company by id """
    result = get_company(id)
    if result:
        return result

    raise HTTPException(status_code=404, detail="Company not found")
