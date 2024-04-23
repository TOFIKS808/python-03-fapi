"""
    Testing functional tests for db comment
"""
import unittest
from tests.DbTestCase import DbTestTestCase
from src.db.comment import get_comment
from src.Model import Comment


class CommentDbTestCase(DbTestTestCase):
    """ Testing class for db comment """

    def test_get_item_not_existing(self):
        """ Testing get_users with an item that does not exist """
        self.assertIsNone(get_comment(id=-11))

    def test_get_item(self):
        """ Testing if output is instance of the User class """
        result = get_comment(id=1)
        self.assertIsInstance(result, Comment)


if __name__ == '__main__':
    unittest.main()
