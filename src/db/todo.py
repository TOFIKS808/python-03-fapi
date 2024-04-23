# pylint: disable=W0622
"""
    DB functions for todo
"""
from sqlalchemy import select

from src.Model import Todo
from src.db.lib import get_db_session
from src.logger import logger


def get_todo(id: int) -> None | Todo:
    """get todo by id"""
    with get_db_session() as session:
        try:
            return session.execute(select(Todo).where(Todo.id == id)).scalars().one()
        except Exception as e:
            logger().debug(f"get_todo : {str(e)}")
            return None
