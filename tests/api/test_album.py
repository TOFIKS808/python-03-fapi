# pylint: disable=R0801
"""
    Tests for functional tests for album endpoints.
"""
import unittest
from fastapi.testclient import TestClient
from tests.DbTestCase import DbTestTestCase

from main import app


class CompaniesTestCase(DbTestTestCase):
    """
        Tests for functional tests for album endpoints.
    """

    def setUp(self):
        """ setup test environment. """
        self.client = TestClient(app)
        super().setUp()

    def test_company_get_item_not_existing(self):
        """ Test GET request to /albums/{id} with invalid id. """
        response = self.client.get("/albums/-1")
        self.assertEqual(404, response.status_code)

    def test_company_get_item(self):
        """ Test GET request to /albums/{id} with valid id. """
        response = self.client.get("/albums/1")
        self.assertEqual(200, response.status_code)

        album = response.json()
        self.assertEqual(1, album.get('id'))


if __name__ == '__main__':
    unittest.main()
