#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
"""Tests the BaseModel class"""


class TestBaseModel(unittest.TestCase):
    """Unittest class for BaseModel"""

    def setUp(self):
        """SetUp at the start of each test"""
        self.base1 = BaseModel()
        self.base2 = BaseModel()
        # self.base1.id = "base1"
        # self.base2.id = "base2"

    def test_isinstance(self):
        """Test instace of BaseModel"""
        self.assertIsInstance(self.base1, BaseModel)

    def test_id(self):
        """Test the id instance attributes"""
        self.assertIn("id", self.base1.__dict__)
        self.assertIs(type(self.base1.id), str)
        self.assertNotEqual(self.base1.id, self.base2.id)

    def test_created_at(self):
        """Test the created_at instance attributes"""
        self.assertIn("created_at", self.base1.__dict__)
        self.assertIs(type(self.base1.created_at), datetime)

    def test_updated_at(self):
        """Test the updated_at instance attributes"""
        self.assertIn("updated_at", self.base1.__dict__)
        self.assertIs(type(self.base1.updated_at), datetime)

    def test_save_method(self):
        """Test that the method updates the created_at attribute"""
        up1 = self.base2.updated_at
        self.base2.save()
        up2 = self.base2.updated_at
        self.assertNotEqual(up1, up2)

    def test_to_dict_method(self):
        """Test that the to_dict method returns a dictionary
            that has all the required key value pairs"""
        dict1 = self.base2.to_dict()
        self.assertEqual(dict1["__class__"], "BaseModel")
        self.assertIs(type(dict1["created_at"]), str)
        self.assertIs(type(dict1["updated_at"]), str)


if __name__ == "__main__":
    unittest.main()
