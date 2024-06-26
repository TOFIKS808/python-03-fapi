# pylint: disable=W0622
"""
    DB functions for posts
"""
from typing import List
from sqlalchemy import select, delete

from src.Model import Post
from src.ApiModel import PostCreate, PostUpdate
from src.db.lib import get_db_session
from src.logger import logger


def get_item(id: int) -> None | Post:
    """get post by id"""
    with get_db_session() as session:
        try:
            return session.execute(select(Post).where(Post.id == id)).scalars().one()
        except Exception as e:
            logger().debug(f"get_post: {str(e)}")
    return None


def get_collection() -> List[Post]:
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
    return None


def create_item(post: PostCreate) -> None | Post:
    """create post"""
    db_post = Post(title=post.title, body=post.body, user_id=post.user_id)

    with get_db_session() as session:
        try:
            session.add(db_post)
            session.commit()

            return get_item(db_post.id)

        except Exception as e:
            logger().debug(f"create_post: {str(e)}")
    return None


def update_item(id: int, post: PostUpdate) -> None | Post:
    """update post"""

    with get_db_session() as session:
        try:
            session.query(Post).filter(Post.id == id).update({'title': post.title, 'body': post.body})
            session.commit()
            return get_item(id)
        except Exception as e:
            logger().debug(f"update_post: {str(e)}")
    return None
