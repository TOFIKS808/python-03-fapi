# pylint: disable=R0801,C0103
"""
    Tests for functional tests for user endpoints.
"""
import unittest
from fastapi.testclient import TestClient
from tests.DbTestCase import DbTestTestCase

from main import app


class UsersTestCase(DbTestTestCase):
    """
        Tests for functional tests for user endpoints.
    """

    def setUp(self):
        """ setup test environment. """
        self.client = TestClient(app)
        super().setUp()

    def test_users_get_item_not_existing(self):
        """ Test GET request to /users/{id} with invalid id. """
        response = self.client.get("/users/-1")
        self.assertEqual(404, response.status_code)

    def test_users_get_item(self):
        """ Test GET request to /users/{id} with valid id. """
        response = self.client.get("/users/1")
        self.assertEqual(200, response.status_code)

        user = response.json()
        self.assertEqual(1, user.get('id'))
        self.assertEqual(1, user.get('company').get('id'))
        self.assertEqual(1, user.get('address').get('id'))


if __name__ == '__main__':
    unittest.main()
