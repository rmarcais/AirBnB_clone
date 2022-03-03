#!/usr/bin/python3
"""This module provides tests for the class Place"""


from models.base_model import BaseModel
from models.place import Place
import unittest
import datetime
import models
import os


class TestPlace(unittest.TestCase):
    """Test the Place class"""
    dico = models.storage.all().copy()
    for k, v in dico.items():
        del models.storage.all()[k]
    models.storage.save()

    def test_place_id(self):
        """Test the id attribute of the class"""
        var = Place()
        self.assertIsInstance(var.id, str)

    def test_place_created_at(self):
        """Test the created_at attribute of the class"""
        var = Place()
        self.assertIsInstance(var.created_at, datetime.datetime)

    def test_place_updated_at(self):
        """Test the updated_at attribute of the class"""
        var = Place()
        self.assertIsInstance(var.updated_at, datetime.datetime)

    def test_base_case(self):
        """Base cases: instantiation of the class"""
        u1 = Place()
        self.assertEqual(type(u1), Place)

    def test_place_name(self):
        """Test the name attribute of the class"""
        var = Place()
        self.assertIsInstance(var.name, str)

    def test_city_id(self):
        """Test the city_id attribute of the class"""
        var = Place()
        self.assertIsInstance(var.city_id, str)

    def test_user_id(self):
        """Test the user_id attribute of the class"""
        var = Place()
        self.assertIsInstance(var.user_id, str)

    def test_description(self):
        """Test the description attribute of the class"""
        var = Place()
        self.assertIsInstance(var.description, str)

    def test_number_rooms(self):
        """Test the number_rooms attribute of the class"""
        var = Place()
        self.assertIsInstance(var.number_rooms, int)

    def test_number_bathrooms(self):
        """Test the number_bathrooms attribute of the class"""
        var = Place()
        self.assertIsInstance(var.number_bathrooms, int)

    def test_max_guest(self):
        """Test the max_guest attribute of the class"""
        var = Place()
        self.assertIsInstance(var.max_guest, int)

    def test_price_by_night(self):
        """Test the price_by_name attribute of the class"""
        var = Place()
        self.assertIsInstance(var.price_by_night, int)

    def test_longitude(self):
        """Test the longitude attribute of the class"""
        var = Place()
        self.assertIsInstance(var.longitude, float)

    def test_latitude(self):
        """Test the latitude attribute of the class"""
        var = Place()
        self.assertIsInstance(var.latitude, float)

    def test_amenity_ids(self):
        """Test the amenity_ids attribute of the class"""
        var = Place()
        self.assertIsInstance(var.amenity_ids, list)


class TestIsSubclass(unittest.TestCase):
    """This class tests if Place is a subclass of BaseModel"""
    dico = models.storage.all().copy()
    for k, v in dico.items():
        del models.storage.all()[k]
    models.storage.save()

    def test_is_subclass(self):
        """Test if Place is a subclass of BaseModel"""
        self.assertEqual(issubclass(Place, BaseModel), True)


class TestAttributes(unittest.TestCase):
    """This class does some tests with Place's attributes"""
    dico = models.storage.all().copy()
    for k, v in dico.items():
        del models.storage.all()[k]
    models.storage.save()

    def test_add_attr(self):
        """Test adding a new attribute"""
        u1 = Place()
        u1.color = "green"
        dico_place = u1.to_dict()
        u1.save()
        self.assertEqual(u1.color, "green")
        self.assertIsInstance(u1, Place)
        self.assertEqual(type(dico_place), dict)

    def test_update_add(self):
        """Test updating attributes"""
        u2 = Place()
        u2.name = "John"
        u2.city_id = "Toulouse"
        self.assertEqual(u2.name, "John")
        self.assertEqual(u2.city_id, "Toulouse")
        self.assertIsInstance(u2, Place)
        u3 = Place()
        self.assertLess(u2.created_at, u3.created_at)
        self.assertLess(u2.updated_at, u3.updated_at)


if __name__ == '__main__':
    unittest.main()
