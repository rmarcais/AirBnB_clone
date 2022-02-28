#!/usr/bin/python3
"""base_model.py
This module provides a class neamed BaseModel.
"""


import uuid
from datetime import datetime
import time


class BaseModel:
    """This class defines all common attributes/methods for other classes."""

    def __init__(self):
        """This method is called when a new instance is created."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Tells the main program how to print the object."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at with the current
        datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
        __dict__ of the instance.
        """
        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
