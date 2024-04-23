"""
    Testing functional tests for db Photo
"""
import unittest
from tests.DbTestCase import DbTestTestCase
from src.db.photo import get_photo
from src.Model import Photo


class AddressDbTestCase(DbTestTestCase):
    """ Testing class for db photo """

    def test_get_item_not_existing(self):
        """ Testing get_photo with an item that does not exist """
        self.assertIsNone(get_photo(id=-11))

    def test_get_item(self):
        """ Testing if output is instance of the Photo class """
        result = get_photo(id=1)
        self.assertIsInstance(result, Photo)


if __name__ == '__main__':
    unittest.main()
