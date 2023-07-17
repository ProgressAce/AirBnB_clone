#!/usr/bin/python3
"""Unittests for the State class."""
import unittest
import models
from models.state import State
from models.base_model import BaseModel
from datetime import datetime


class TestState(unittest.TestCase):
    """Unittests for State class."""

    def setUp(self):
        """Initialise variables for the unittests to use."""

        self.state = State()

    def test_instance_of(self):
        """Test that object is instance of class State and parent BaseModel."""

        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state, BaseModel)

    def test_public_attribute_access(self):
        """Test that the public class attributes can be accessed."""

        self.assertEqual(self.state.name, '')

    def test_inherited_attribute_access(self):
        """Test that the inherited instance attributes can be accessed."""

        self.assertIs(type(self.state.id), str)
        self.assertIs(type(self.state.created_at), datetime)
        self.assertIs(type(self.state.updated_at), datetime)

    def test_save_method_inheritance(self):
        """This inherited method should update updated_at with current datetime."""

        previous_date = self.state.updated_at
        state_key = f'{self.state.__class__.__name__}.{self.state.id}'
        del models.storage._FileStorage__objects[state_key]

        self.state.save()  # test save method
        self.assertNotEqual(self.state.updated_at, previous_date)

    def test_to_dict_method_inheritance(self):
        """Should return the dictionary representation of the object.

        The dictionary contains the key/values of __dict__ of the object.
        Among these a key called __class__ is set to identify the class
        of the object when it will be turned into an object again.

        The created_at and updated_at attributes will be converted to str
        objects in the iso format: %Y-%m-%dT%H:%M:%S.%f"""

        self.assertIs(type(self.state.created_at), datetime)  # confirm datetime obj
        self.assertIs(type(self.state.updated_at), datetime)

        state_dict = self.state.to_dict()
        # self.assertEqual(state_dict, self.state.__dict__)
        self.assertIs(type(state_dict['created_at']), str)  # confirm str obj
        self.assertIs(type(state_dict['updated_at']), str)
