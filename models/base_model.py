#!/usr/bin/python3
"""Module that defines the BaseModel class"""

from datetime import datetime
import uuid


class BaseModel:
    def __init__(self) -> None:
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self) -> None:
        return "[{}] ({}) {}".format(
           type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict = self.__dict__
        dict.update(
            {'created_at': str(datetime.isoformat(dict['created_at'])),
             'updated_at': str(datetime.isoformat(dict['updated_at'])),
             '__class__': type(self).__name__})
        return dict
