# pylint: disable=R0801, C0103

"""
    Tests for functional tests for todo endpoints.
"""
import unittest
from fastapi.testclient import TestClient
from tests.DbTestCase import DbTestTestCase

from main import app


class CompaniesTestCase(DbTestTestCase):
    """
        Tests for functional tests for todo endpoints.
    """

    def setUp(self):
        """ setup test environment. """
        self.client = TestClient(app)
        super().setUp()

    def test_photo_get_item_not_existing(self):
        """ Test GET request to /todos/{id} with invalid id. """
        response = self.client.get("/todos/-1")
        self.assertEqual(404, response.status_code)

    def test_photo_get_item(self):
        """ Test GET request to /todos/{id} with valid id. """
        response = self.client.get("/todos/1")
        self.assertEqual(200, response.status_code)

        photo = response.json()
        self.assertEqual(1, photo.get('id'))


if __name__ == '__main__':
    unittest.main()
