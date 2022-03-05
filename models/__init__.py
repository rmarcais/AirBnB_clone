"""
This module creates a unique instance for the application

Import the class FilseStorage, create a variable storage and
use the method reload.
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
