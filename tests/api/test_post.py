# pylint: disable=R0801,C0103
"""
    Tests for functional tests for posts endpoints.
"""
import unittest
from fastapi.testclient import TestClient
from tests.DbTestCase import DbTestTestCase

from main import app


class PostTestCase(DbTestTestCase):
    """
        Tests for functional tests for posts endpoints.
    """

    def setUp(self):
        """ setup test environment. """
        self.client = TestClient(app)
        super().setUp()

    def test_post_get_item_not_existing(self):
        """ Test GET request to /posts/{id} with invalid id. """
        response = self.client.get("/posts/-1")
        self.assertEqual(404, response.status_code)

    def test_post_get_item(self):
        """ Test GET request to /posts/{id} with valid id. """
        response = self.client.get("/posts/1")
        self.assertEqual(200, response.status_code)

        post = response.json()
        self.assertEqual(1, post.get('id'))

    def test_post_delete_item(self):
        response = self.client.delete("/posts/1")
        print(response.status_code)
        response = self.client.delete("/posts/1")
        print(response.status_code)

if __name__ == '__main__':
    unittest.main()
