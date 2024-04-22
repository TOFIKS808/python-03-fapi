"""
    Testing functional tests for db users
"""
import unittest
from src.db.users import get_user
from src.db.lib import get_db_url_test
from src.Model import User


class UsersDbTestCase(unittest.TestCase):
    """ Testing class for db users """

    def test_get_item_not_existing(self):
        """ Testing get_users with an item that does not exist """
        self.assertIsNone(get_user(id=-11, url=get_db_url_test()))

    def test_get_item(self):
        """ Testing if output is instance of the User class """
        result = get_user(id=1, url=get_db_url_test())
        self.assertIsInstance(result, User)


if __name__ == '__main__':
    unittest.main()
