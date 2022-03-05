#!/usr/bin/python3
"""
This module contains unit tests for the class FileStorage.
"""


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from datetime import datetime
import unittest
import models
import json
import uuid
import os


class TestAllMethod(unittest.TestCase):
    """
    This class provides tests for the all method.
    """
    def test_instance_filestorage(self):
        """Test create a FileStorage instance"""
        f1 = FileStorage()
        self.assertEqual(type(f1), FileStorage)

    def test_type_return_value(self):
        """Test the type of the return value"""
        self.assertEqual(type(models.storage.all()), dict)

    def tests_none_objects(self):
        """Test all without objects"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        self.assertEqual(models.storage.all(), {})

    def tests_one_objects(self):
        """Test with one object"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        b1 = BaseModel()
        b1.save()
        self.assertEqual(len(models.storage.all()), 1)

    def tests_more_than_one_objects(self):
        """Test with more than one object"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        b2 = BaseModel()
        b3 = BaseModel()
        b2.save()
        b3.save()
        self.assertEqual(len(models.storage.all()), 2)

    def tests_all_types(self):
        """Test with all types of class"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        b1 = BaseModel()
        b1.save()
        u1 = User()
        u1.save()
        p1 = Place()
        p1.save()
        r1 = Review()
        r1.save()
        c1 = City()
        c1.save()
        a1 = Amenity()
        a1.save()
        s1 = State()
        s1.save()
        self.assertEqual(len(models.storage.all()), 7)


class TestNewMethod(unittest.TestCase):
    """Class that tests the new method"""

    def test_new_all_classes(self):
        """Test the new method with all types of class
        (The new method called when we create a new instance)"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        b1 = BaseModel()
        b1.save()
        u1 = User()
        u1.save()
        p1 = Place()
        p1.save()
        r1 = Review()
        r1.save()
        c1 = City()
        c1.save()
        a1 = Amenity()
        a1.save()
        s1 = State()
        s1.save()
        self.assertEqual(len(models.storage.all()), 7)

    def test_key(self):
        """Test the value of the key when the new method is called"""
        """Test with all types of class"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        b1 = BaseModel()
        b1.save()
        dico = models.storage.all()
        self.assertEqual(type(dico["BaseModel." + str(b1.id)]), type(b1))


class TestSaveMethod(unittest.TestCase):
    """Class that tests the save method"""

    def test_jsonfile_creation(self):
        """Test if the json file has been created"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        os.remove("file.json")
        self.assertEqual(os.path.exists("file.json"), False)
        b1 = BaseModel()
        b1.save()
        self.assertEqual(os.path.exists("file.json"), True)

    def test_if_jsonfile_is_filled(self):
        """Test if the save method fills the json file"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        self.assertEqual(os.path.getsize("file.json"), 2)
        s1 = State()
        s1.save()
        self.assertGreater(os.path.getsize("file.json"), 2)

    def test_save_after_sel(self):
        """Test if the save method fills the json file"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        u1 = User()
        p1 = Place()
        u1.save()
        p1.save()
        self.assertGreater(os.path.getsize("file.json"), 2)
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        self.assertEqual(os.path.getsize("file.json"), 2)


class TestReloadMethod(unittest.TestCase):
    """Class that tests the reload method"""

    def test_reload_type(self):
        """Test the reload method"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        u1 = User()
        u1.save()
        models.storage.reload()
        dico = models.storage.all()
        for k, v in dico.items():
            self.assertEqual(type(dico[k]), type(u1))


if __name__ == '__main__':
    unittest.main()
