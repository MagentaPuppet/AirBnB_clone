#!/usr/bin/python3
"""Module that contains the class FileStorage"""

import datetime
import json
import os
from os.path import exists


class FileStorage:
    """Serializes instances to a JSON file and
       deserializes JSON file to instances
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """Sets in the dictionary __objects the argument obj
           with key <obj class name>.id
        """

        FileStorage.__objects["{}.{}".format(
            type(obj).__name__, str(obj.id))] = obj

    def save(self):
        """Serializes the dictionary __objects to the
           JSON file(path: __file_path)
        """

        file_data = {}
        for key in FileStorage.__objects:
            file_data[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(file_data, file)

    def reload(self):
        """Deserializes the JSON file to the dictionary __objects
           (only if the JSON file (__file_path) exists); otherwise, do nothing.
        """

        if exists(FileStorage.__file_path):
            self.classes()
            with open(FileStorage.__file_path, 'r') as file:
                file_data = json.load(file)
                for key in file_data:
                    FileStorage.__objects[key] =\
                        self.classes()[file_data[key]["__class__"]](
                            **file_data[key])

    def classes(self):
        """Helper method to import other classes from the package"""

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        return classes

    def attributes(self):
        """Returns the valid attributes and their types for classname."""
        attributes = {
            "BaseModel": {
                "id": str,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime
                },
            "User": {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str
                },
            "State": {"name": str},
            "City":{"state_id": str, "name": str},
            "Amenity": {"name": str},
            "Place": {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list
                },
            "Review": {
                "place_id": str,
                "user_id": str,
                "text": str
                }
        }
        return attributes
