#!/usr/bin/python3
"""Unittests for the Review class."""
import unittest
import models
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime


class TestState(unittest.TestCase):
    """Unittests for Review class."""

    def setUp(self):
        """Initialise variables for the unittests to use."""

        self.review = Review()

    def test_instance_of(self):
        """Test that object is instance of class Review and parent BaseModel."""

        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review, BaseModel)

    def test_public_attribute_access(self):
        """Test that the public class attributes can be accessed."""

        self.assertEqual(self.review.place_id, '')
        self.assertEqual(self.review.user_id, '')
        self.assertEqual(self.review.text, '')

    def test_inherited_attribute_access(self):
        """Test that the inherited instance attributes can be accessed."""

        self.assertIs(type(self.review.id), str)
        self.assertIs(type(self.review.created_at), datetime)
        self.assertIs(type(self.review.updated_at), datetime)

    def test_save_method_inheritance(self):
        """This inherited method should update updated_at with current datetime."""

        previous_date = self.review.updated_at
        review_key = f'{self.review.__class__.__name__}.{self.review.id}'
        del models.storage._FileStorage__objects[review_key]

        self.review.save()
        self.assertNotEqual(self.review.updated_at, previous_date)

    def test_to_dict_method_inheritance(self):
        """Should return the dictionary representation of the object.

        The dictionary contains the key/values of __dict__ of the object.
        Among these a key called __class__ is set to identify the class
        of the object when it will be turned into an object again.

        The created_at and updated_at attributes will be converted to str
        objects in the iso format: %Y-%m-%dT%H:%M:%S.%f"""

        self.assertIs(type(self.review.created_at), datetime)  # confirm datetime obj
        self.assertIs(type(self.review.updated_at), datetime)

        review_dict = self.review.to_dict()
        # self.assertEqual(review_dict, self.review.__dict__)
        self.assertIs(type(review_dict['created_at']), str)  # confirm str obj
        self.assertIs(type(review_dict['updated_at']), str)
