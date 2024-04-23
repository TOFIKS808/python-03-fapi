# pylint: disable=W0622
"""
    DB functions for geo
"""
from sqlalchemy import select

from src.Model import Geo
from src.db.lib import get_db_session
from src.logger import logger


def get_geo(id: int) -> None | Geo:
    """get geo by id"""
    with get_db_session() as session:
        try:
            return session.execute(select(Geo).where(Geo.id == id)).scalars().one()
        except Exception as e:
            logger().debug(f"get_geo : {str(e)}")
            return None
