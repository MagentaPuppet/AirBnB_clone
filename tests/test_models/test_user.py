#!/usr/bin/python3
"""Test module for the class User"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Tests the class User"""

    def test___str__(self):
        """Tests if __str__() returns a string in the correct format"""

        my_model = User()
        self.assertIsInstance(my_model.__str__(), str)
        self.assertEqual(my_model.__str__(), "[{}] ({}) {}".format(
                         type(my_model).__name__, my_model.id,
                         my_model.__dict__))

    def test_save(self):
        """Tests if save() updates the attribute created_at"""

        time_1 = datetime.now()
        my_model = User()
        time_2 = datetime.now()
        self.assertEqual(my_model.created_at, my_model.updated_at)
        self.assertGreaterEqual(my_model.updated_at, time_1)
        self.assertLessEqual(my_model.updated_at, time_2)
        my_model.save()
        time_3 = datetime.now()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)
        self.assertGreaterEqual(my_model.updated_at, time_2)
        self.assertLessEqual(my_model.updated_at, time_3)

    def test_to_dict(self):
        """Tests if to_dict() updates __dict__ for the instance -> Tests if:
         - a key __class__ is added which contains a string showing the class
           name
         - the instance attributes created_at and updated_at are converted
           to string objects in the ISO format
        """

        my_model = User()
        created_at = my_model.created_at
        updated_at = my_model.updated_at
        dict = my_model.to_dict()
        self.assertEqual(dict['__class__'], str(type(my_model).__name__))
        self.assertEqual(type(dict['__class__']), str)
        self.assertEqual(type(dict['created_at']), str)
        self.assertEqual(type(dict['updated_at']), str)
        self.assertEqual(str(datetime.isoformat(created_at)),
                         dict['created_at'])
        self.assertEqual(str(datetime.isoformat(updated_at)),
                         dict['created_at'])

    def test_kwargs(self):
        """Tests if the attributes of my_model and my_new_model are the same
           and that the two instances are not the same object
        """

        my_model = User()
        my_new_model = User(**(my_model.to_dict()))
        self.assertEqual(my_model.__str__(), my_new_model.__str__())
        self.assertIsNot(my_model, my_new_model)

    def test_is_subclass(self):
        """Tests if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_email(self):
        """Tests if attributes exist in User"""
        my_user = User()
        self.assertTrue(hasattr(my_user, "email"))

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
