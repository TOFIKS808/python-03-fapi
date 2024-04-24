# pylint: disable=W0622
"""
    DB functions for posts
"""
from typing import List
from sqlalchemy import select, delete

from src.Model import Post
from src.ApiModel import Post as ApiPost
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


def get_posts() -> List[Post]:
    """get all posts"""
    with get_db_session() as session:
        try:
            return session.execute(select(Post)).scalars().all()
        except Exception as e:
            logger().debug(f"get_posts : {str(e)}")
            return None


def delete_item(id: int):
    """delete post by id"""
    with get_db_session() as session:
        try:
            r = session.execute(delete(Post).where(Post.id == id))
            session.commit()
            return bool(r.rowcount)
        except Exception as e:
            logger().debug(f"delete_post: {str(e)}")


def create_item(post: ApiPost):
    """create post"""
    db_post = Post(title=post.title, body=post.body, user_id=post.user_id)

    with get_db_session() as session:
        try:
            r = session.add(db_post)
            print(r)
            session.commit()

        except Exception as e:
            logger().debug(f"delete_post: {str(e)}")
