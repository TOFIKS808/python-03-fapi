"""
    Tests for `dummy` package
"""
import unittest
from src.dummy import returns


class TestDummy(unittest.TestCase):
    """dummy test case"""

    def test_returns(self):
        """testing returns"""
        self.assertEqual(1, returns(1))
        self.assertEqual("string", returns("string"))
