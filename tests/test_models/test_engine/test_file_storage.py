#!/usr/bin/python3
"""Test module for the class FileStorage"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models import storage
from os.path import exists
import json


class TestFileStorage(unittest.TestCase):
    """Tests the class FileStorage"""

    __file_path = 'file.json'

    def test_all(self):
        """Tests if all() returns a dictionary"""

        storage = FileStorage()
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        """Tests if new() updates the private dictionary __objects
           accessed with all() with a created BaseModel instance
        """

        storage = FileStorage()
        my_model = BaseModel()
        objects = storage.all()
        self.assertTrue(my_model in objects.values())

    def test_save(self):
        """Tests if save() creates a JSON file if it doesn't exist"""

        storage = FileStorage()
        storage.save()
        self.assertTrue(exists(TestFileStorage.__file_path))

    def test_reload(self):
        """Tests if the created JSON file is updated each time save()
           is called and that reload() loads in the previouly created
           objects stored in the JSON file
        """

        storage = FileStorage()
        storage.save()
        with open(TestFileStorage.__file_path, 'r') as file_1:
            file_data_1 = json.load(file_1)
        my_model_1 = BaseModel()
        storage.save()
        with open(TestFileStorage.__file_path, 'r') as file_2:
            file_data_2 = json.load(file_2)
        self.assertNotEqual(file_data_1, file_data_2)

        all_1 = storage.all()
        storage.reload()
        all_2 = storage.all()
        self.assertEqual(all_1, all_2)

    def test___file_path(self):
        self.assertTrue(exists(TestFileStorage.__file_path))

    def test___objects(self):
        storage = FileStorage()
        self.assertTrue(storage.all())

    def test_attr(self):
        """Tests if attributes exist in User"""
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        self.assertTrue(hasattr(my_user, "email"))
        self.assertTrue(hasattr(my_user, "password"))
        self.assertTrue(hasattr(my_user, "first_name"))
        self.assertTrue(hasattr(my_user, "last_name"))
        my_user.save()
        storage.reload()
        with open(TestFileStorage.__file_path, 'r') as file:
            file_data = json.load(file)
        self.assertTrue(my_user.to_dict() in file_data.values())
        self.assertTrue(my_user.first_name == "Betty")
        self.assertTrue(my_user.last_name == "Bar")
        self.assertTrue(my_user.email == "airbnb@mail.com")
        self.assertTrue(my_user.password == "root")

if __name__ == '__main__':
    unittest.main()
