#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
"""Tests the BaseModel class"""


class TestBaseModel(unittest.TestCase):
    """Unittest class for BaseModel"""

    def setUp(self):
        """SetUp for this tests"""
        self.model = BaseModel()

    def test_isinstance(self):
        """Test instace of BaseModel"""
        self.assertIsInstance(self.model, BaseModel)

    def test_attribute(self):
        """Test instance attributes"""
        with self.assertRaises(AttributeError):
            self.model.gg


if __name__ == "__main__":
    unittest.main()
