import unittest
from tests.DbTestCase import DbTestTestCase
from src.db.post import get_item, get_collection, delete_item, create_item
from src.Model import Post
from src.ApiModel import Post as ApiPost


class PostTestCase(DbTestTestCase):
    def test_get_item_not_existing(self):
        """ Testing get post with an item that does not exist """
        self.assertIsNone(get_item(id=-11))

    def test_get_item(self):
        """ Testing if output is instance of the Post class """
        self.assertIsInstance(get_item(id=1), Post)

    def test_delete_item(self):
        """testing delete item"""
        count_prior_delete = len(get_collection())
        delete_item(1)
        delete_item(1)
        count_after_delete = len(get_collection())
        self.assertEqual(count_prior_delete - 1, count_after_delete)
        self.assertIsNone(get_item(1))

    def test_create_item(self):
        count_prior_create = len(get_collection())
        api_post = ApiPost(user_id=1, title='title', body='body')

        post = create_item(api_post)
        self.assertIsInstance(post, Post)
        self.assertIsNotNone(post.id)
        count_after_create = len(get_collection())
        self.assertEqual(count_prior_create + 1, count_after_create)


if __name__ == '__main__':
    unittest.main()
