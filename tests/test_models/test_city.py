#!/usr/bin/python3
"""This module provides tests for the class City"""


from models.base_model import BaseModel
from models.city import City
import unittest
import datetime
import models
import os


class TestCity(unittest.TestCase):
    """Test the City class"""
    dico = models.storage.all().copy()
    for k, v in dico.items():
        del models.storage.all()[k]
    models.storage.save()

    def test_city_id(self):
        """Test the id attribute of the class"""
        var = City()
        self.assertIsInstance(var.id, str)

    def test_city_created_at(self):
        """Test the created_at attribute of the class"""
        var = City()
        self.assertIsInstance(var.created_at, datetime.datetime)

    def test_city_updated_at(self):
        """Test the updated_at attribute of the class"""
        var = City()
        self.assertIsInstance(var.updated_at, datetime.datetime)

    def test_base_case(self):
        """Base cases: instantiation of the class"""
        u1 = City()
        self.assertEqual(type(u1), City)

    def test_city_name(self):
        """Test the name attribute of the class"""
        var = City()
        self.assertIsInstance(var.name, str)

    def test_city_state_id(self):
        """Test the state_id attribute of the class"""
        var = City()
        self.assertIsInstance(var.state_id, str)


class TestIsSubclass(unittest.TestCase):
    """This class tests if City is a subclass of BaseModel"""
    dico = models.storage.all().copy()
    for k, v in dico.items():
        del models.storage.all()[k]
    models.storage.save()

    def test_is_subclass(self):
        """Test if City is a subclass of BaseModel"""
        self.assertEqual(issubclass(City, BaseModel), True)


class TestAttributes(unittest.TestCase):
    """This class does some tests with City's attributes"""
    dico = models.storage.all().copy()
    for k, v in dico.items():
        del models.storage.all()[k]
    models.storage.save()

    def test_add_attr(self):
        """Test adding a new attribute"""
        u1 = City()
        u1.eye_color = "green"
        dico_city = u1.to_dict()
        u1.save()
        self.assertEqual(u1.eye_color, "green")
        self.assertIsInstance(u1, City)
        self.assertEqual(type(dico_city), dict)

    def test_update_add(self):
        """Test updating attributes"""
        u2 = City()
        u2.name = "John"
        u2.state_id = "Toulouse"
        self.assertEqual(u2.name, "John")
        self.assertEqual(u2.state_id, "Toulouse")
        self.assertIsInstance(u2, City)
        u3 = City()
        self.assertLess(u2.created_at, u3.created_at)
        self.assertLess(u2.updated_at, u3.updated_at)


if __name__ == '__main__':
    unittest.main()
