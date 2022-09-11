#!/usr/bin/python3
"""Module that defines the BaseModel class"""

from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """Class that defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs) -> None:
        """Init method"""

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key != '__class__':
                    if key in ["created_at", "updated_at"]:
                        self.__dict__[key] = datetime.strptime(
                            kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")

                    else:
                        self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self) -> None:
        """Returns a human readable representation of an instance"""

        return "[{}] ({}) {}".format(
           type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at
           with the current datetime
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
           of __dict__ of the instance
        """

        dict = self.__dict__.copy()
        dict['created_at'] = datetime.isoformat(dict['created_at'])
        dict['updated_at'] = datetime.isoformat(dict['updated_at'])
        dict['__class__'] = type(self).__name__
        return dict
