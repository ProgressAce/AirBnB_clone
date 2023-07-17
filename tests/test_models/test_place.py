#!/usr/bin/python3
"""Unittests for the City class."""
import unittest
import models
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime


class TestState(unittest.TestCase):
    """Unittests for Place class."""

    def setUp(self):
        """Initialise variables for the unittests to use."""

        self.place = Place()

    def test_instance_of(self):
        """Test that object is instance of class Place and parent BaseModel."""

        self.assertIsInstance(self.place, Place)
        self.assertIsInstance(self.place, BaseModel)

    def test_public_attribute_access(self):
        """Test that the public class attributes can be accessed."""

        self.assertEqual(self.place.city_id, '')
        self.assertEqual(self.place.user_id, '')
        self.assertEqual(self.place.name, '')
        self.assertEqual(self.place.description, '')
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_inherited_attribute_access(self):
        """Test that the inherited instance attributes can be accessed."""

        self.assertIs(type(self.place.id), str)
        self.assertIs(type(self.place.created_at), datetime)
        self.assertIs(type(self.place.updated_at), datetime)

    def test_save_method_inheritance(self):
        """This inherited method should update updated_at with current datetime."""

        previous_date = self.place.updated_at
        place_key = f'{self.place.__class__.__name__}.{self.place.id}'
        del models.storage._FileStorage__objects[place_key]

        self.place.save()
        self.assertNotEqual(self.place.updated_at, previous_date)

    def test_to_dict_method_inheritance(self):
        """Should return the dictionary representation of the object.

        The dictionary contains the key/values of __dict__ of the object.
        Among these a key called __class__ is set to identify the class
        of the object when it will be turned into an object again.

        The created_at and updated_at attributes will be converted to str
        objects in the iso format: %Y-%m-%dT%H:%M:%S.%f"""

        self.assertIs(type(self.place.created_at), datetime)  # confirm datetime obj
        self.assertIs(type(self.place.updated_at), datetime)

        place_dict = self.place.to_dict()
        # self.assertEqual(place_dict, self.place.__dict__)
        self.assertIs(type(place_dict['created_at']), str)  # confirm str obj
        self.assertIs(type(place_dict['updated_at']), str)
