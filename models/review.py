#!/usr/bin/python3
"""Defines a class for Reviews."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents the reviews of the airbnb."""

    place_id = ''
    user_id = ''
    text = ''
