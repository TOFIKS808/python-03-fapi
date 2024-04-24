import unittest
from tests.DbTestCase import DbTestTestCase
from src.db.post import get_item, get_collection, delete_item, create_item, update_item
from src.Model import Post
from src.ApiModel import PostCreate, PostUpdate


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
        api_post = PostCreate(user_id=1, title='title', body='body')

        post = create_item(api_post)
        self.assertIsInstance(post, Post)
        self.assertIsNotNone(post.id)
        count_after_create = len(get_collection())
        self.assertEqual(count_prior_create + 1, count_after_create)

    def test_update_item(self):
        """ testing update item"""
        post1 = get_item(1)
        post2 = update_item(1, PostUpdate(title='title', body='body'))

        self.assertNotEqual(post1.title, post2.title)
        self.assertNotEqual(post1.body, post2.body)
        self.assertEqual(post2.title, 'title')
        self.assertEqual(post2.body, 'body')


if __name__ == '__main__':
    unittest.main()
