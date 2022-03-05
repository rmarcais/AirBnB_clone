#!/usr/bin/python3
"""base_model.py
This module provides a class named BaseModel.
import models
import uuid
from datetime import datetime


class BaseModel:
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
        datetime
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        Returns a dictionary containing all keys/values of
        __dict__ of the instance
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    our code insert here
    """
    def __init__(self, *args, **kwargs):
        """
        constructor of base Model
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    dataTime = "%Y-%m-%dT %H:%M:%S.%f"
                    val = datetime.strptime(kwargs[key], dataTime)
                if key != '__class__':
                    setattr(self, key, val)

    def __str__(self):
        """
        method for named
        """
        nameClass = self.__class__.__name__
        return ("[{}] ({}) {}".format(nameClass, self.id, self.__dict__))

    def save(self):
        """
        method for save stuff
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        method for create a dict
        """
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        formatTime = "%Y-%m-%dT %H:%M:%S.%f"
        new_dict["created_at"] = self.created_at.strftime(formatTime)
        new_dict["updated_at"] = self.updated_at.strftime(formatTime)
        return new_dict
