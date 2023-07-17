#!/usr/bin/python3
"""Defines a class for Cities."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents the cities provided by the airbnb."""

    state_id = ''
    name = ''
