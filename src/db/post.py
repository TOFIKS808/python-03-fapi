# pylint: disable=W0622
"""
    DB functions for posts
"""
from sqlalchemy import select

from src.Model import Post
from src.db.lib import get_db_session
from src.logger import logger


def get_post(id: int) -> None | Post:
    """get post by id"""
    with get_db_session() as session:
        try:
            return session.execute(select(Post).where(Post.id == id)).scalars().one()
        except Exception as e:
            logger().debug(f"get_post: {str(e)}")
            return None
