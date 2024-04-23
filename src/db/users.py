# pylint: disable=W0622
"""
    DB functions for users
"""
from sqlalchemy import select

from src.Model import User
from src.db.lib import get_db_session
from src.logger import logger


def get_user(id: int) -> None | User:
    """get user by id"""
    with get_db_session() as session:
        try:
            return session.execute(select(User).where(User.id == id)).scalars().one()
        except Exception as e:
            logger().debug(f"get_user : {str(e)}")
            return None
