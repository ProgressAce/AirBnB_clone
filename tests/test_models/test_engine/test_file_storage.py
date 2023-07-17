#!/usr/bin/python3
"""Unittests for FileStorage class."""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Unittest for the entire FileStorage class, used for string objects.
    """

    def setUp(self):
        """Set up code to use for the all the tests."""

        self.file_storage = FileStorage()

    def test_private_attribute_access(self):
        """Test that the private class attributes are not accessible."""

        with self.assertRaises(AttributeError):
            print(self.file_storage.__file_path)
            print(self.file_storage.__objects)

    def test_file_storage_instance(self):
        """Test if a created FileStorage instance is of type FileStorage."""

        self.assertIs(type(self.file_storage), FileStorage)

    def test_all_method(self):
        """Test that the all method returns a dictionary."""

        obj_dict = self.file_storage.all()
        self.assertIs(type(obj_dict), dict)

    def test_new_method_insertion(self):
        """Test that the new() adds one new object to __object."""

        obj_len = len(self.file_storage.all())  # returns objects in storage
        self.file_storage.new(BaseModel())
        self.assertEqual(len(self.file_storage.all()), obj_len + 1)

    def test_new_method_incorrect_arg_number(self):
        """Tests that the new_method only accepts one argument."""

        with self.assertRaises(TypeError):
            self.file_storage.new()
            self.file_storage.new(BaseModel(), BaseModel())

    def test_new_method_incorrect_arg_type(self):
        """Tests that new() only accepts arguments with id attribute."""

        with self.assertRaises(AttributeError):
            self.file_storage.new('object')
            self.file_storage.new(5)
            self.file_storage.new(2.55)
            self.file_storage.new(67j)
            self.file_storage.new({5: 'five'})
            self.file_storage.new({4, 7})
            self.file_storage.new([6, 8])
            self.file_storage.new((0, 1, 2))

    def test_new_method_accepted_args(self):
        """Tests that new() only accepts arguments of type BaseModel.

        This includes any custom classes that inherit from BaseModel.
        Otherwise a TypeError is raised."""

        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)
        self.file_storage.new(base_model)

        class Person(BaseModel):
            """Represents a person and there identification."""

            pass

        person = Person()
        self.file_storage.new(person)
        self.assertIsInstance(person, BaseModel)

        # delete person key from FileStorage's __objects.
        person_key = '{}.{}'.format(person.__class__.__name__, person.id)
        del self.file_storage._FileStorage__objects[person_key]

        self.assertFalse(isinstance(dict(), BaseModel))

    def test_save_method_file_not_found(self):
        """Test that save() continues to serialize even if file is not found.
        """
        pass

    def test_save_method_empty_objects(self):
        """Test that save() serializes even if __objects is found empty.
        """
        pass

    def test_reload_method_file_not_found(self):
        """Test that nothing happens, should the file not be found."""

        path = self.file_storage._FileStorage__file_path
        self.file_storage._FileStorage__file_path = ''  # ensure missing file
        self.file_storage.reload()
        self.file_storage._FileStorage__file_path = path

        # test for existing, but empty json file.
