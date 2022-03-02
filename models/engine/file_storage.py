#!/usr/bin/python3
"""file_storage.py
This module defines a class named FileStorage.
"""

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json


class FileStorage:
    """Class that serializes instances to a JSON file and deserializes
    JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionnary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj

    def save(self):
        """Method that serializes __objects to the JSON file."""
        dico = {}
        for k, v in FileStorage.__objects.items():
            dico[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dico, f)

    def reload(self):
        """Method that deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, "r") as f:
                dico2 = json.load(f)
                for k, v in dico2.items():
                    FileStorage.__objects[k] = eval(v['__class__'])(**v)
        except Exception:
            return
