# pylint: disable=R0801, C0103
"""
    Tests for functional tests for user endpoints.
"""
import unittest
from fastapi.testclient import TestClient
from tests.DbTestCase import DbTestTestCase

from main import app
class UsersTestCase(DbTestTestCase):
    """
        Tests for functional tests for address endpoints.
    """

    def setUp(self):
        """ setup test environment. """
        self.client = TestClient(app)
        super().setUp()

    def test_address_get_item_not_existing(self):
        """ Test GET request to /addresses/{id} with invalid id. """
        response = self.client.get("/addresses/-1")
        self.assertEqual(404, response.status_code)

    def test_company_get_item(self):
        """ Test GET request to /addresses/{id} with valid id. """
        response = self.client.get("/addresses/1")
        self.assertEqual(200, response.status_code)

        address = response.json()
        self.assertEqual(1, address.get('id'))
        self.assertEqual(1, address.get('geo').get('id'))


if __name__ == '__main__':
    unittest.main()
