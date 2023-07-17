#!/usr/bin/python3
"""Tests the BaseModel class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


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

    # Task 4 - kwargs argument
    def test_kwargs_empty(self):
        """Test that the base attributes are created when kwargs is empty.

        'id' and 'created_at' attributes are created."""

        self.assertTrue(hasattr(self.base1, 'id'))
        self.assertTrue(hasattr(self.base1, 'created_at'))
        self.assertTrue(hasattr(self.base1, 'updated_at'))

    def test_kwargs_not_empty(self):
        """Test that attributes are created using all the keys from kwargs

        This allows a new instance to be created using a previous instance's
        attributes.

        __class__ should not be one of these attributes and
        'created_at' and 'updated_at' should be datetime objects."""

        self.json_dict = {
                'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                'created_at': '2017-09-28T21:03:54.052298',
                'updated_at': '2017-09-28T21:03:54.052302',
                'name': 'My_First_Model',
                '__class__': 'BaseModel'}
        self.new_base = BaseModel(**self.json_dict)

        # check that attributes were created from all the keys
        self.assertFalse('__class__' in self.new_base.__dict__)
        for key in self.json_dict.keys():
            if key == '__class__':
                continue
            self.assertTrue(hasattr(self.new_base, key))

        # check for datetime objects
        self.assertEqual(type(self.new_base.created_at), datetime)
        self.assertEqual(type(self.new_base.updated_at), datetime)


if __name__ == "__main__":
    unittest.main()
