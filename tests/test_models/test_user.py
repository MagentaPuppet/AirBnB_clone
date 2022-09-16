#!/usr/bin/python3
"""Test module for the class User"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models import storage
import json


class TestUser(unittest.TestCase):
    """Tests the class User"""

    __file_path = "file.json"

    def test_is_subclass(self):
        """Tests if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

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
        with open(TestUser.__file_path, 'r') as file:
            file_data = json.load(file)
        self.assertTrue(my_user.to_dict() in file_data.values())
        self.assertTrue(my_user.first_name == "Betty")
        self.assertTrue(my_user.last_name == "Bar")
        self.assertTrue(my_user.email == "airbnb@mail.com")
        self.assertTrue(my_user.password == "root")


if __name__ == '__main__':
    unittest.main()
