#!/usr/bin/python3
"""Unittests for the User class."""
import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Unittests for the User class."""

    def setUp(self):
        """Initialise test variables for all the unittests."""

        self.user = User()

    def test_instance(self):
        """Test if object is instance of User and and its parent BaseModel."""

        self.assertTrue(isinstance(self.user, User))
        self.assertTrue(isinstance(self.user, BaseModel))

    def test_access_public_attributes(self):
        """Tests that public class attributes can be accessed."""

        self.assertEqual(self.user.email, '')
        self.assertEqual(self.user.password, '')
        self.assertEqual(self.user.first_name, '')
        self.assertEqual(self.user.last_name, '')

    def test_access_inherited_attributes(self):
        """Test the access to the inherited attributes from BaseModel."""

        self.assertIs(type(self.user.id), str)
        self.assertIs(type(self.user.created_at), datetime)
        self.assertIs(type(self.user.updated_at), datetime)

    def test_save_method_inheritance(self):
        """This inherited method should update updated_at with current datetime."""

        previous_date = self.user.updated_at
        self.user.save()
        self.assertNotEqual(self.user.updated_at, previous_date)

    def test_to_dict_method_inheritance(self):
        """Should return the dictionary representation of the object.

        The dictionary contains the key/values of __dict__ of the object.
        Among these a key called __class__ is set to identify the class
        of the object when it will be turned into an object again.

        The created_at and updated_at attributes will be converted to str
        objects in the iso format: %Y-%m-%dT%H:%M:%S.%f"""

        self.assertIs(type(self.user.created_at), datetime)  # confirm datetime obj
        self.assertIs(type(self.user.updated_at), datetime)

        user_dict = self.user.to_dict()
        # self.assertEqual(user_dict, self.user.__dict__)
        self.assertIs(type(user_dict['created_at']), str)  # confirm str obj
        self.assertIs(type(user_dict['updated_at']), str)
