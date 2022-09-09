#!/usr/bin/python3
import unittest
from datetime import date, datetime
from xmlrpc.client import _iso8601_format
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_save(self):
        time_1 = datetime.now()
        my_model = BaseModel()
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
        my_model = BaseModel()
        created_at = my_model.created_at
        updated_at = my_model.updated_at
        dict = my_model.to_dict()
        self.assertEqual(len(dict), len(my_model.__dict__) + 1)
        self.assertEqual(dict['__class__'], str(type(my_model).__name__))
        self.assertEqual(type(dict['__class__']), str)
        self.assertEqual(type(dict['created_at']), str)
        self.assertEqual(type(dict['updated_at']), str)
        self.assertEqual(str(datetime.isoformat(created_at)),
                         dict['created_at'])
        self.assertEqual(str(datetime.isoformat(updated_at)),
                         dict['created_at'])


if __name__ == '__main__':
    unittest.main()
