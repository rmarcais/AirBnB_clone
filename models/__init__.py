#!/usr/bin/python3
"""This module creates a unique FileStorage instance for your application.



from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


storage = FileStorage()
storage.reload()
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

storage = FileStorage()
storage.reload()
