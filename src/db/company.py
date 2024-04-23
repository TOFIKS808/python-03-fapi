# pylint: disable=W0622
"""
    DB functions for company
"""
from sqlalchemy import select

from src.Model import Company
from src.db.lib import get_db_session
from src.logger import logger


def get_company(id: int) -> None | Company:
    """get company by id"""
    with get_db_session() as session:
        try:
            return session.execute(select(Company).where(Company.id == id)).scalars().one()
        except Exception as e:
            logger().debug(f"get_company : {str(e)}")
            return None
