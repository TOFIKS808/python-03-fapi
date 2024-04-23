# pylint: disable=C0103

""" Unittest helper class for DB operations"""
import unittest
from os import getenv
import sqlalchemy as sql
from sqlalchemy_utils import database_exists, drop_database
from sqlalchemy import orm

from src.Model import User, Post, Comment, Album, Photo, Todo

from src.populate_db import create_db, create_schema, endpoint_users, endpoint_posts, endpoint_comments, \
    endpoint_albums, endpoint_photos, endpoint_todos


class DbTestTestCase(unittest.TestCase):
    """DB test case"""

    def setUp(self) -> None:
        """set up db"""
        url = getenv('DB_URL')

        self.__func_create_db(url)
        self.__func_create_schema(url)
        self.__func_endpoint_users(url)
        self.__func_endpoint_posts(url)
        self.__func_endpoint_comments(url)
        self.__func_endpoint_albums(url)
        self.__func_endpoint_photos(url)
        self.__func_endpoint_todos(url)

    def tearDown(self) -> None:
        """tear down db"""
        url = getenv('DB_URL')

        engine = sql.create_engine(url)
        if database_exists(engine.url):
            drop_database(engine.url)

    def __func_create_db(self, url: str):
        """Database creation test"""
        create_db(url)
        engine = sql.create_engine(url)
        self.assertTrue(database_exists(engine.url))

    def __func_create_schema(self, url: str):
        """ Tables creation test """
        create_schema(url)
        engine = sql.create_engine(url)
        self.assertTrue(sql.inspect(engine).has_table('address'))
        self.assertTrue(sql.inspect(engine).has_table('album'))
        self.assertTrue(sql.inspect(engine).has_table('comment'))
        self.assertTrue(sql.inspect(engine).has_table('company'))
        self.assertTrue(sql.inspect(engine).has_table('geo'))
        self.assertTrue(sql.inspect(engine).has_table('photo'))
        self.assertTrue(sql.inspect(engine).has_table('post'))
        self.assertTrue(sql.inspect(engine).has_table('todo'))
        self.assertTrue(sql.inspect(engine).has_table('users'))

    def __func_endpoint_users(self, url: str):
        """ Populating users table test """

        endpoint_users(url)
        engine = sql.create_engine(url)
        with orm.Session(engine) as session:
            users = session.execute(sql.select(User).order_by(User.id)).scalars().all()
            self.assertEqual(10, len(users))
            user: User = users[1]
            self.assertIsInstance(user, User)
            self.assertEqual(2, user.id)
            self.assertEqual("Ervin Howell", user.name)
            self.assertEqual("Antonette", user.username)
            self.assertEqual("Shanna@melissa.tv", user.email)
            self.assertEqual("Victor Plains", user.address.street)
            self.assertEqual("Suite 879", user.address.suite)
            self.assertEqual("Wisokyburgh", user.address.city)
            self.assertEqual("90566-7771", user.address.zipcode)
            self.assertEqual("-43.9509", user.address.geo.lat)
            self.assertEqual("-34.4618", user.address.geo.long)

    def __func_endpoint_posts(self, url: str):
        """ Populating post table test """

        endpoint_posts(url)
        engine = sql.create_engine(url)
        with orm.Session(engine) as session:
            posts = session.execute(sql.select(Post).order_by(Post.id)).scalars().all()
            self.assertEqual(100, len(posts))
            post: Post = posts[1]
            self.assertEqual(1, post.user_id)
            self.assertEqual(2, post.id)
            self.assertEqual("qui est esse", post.title)
            self.assertEqual(post.body,
                             "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores"
                             " neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam"
                             " non debitis possimus qui neque nisi nulla")

    def __func_endpoint_comments(self, url: str):
        """ Populating comment table test """

        endpoint_comments(url)
        engine = sql.create_engine(url)
        with orm.Session(engine) as session:
            comments = session.execute(sql.select(Comment).order_by(Comment.id)).scalars().all()
            self.assertEqual(500, len(comments))
            comment: Comment = comments[1]
            self.assertEqual(1, comment.post_id)
            self.assertEqual(2, comment.id)
            self.assertEqual("quo vero reiciendis velit similique earum", comment.name)
            self.assertEqual("Jayne_Kuhic@sydney.com", comment.email)
            self.assertEqual(comment.body, "est natus enim nihil est dolore omnis voluptatem numquam\net omnis"
                                           " occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint"
                                           " nostrum voluptatem reiciendis et")

    def __func_endpoint_albums(self, url: str):
        """ Populating album table test """

        endpoint_albums(url)
        engine = sql.create_engine(url)
        with orm.Session(engine) as session:
            albums = session.execute(sql.select(Album).order_by(Album.id)).scalars().all()
            self.assertEqual(100, len(albums))
            album: Album = albums[1]
            self.assertEqual(1, album.user_id)
            self.assertEqual(2, album.id)
            self.assertEqual(album.title, "sunt qui excepturi placeat culpa")

    def __func_endpoint_photos(self, url: str):
        """ Populating photo table test """

        endpoint_photos(url)
        engine = sql.create_engine(url)
        with orm.Session(engine) as session:
            photos = session.execute(sql.select(Photo).order_by(Photo.id)).scalars().all()
            self.assertEqual(5000, len(photos))
            photo: Photo = photos[1]
            self.assertEqual(1, photo.album_id)
            self.assertEqual(2, photo.id)
            self.assertEqual(photo.title, "reprehenderit est deserunt velit ipsam")
            self.assertEqual(photo.url, "https://via.placeholder.com/600/771796")
            self.assertEqual(photo.thumbnail_url, "https://via.placeholder.com/150/771796")

    def __func_endpoint_todos(self, url: str):
        """ Populating todo table test """

        endpoint_todos(url)
        engine = sql.create_engine(url)
        with orm.Session(engine) as session:
            todos = session.execute(sql.select(Todo).order_by(Todo.id)).scalars().all()
            self.assertEqual(200, len(todos))
            todo: Todo = todos[1]
            self.assertEqual(1, todo.user_id)
            self.assertEqual(2, todo.id)
            self.assertEqual(todo.title, "quis ut nam facilis et officia qui")
            self.assertEqual(todo.completed, False)
