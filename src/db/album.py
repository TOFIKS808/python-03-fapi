# pylint: disable=W0622
"""
    DB functions for album
"""
from sqlalchemy import select
from src.Model import Album
from src.db.lib import get_db_session
from src.logger import logger


def get_album(id: int) -> None | Album:
    """get album by id"""
    with get_db_session() as session:
        try:
            return session.execute(select(Album).where(Album.id == id)).scalars().one()
        except Exception as e:
            logger().debug(f"get_album : {str(e)}")
            return None
