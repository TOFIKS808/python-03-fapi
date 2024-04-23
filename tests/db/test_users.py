"""
    Testing functional tests for db users
"""
import unittest
from src.db.users import get_user
from src.Model import User
from tests.DbTestCase import DbTestTestCase


class UsersDbTestCase(DbTestTestCase):
    """ Testing class for db users """

    def test_get_item_not_existing(self):
        """ Testing get_users with an item that does not exist """
        self.assertIsNone(get_user(id=-11))

    def test_get_item(self):
        """ Testing if output is instance of the User class """
        result = get_user(id=1)
        self.assertIsInstance(result, User)


if __name__ == '__main__':
    unittest.main()
