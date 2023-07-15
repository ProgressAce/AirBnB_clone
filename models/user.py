#!/usr/bin/python3
"""Defines a class for a User."""
from models.base_model import BaseModel
import models
import uuid



class User(BaseModel):
    """Represents a User."""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
