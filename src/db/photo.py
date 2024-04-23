# pylint: disable=W0622
"""
    DB functions for photo
"""
from sqlalchemy import select

from src.Model import Photo
from src.db.lib import get_db_session
from src.logger import logger


def get_photo(id: int) -> None | Photo:
    """get photo by id"""
    with get_db_session() as session:
        try:
            return session.execute(select(Photo).where(Photo.id == id)).scalars().one()
        except Exception as e:
            logger().debug(f"get_photo : {str(e)}")
            return None
