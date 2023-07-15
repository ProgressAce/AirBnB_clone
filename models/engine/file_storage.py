#!/usr/bin/python3
"""Defines a class for storing objects to a json file."""
from models.base_model import BaseModel
import json
import os


class FileStorage:
    """Representation of storing objects to a file and receiving it.

    Uses json serialisation and deserialisation.
    Args:
        __file_path(str): path to the json file.
        __objects(dict): stores objects, by <class name>.id, eg.BaseModel.1122
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns __objects - a dictionary of objects."""

        return self.__objects

    def new(self, obj):
        """Adds a new object to __objects.

        Uses <class name>.id as the key of the object.
        Any object with an if attribute will not raise an exception."""

        if not isinstance(obj, BaseModel):
            raise AttributeError
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """Serialises all the objects from __objects into a json file.

        Converts the objects in __objects to a dictionary
        and then serialises it before putting it into the json file."""

        with open(self.__file_path, 'w') as js_f:
            json_dict = {}

            # convert to serializable dictionary
            for key, value in self.__objects.items():
                json_dict[key] = value.to_dict()

            json.dump(json_dict, js_f)

    def reload(self):
        """Deserialises json file to python dict containing custom objects.

        The file is only serialised if: it exists and is not empty."""

        path = self.__file_path

        if os.path.exists(path):  # and os.stat(path).st_size != 0:
            with open(path, 'r') as js_f:
                json_dict = json.load(js_f)  # dict containing json datatypes

                # convert the json_dict values back to BaseModel objects.
                for key, value in json_dict.items():
                    self.__objects[key] = BaseModel(**value)
        else:
            pass
