#!/usr/bin/python3
"""Module that contains the class FileStorage"""

import json
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
                        self.classes()[file_data[key]["__class__"]](**file_data[key])

    def classes(self):
        """Helper method to import other classes from the package"""

        from models.base_model import BaseModel
        from models.user import User
        classes = {"BaseModel": BaseModel,
                   "User": User}
        return classes
