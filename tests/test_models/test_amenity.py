#!/usr/bin/python3
"""This module provides tests for the class User"""


from models.base_model import BaseModel
from models.amenity import Amenity
import unittest
import datetime
import models
import os


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""
    dico = models.storage.all().copy()
    for k, v in dico.items():
        del models.storage.all()[k]
    models.storage.save()

    def test_amenity_id(self):
        """Test the tpe of id"""
        var = Amenity()
        self.assertIsInstance(var.id, str)

    def test_amenity_created_at(self):
        """Test the type of created_at"""
        var = Amenity()
        self.assertIsInstance(var.created_at, datetime.datetime)

    def test_amenity_updated_at(self):
        """Test the type of updated_at"""
        var = Amenity()
        self.assertIsInstance(var.updated_at, datetime.datetime)

    def test_base_case(self):
        """Base cases: instantiation of the class Amenity"""
        u1 = Amenity()
        self.assertEqual(type(u1), Amenity)

    def test_amenity_name(self):
        """Test the type of name"""
        var = Amenity()
        self.assertIsInstance(var.name, str)


class TestIsSubclass(unittest.TestCase):
    """This class tests if Amenity is a subclass of BaseModel"""
    dico = models.storage.all().copy()
    for k, v in dico.items():
        del models.storage.all()[k]
    models.storage.save()

    def test_is_subclass(self):
        """Test if User is a subclass of BaseModel"""
        self.assertEqual(issubclass(Amenity, BaseModel), True)


class TestAttributes(unittest.TestCase):
    """This class does some tests with User's attributes"""
    dico = models.storage.all().copy()
    for k, v in dico.items():
        del models.storage.all()[k]
    models.storage.save()

    def test_add_attr(self):
        """Test adding a new attribute"""
        u1 = Amenity()
        u1.color = "green"
        dico_amenity = u1.to_dict()
        u1.save()
        self.assertEqual(u1.color, "green")
        self.assertIsInstance(u1, Amenity)
        self.assertEqual(type(dico_amenity), dict)

    def test_update_add(self):
        """Test updating attributes"""
        u2 = Amenity()
        u2.name = "Paris"
        self.assertEqual(u2.name, "Paris")
        self.assertIsInstance(u2, Amenity)
        u3 = Amenity()
        self.assertLess(u2.created_at, u3.created_at)
        self.assertLess(u2.updated_at, u3.updated_at)


if __name__ == '__main__':
    unittest.main()
