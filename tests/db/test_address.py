"""
    Testing functional tests for db address
"""
import unittest
from src.db.address import get_address
from src.db.lib import get_db_url_test
from src.Model import Address


class AddressDbTestCase(unittest.TestCase):
    """ Testing class for db address """

    def test_get_item_not_existing(self):
        """ Testing get_users with an item that does not exist """
        self.assertIsNone(get_address(id=-11, url=get_db_url_test()))

    def test_get_item(self):
        """ Testing if output is instance of the User class """
        result = get_address(id=1, url=get_db_url_test())
        self.assertIsInstance(result, Address)


if __name__ == '__main__':
    unittest.main()
