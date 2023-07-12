#!/usr/bin/python3
import uuid
from datetime import datetime
"""BaseModel
Class definition for BaseModel
"""


class BaseModel():
    """BaseModel class

    BaseModel defines all common attributes/methods for other classes
    """

    def __init__(self):
        """Initializes a BaseModel object
        """
        self.id = str(uuid.uuid4())
        """str: Unique id for each BaseModel"""
        self.created_at = datetime.now()
        """datetime: Current datetime when an instance is created"""
        self.updated_at = self.created_at
        """datetime: Current datetime when an instance is created,
        updated everytime the object is changed
        """

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                self.__dict__))

    def save(self):
        """Updates the updated_at attribute with the current datetime
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary of all keys/values of __dict__ of the instance

        a key __class__ is added to this dictionary with the
        class name of the object

        created_at and updated_at are converted to string object in ISO format:
        format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259
        """

        new_dict = {key: self.__dict__[key] for key in self.__dict__}
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict


if __name__ == "__main__":
    b1 = BaseModel()
    print(b1)
