#!/usr/bin/python3
"""Test module for the class User"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """Tests the class User"""

    def test_is_subclass(self):
        """Tests if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_email(self):
        """Tests if attributes exist in User"""
        my_user = User()
        id = my_user.id
        self.assertTrue(hasattr(my_user, "email"))
        my_user.email = "airbnb@mail.com"
        my_user.save()
        my_user.reload()
        self.assertTrue(my_user in storage.all())
        self.assertTrue(my_user.email == "airbnb@mail.com")

    def test_password(self):
        """Tests if attributes exist in User"""
        my_user = User()
        self.assertTrue(hasattr(my_user, "password"))

    def test_first_name(self):
        """Tests if attributes exist in User"""
        my_user = User()
        self.assertTrue(hasattr(my_user, "first_name"))

    def test_last_name(self):
        """Tests if attributes exist in User"""
        my_user = User()
        self.assertTrue(hasattr(my_user, "last_name"))


if __name__ == '__main__':
    unittest.main()
