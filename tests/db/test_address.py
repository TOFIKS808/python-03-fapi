"""
    Testing functional tests for db address
"""
import unittest
from tests.DbTestCase import DbTestTestCase
from src.db.address import get_address
from src.Model import Address


class AddressDbTestCase(DbTestTestCase):
    """ Testing class for db address """

    def test_get_item_not_existing(self):
        """ Testing get_address with an item that does not exist """
        self.assertIsNone(get_address(id=-11))

    def test_get_item(self):
        """ Testing if output is instance of the Address class """
        result = get_address(id=1)
        self.assertIsInstance(result, Address)


if __name__ == '__main__':
    unittest.main()
