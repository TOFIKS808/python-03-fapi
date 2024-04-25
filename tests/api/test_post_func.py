""" Tests for the post function """
from tests.DbTestCase import DbTestTestCase
from src.Model import Post
from src.ApiModel import PostCreate, PostUpdate
from src.api.post import posts_create_item, posts_update_item


class PostFuncTestCase(DbTestTestCase):
    """ Test cases for posts functions """
    def test_post_create_item(self):
        """ Test post creation """

        post = PostCreate(user_id=1, title='Test title',body='Test Body')
        item = posts_create_item(post)
        self.assertIsInstance(item, Post)
        self.assertEqual(item.title, 'Test title')
        self.assertEqual(item.body, 'Test Body', )
        self.assertEqual(item.user_id, 1)

    def test_post_update_item(self):
        """ Test post update """

        post = PostUpdate(title='Test title',body='Test Body')
        item = posts_update_item(1, post)
        self.assertIsInstance(item, Post)
        self.assertEqual(item.title, 'Test title')
        self.assertEqual(item.body, 'Test Body', )
        self.assertEqual(item.user_id, 1)
