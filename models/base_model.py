#!/usr/bin/python3
"""Defines BaseModel class which acts as a base for other classes.
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """
    BaseModel defines all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a BaseModel object.

        kwargs is used to define new attributes for an instance.
        When kwargs is empty, the base attributes will be defined.
        Args:
            *args: will not be used.
            **kwargs: dictionary for defining new attributes.
        """

        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            # new instances are stored to storage in memory
        else:
            print(kwargs)
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
            print(self.__class__.__name__)

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                self.__dict__))

    def save(self):
        """Updates the updated_at attribute with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary of all keys/values of __dict__ of the instance

        a key __class__ is added to this dictionary with the
        class name of the object.

        created_at and updated_at are converted to string object in ISO format:
        format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
        """

        new_dict = {key: self.__dict__[key] for key in self.__dict__}
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
