#!/usr/bin/python3
"""
base_model.py
This module provides a class named BaseModel.
"""


import models
import uuid
from datetime import datetime


"""class BaseModel:
    This class defines all common attributes/methods for other classes.

    def __init__(self, *args, **kwargs):
        This method is called when a new instance is created.
        Args:
        *args: unused
        *kwargs: pairs of attributes\values
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self,
                                key, datetime.strptime(value,
                                                       "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        Returns the string representation of a BaseModel instance
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        Updates the public instance attribute updated_at with the current
        datetime.
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        Returns a dictionary containing all keys/values of
        __dict__ of the instance.
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
"""
class BaseModel:
    """
    This class defines all common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        This is the constructor method.
        """
        mod = '%Y-%m-%dT%H:%M:%S.%f'
        if len(args) == 0 and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        date_time_str = datetime.strptime(value, mod)
                        setattr(self, key, date_time_str)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        THis method return the good format.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        This method updates the public instance attribute 'updated_at' with
        the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        This method returns a dictionary containing all keys/values of __dict__
        of the instance.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
