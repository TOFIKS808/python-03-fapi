# pylint: disable=R0801,C0103
"""
    Tests for functional tests for comment endpoints.
"""
import unittest
from fastapi.testclient import TestClient
from tests.DbTestCase import DbTestTestCase

from main import app


class CommentTestCase(DbTestTestCase):
    """
        Tests for functional tests for comment endpoints.
    """

    def setUp(self):
        """ setup test environment. """
        self.client = TestClient(app)
        super().setUp()

    def test_comments_get_item_not_existing(self):
        """ Test GET request to /comments/{id} with invalid id. """
        response = self.client.get("/comments/-1")
        self.assertEqual(404, response.status_code)

    def test_comments_get_item(self):
        """ Test GET request to /comments/{id} with valid id. """
        response = self.client.get("/comments/1")
        self.assertEqual(200, response.status_code)

        comment = response.json()
        self.assertEqual(1, comment.get('id'))


if __name__ == '__main__':
    unittest.main()
