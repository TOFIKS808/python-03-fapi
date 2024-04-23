"""
    Testing functional tests for db address
"""
import unittest
from tests.DbTestCase import DbTestTestCase
from src.db.company import get_company
from src.Model import Company


class AddressDbTestCase(DbTestTestCase):
    """ Testing class for db company """

    def test_get_item_not_existing(self):
        """ Testing get_company with an item that does not exist """
        self.assertIsNone(get_company(id=-11))

    def test_get_item(self):
        """ Testing if output is instance of the Company class """
        result = get_company(id=1)
        self.assertIsInstance(result, Company)


if __name__ == '__main__':
    unittest.main()
