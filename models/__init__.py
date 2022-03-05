#!/usr/bin/python3
"""This module creates a unique FileStorage instance for your application.
"""


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


storage = FileStorage()
storage.reload()
