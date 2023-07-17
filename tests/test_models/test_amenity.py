#!/usr/bin/python3
"""Unittests for the City class."""
import unittest
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime


class TestState(unittest.TestCase):
    """Unittests for Amenity class."""

    def setUp(self):
        """Initialise variables for the unittests to use."""

        self.amenity = Amenity()

    def test_instance_of(self):
        """Test that object is instance of class amenity and parent BaseModel."""

        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity, BaseModel)

    def test_public_attribute_access(self):
        """Test that the public class attributes can be accessed."""

        self.assertEqual(self.amenity.name, '')

    def test_inherited_attribute_access(self):
        """Test that the inherited instance attributes can be accessed."""

        self.assertIs(type(self.amenity.id), str)
        self.assertIs(type(self.amenity.created_at), datetime)
        self.assertIs(type(self.amenity.updated_at), datetime)

    def test_save_method_inheritance(self):
        """This inherited method should update updated_at with current datetime."""

        previous_date = self.amenity.updated_at
        amenity_key = f'{self.amenity.__class__.__name__}.{self.amenity.id}'
        del models.storage._FileStorage__objects[amenity_key]

        self.amenity.save()
        self.assertNotEqual(self.amenity.updated_at, previous_date)

    def test_to_dict_method_inheritance(self):
        """Should return the dictionary representation of the object.

        The dictionary contains the key/values of __dict__ of the object.
        Among these a key called __class__ is set to identify the class
        of the object when it will be turned into an object again.

        The created_at and updated_at attributes will be converted to str
        objects in the iso format: %Y-%m-%dT%H:%M:%S.%f"""

        self.assertIs(type(self.amenity.created_at), datetime)  # confirm datetime obj
        self.assertIs(type(self.amenity.updated_at), datetime)

        amenity_dict = self.amenity.to_dict()
        # self.assertEqual(amenity_dict, self.amenity.__dict__)
        self.assertIs(type(amenity_dict['created_at']), str)  # confirm str obj
        self.assertIs(type(amenity_dict['updated_at']), str)
