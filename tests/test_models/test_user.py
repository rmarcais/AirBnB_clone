#!/usr/bin/python3
"""This module provides tests for the class User"""


from models.base_model import BaseModel
from models.user import User
import unittest
import datetime
import models
import os


class TestUser(unittest.TestCase):
    """Test the User class"""
    dico = models.storage.all().copy()
    for k, v in dico.items():
        del models.storage.all()[k]
    models.storage.save()

    def test_user_id(self):
        """Test the type of id"""
        var = User()
        self.assertIsInstance(var.id, str)

    def test_user_created_at(self):
        """Test the type of created_at"""
        var = User()
        self.assertIsInstance(var.created_at, datetime.datetime)

    def test_user_updated_at(self):
        """Test the type of updated_at"""
        var = User()
        self.assertIsInstance(var.updated_at, datetime.datetime)

    def test_base_case(self):
        """Base cases: instantiation of the class User"""
        u1 = User()
        self.assertEqual(type(u1), User)

    def test_user_email(self):
        """Test the type of email"""
        var = User()
        self.assertIsInstance(var.email, str)

    def test_user_passwd(self):
        """Test the type of password"""
        var = User()
        self.assertIsInstance(var.password, str)

    def test_user_first_name(self):
        """Test the type of first_name"""
        var = User()
        self.assertIsInstance(var.first_name, str)

    def test_user_last_name(self):
        """Test the type of last_name"""
        var = User()
        self.assertIsInstance(var.last_name, str)


class TestIsSubclass(unittest.TestCase):
    """This class tests if User is a subclass of BaseModel"""
    dico = models.storage.all().copy()
    for k, v in dico.items():
        del models.storage.all()[k]
    models.storage.save()

    def test_is_subclass(self):
        """Test if User is a subclass of BaseModel"""
        self.assertEqual(issubclass(User, BaseModel), True)


class TestAttributes(unittest.TestCase):
    """This class does some tests with User's attributes"""
    dico = models.storage.all().copy()
    for k, v in dico.items():
        del models.storage.all()[k]
    models.storage.save()

    def test_add_attr(self):
        """Test adding a new attribute"""
        u1 = User()
        u1.eye_color = "green"
        dico_user = u1.to_dict()
        u1.save()
        self.assertEqual(u1.eye_color, "green")
        self.assertIsInstance(u1, User)
        self.assertEqual(type(dico_user), dict)

    def test_update_add(self):
        """Test updating attributes"""
        u2 = User()
        u2.first_name = "John"
        u2.last_name = "Smith"
        self.assertEqual(u2.first_name, "John")
        self.assertEqual(u2.last_name, "Smith")
        self.assertIsInstance(u2, User)
        u3 = User()
        self.assertLess(u2.created_at, u3.created_at)
        self.assertLess(u2.updated_at, u3.updated_at)


if __name__ == '__main__':
    unittest.main()
