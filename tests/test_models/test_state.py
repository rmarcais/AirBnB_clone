#!/usr/bin/python3
"""This module provides tests for the class State"""


from models.base_model import BaseModel
from models.state import State
import unittest
import datetime
import models
import os


class TestState(unittest.TestCase):
    """Test the State class"""
    dico = models.storage.all().copy()
    for k, v in dico.items():
        del models.storage.all()[k]
    models.storage.save()

    def test_state_id(self):
        """Test the type of id"""
        var = State()
        self.assertIsInstance(var.id, str)

    def test_state_created_at(self):
        """Test the type of created_at"""
        var = State()
        self.assertIsInstance(var.created_at, datetime.datetime)

    def test_state_updated_at(self):
        """Test the type of updated_at"""
        var = State()
        self.assertIsInstance(var.updated_at, datetime.datetime)

    def test_base_case(self):
        """Base cases: instantiation of the class State"""
        u1 = State()
        self.assertEqual(type(u1), State)

    def test_state_name(self):
        """Test the type of name"""
        var = State()
        self.assertIsInstance(var.name, str)


class TestIsSubclass(unittest.TestCase):
    """This class tests if User is a subclass of BaseModel"""
    dico = models.storage.all().copy()
    for k, v in dico.items():
        del models.storage.all()[k]
    models.storage.save()

    def test_is_subclass(self):
        """Test if State is a subclass of BaseModel"""
        self.assertEqual(issubclass(State, BaseModel), True)


class TestAttributes(unittest.TestCase):
    """This class does some tests with State's attributes"""
    dico = models.storage.all().copy()
    for k, v in dico.items():
        del models.storage.all()[k]
    models.storage.save()

    def test_add_attr(self):
        """Test adding a new attribute"""
        u1 = State()
        u1.color = "green"
        dico_state = u1.to_dict()
        u1.save()
        self.assertEqual(u1.color, "green")
        self.assertIsInstance(u1, State)
        self.assertEqual(type(dico_state), dict)

    def test_update_add(self):
        """Test updating attributes"""
        u2 = State()
        u2.name = "Paris"
        self.assertEqual(u2.name, "Paris")
        self.assertIsInstance(u2, State)
        u3 = State()
        self.assertLess(u2.created_at, u3.created_at)
        self.assertLess(u2.updated_at, u3.updated_at)


if __name__ == '__main__':
    unittest.main()
