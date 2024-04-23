"""
    Testing functional tests for db todo
"""
import unittest
from tests.DbTestCase import DbTestTestCase
from src.db.todo import get_todo
from src.Model import Todo


class CommentDbTestCase(DbTestTestCase):
    """ Testing class for db todo """

    def test_get_item_not_existing(self):
        """ Testing get_todo with an item that does not exist """
        self.assertIsNone(get_todo(id=-11))

    def test_get_item(self):
        """ Testing if output is instance of the Todo class """
        result = get_todo(id=1)
        self.assertIsInstance(result, Todo)


if __name__ == '__main__':
    unittest.main()
