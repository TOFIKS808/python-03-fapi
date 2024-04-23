# pylint: disable=W0622
"""
    DB functions for address
"""
from sqlalchemy import select

from src.Model import Address
from src.db.lib import get_db_session
from src.logger import logger


def get_address(id: int) -> None | Address:
    """get address by id"""
    with get_db_session() as session:
        try:
            return session.execute(select(Address).where(Address.id == id)).scalars().one()
        except Exception as e:
            logger().debug(f"get_address : {str(e)}")
            return None
