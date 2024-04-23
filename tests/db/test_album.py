"""
    Testing functional tests for db album
"""
import unittest
from tests.DbTestCase import DbTestTestCase
from src.db.album import get_album
from src.Model import Album


class AlbumDbTestCase(DbTestTestCase):
    """ Testing class for db album """

    def test_get_item_not_existing(self):
        """ Testing get_album with an item that does not exist """
        self.assertIsNone(get_album(id=-11))

    def test_get_item(self):
        """ Testing if output is instance of the Album class """
        result = get_album(id=1)
        self.assertIsInstance(result, Album)


if __name__ == '__main__':
    unittest.main()
