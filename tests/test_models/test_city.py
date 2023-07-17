#!/usr/bin/python3
"""Unittests for the City class."""
import unittest
import models
from models.city import City
from models.base_model import BaseModel
from datetime import datetime


class TestState(unittest.TestCase):
    """Unittests for City class."""

    def setUp(self):
        """Initialise variables for the unittests to use."""

        self.city = City()

    def test_instance_of(self):
        """Test that object is instance of class City and parent BaseModel."""

        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)

    def test_public_attribute_access(self):
        """Test that the public class attributes can be accessed."""

        self.assertEqual(self.city.state_id, '')
        self.assertEqual(self.city.name, '')

    def test_inherited_attribute_access(self):
        """Test that the inherited instance attributes can be accessed."""

        self.assertIs(type(self.city.id), str)
        self.assertIs(type(self.city.created_at), datetime)
        self.assertIs(type(self.city.updated_at), datetime)

    def test_save_method_inheritance(self):
        """This inherited method should update updated_at with current datetime."""

        previous_date = self.city.updated_at
        city_key = f'{self.city.__class__.__name__}.{self.city.id}'
        del models.storage._FileStorage__objects[city_key]

        self.city.save()
        self.assertNotEqual(self.city.updated_at, previous_date)

    def test_to_dict_method_inheritance(self):
        """Should return the dictionary representation of the object.

        The dictionary contains the key/values of __dict__ of the object.
        Among these a key called __class__ is set to identify the class
        of the object when it will be turned into an object again.

        The created_at and updated_at attributes will be converted to str
        objects in the iso format: %Y-%m-%dT%H:%M:%S.%f"""

        self.assertIs(type(self.city.created_at), datetime)  # confirm datetime obj
        self.assertIs(type(self.city.updated_at), datetime)

        city_dict = self.city.to_dict()
        # self.assertEqual(city_dict, self.city.__dict__)
        self.assertIs(type(city_dict['created_at']), str)  # confirm str obj
        self.assertIs(type(city_dict['updated_at']), str)
