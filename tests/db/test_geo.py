"""
    Testing functional tests for db geo
"""
import unittest
from tests.DbTestCase import DbTestTestCase
from src.db.geo import get_geo
from src.Model import Geo


class AddressDbTestCase(DbTestTestCase):
    """ Testing class for db geo """

    def test_get_item_not_existing(self):
        """ Testing get_geo with an item that does not exist """
        self.assertIsNone(get_geo(id=-11))

    def test_get_item(self):
        """ Testing if output is instance of the Geo class """
        result = get_geo(id=1)
        self.assertIsInstance(result, Geo)


if __name__ == '__main__':
    unittest.main()
