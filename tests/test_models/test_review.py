#!/usr/bin/python3
"""This module provides tests for the class Review"""


from models.base_model import BaseModel
from models.review import Review
import unittest
import datetime
import models
import os


class TestReview(unittest.TestCase):
    """Test the User class"""
    dico = models.storage.all().copy()
    for k, v in dico.items():
        del models.storage.all()[k]
    models.storage.save()

    def test_review_id(self):
        """Test the type of the id"""
        var = Review()
        self.assertIsInstance(var.id, str)

    def test_review_created_at(self):
        """Test the type of created_at"""
        var = Review()
        self.assertIsInstance(var.created_at, datetime.datetime)

    def test_review_updated_at(self):
        """Test the type of updated_at"""
        var = Review()
        self.assertIsInstance(var.updated_at, datetime.datetime)

    def test_base_case(self):
        """Base cases: instantiation of the class User"""
        u1 = Review()
        self.assertEqual(type(u1), Review)

    def test_review_place_id(self):
        """Test the type of place_id"""
        var = Review()
        self.assertIsInstance(var.place_id, str)

    def test_review_user_id(self):
        """Test the type of user_id"""
        var = Review()
        self.assertIsInstance(var.user_id, str)

    def test_review_text(self):
        """Test the type of text"""
        var = Review()
        self.assertIsInstance(var.text, str)


class TestIsSubclass(unittest.TestCase):
    """This class tests if Review is a subclass of BaseModel"""
    dico = models.storage.all().copy()
    for k, v in dico.items():
        del models.storage.all()[k]
    models.storage.save()

    def test_is_subclass(self):
        """Test if Review is a subclass of BaseModel"""
        self.assertEqual(issubclass(Review, BaseModel), True)


class TestAttributes(unittest.TestCase):
    """This class does some tests with User's attributes"""
    dico = models.storage.all().copy()
    for k, v in dico.items():
        del models.storage.all()[k]
    models.storage.save()

    def test_add_attr(self):
        """Test adding a new attribute"""
        u1 = Review()
        u1.eye_color = "green"
        dico_review = u1.to_dict()
        u1.save()
        self.assertEqual(u1.eye_color, "green")
        self.assertIsInstance(u1, Review)
        self.assertEqual(type(dico_review), dict)

    def test_update_add(self):
        """Test updating attributes"""
        u2 = Review()
        u2.place_id = "John"
        u2.user_id = "Smith"
        self.assertEqual(u2.place_id, "John")
        self.assertEqual(u2.user_id, "Smith")
        self.assertIsInstance(u2, Review)
        u3 = Review()
        self.assertLess(u2.created_at, u3.created_at)
        self.assertLess(u2.updated_at, u3.updated_at)


if __name__ == '__main__':
    unittest.main()
