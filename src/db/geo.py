# pylint: disable=W0622
"""
    DB functions for company
"""
from sqlalchemy import select

from src.Model import Company
from src.db.lib import get_db_session, get_db_url_prod
from src.logger import logger


def get_company(id: int, url: str = get_db_url_prod()) -> None | Company:
    """get company by id"""
    with get_db_session(url) as session:
        try:
            return session.execute(select(Company).where(Company.id == id)).scalars().one()
        except Exception as e:
            logger().debug(f"get_user : {str(e)}")
            return None
