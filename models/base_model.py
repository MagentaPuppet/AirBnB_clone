#!/usr/bin/python3
"""Module that defines the BaseModel class"""

from datetime import datetime
import uuid


class BaseModel:
    """class that defines all common attributes/methods for other classes"""

    def __init__(self) -> None:
        """init method"""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self) -> None:
        """prints [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(
           type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at
           with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
           of __dict__ of the instance
        """
        dict = self.__dict__.copy()
        dict.update(
            {'created_at': str(datetime.isoformat(dict['created_at'])),
             'updated_at': str(datetime.isoformat(dict['updated_at'])),
             '__class__': type(self).__name__})
        return dict
