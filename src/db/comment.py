# pylint: disable=W0622
"""
    DB functions for comment
"""
from sqlalchemy import select

from src.Model import Comment
from src.db.lib import get_db_session
from src.logger import logger


def get_comment(id: int) -> None | Comment:
    """get company by id"""
    with get_db_session() as session:
        try:
            return session.execute(select(Comment).where(Comment.id == id)).scalars().one()
        except Exception as e:
            logger().debug(f"get_comment : {str(e)}")
            return None
