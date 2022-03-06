#!/usr/bin/python3
"""Tests for BaseModel"""
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModelInstantiation(unittest.TestCase):
    """test the instantiation"""

    def test_name_class(self):
        """test the class name"""
        bm = BaseModel()
        self.assertEqual(bm.__class__.__name__, "BaseModel")

    def test_bm_id_str(self):
        """test id str"""
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_bm_id_uuid(self):
        """test id uuid"""
        bm = BaseModel()
        self.assertIsInstance(uuid.UUID(bm.id), uuid.UUID)

    def test_bm_unique_id(self):
        """test unique id"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_len_id(self):
        """test the len of the id"""
        bm = BaseModel()
        self.assertEqual(len(bm.id), 36)

    def test_create_type_datetime(self):
        """test if created at"""
        bm = BaseModel()
        self.assertEqual(type(bm.created_at), datetime)

    def test_different_created(self):
        """test if created_at change each time executed"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.created_at, bm2.created_at)

    def test_update_type_datetime(self):
        """test the type of updated_at"""
        bm = BaseModel()
        self.assertEqual(type(bm.updated_at), datetime)

    def test_different_created_updated(self):
        """test if updated_at change each time executed"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.created_at, bm2.updated_at)

    def test_different_updated(self):
        """test if updated_at change each time executed"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.updated_at, bm2.updated_at)


class TestBaseModelStr(unittest.TestCase):
    """test the str method"""

    def test_representation_class_name_and_id(self):
        """test the str representation"""
        bm = BaseModel()
        bm.id = 230691
        self.assertTrue("[BaseModel] (230691)", bm.__str__)

    def test_representation_created_at(self):
        """test if created_at is True"""
        bm = BaseModel()
        self.assertTrue('created_at' in str(bm), True)

    def test_representation_updated_at(self):
        """test if update_at is True"""
        bm = BaseModel()
        self.assertTrue('updated_at' in str(bm), True)


class TestBaseModelSave(unittest.TestCase):
    """test the save method"""

    def test_name_base_model(self):
        """test the save method with name"""
        obj = BaseModel()
        obj.name = "Batman"
        obj.save()
        self.assertEqual(obj.name, "Batman")

    def test_my_number_base_model(self):
        """test the save method with number"""
        obj = BaseModel()
        obj.num = 2306
        obj.save()
        self.assertEqual(obj.num, 2306)

    def test_save_update(self):
        """test if changes of update are saved"""
        obj = BaseModel()
        obj.age = 38
        date1 = obj.updated_at
        obj.save()
        obj.age = 39
        date2 = obj.updated_at
        obj.save()
        self.assertNotEqual(date1, date2)


class TestBaseModelTodict(unittest.TestCase):
    """test the to_dict method"""

    def test_dictionary_return(self):
        """test the to_dict method"""
        bm = BaseModel()
        my_dict = bm.to_dict()
        self.assertEqual(type(my_dict), dict)

    def test_create_dictionary(self):
        """test if the function to_dict work"""
        bm = BaseModel()
        self.assertEqual(type(bm.__dict__), dict)

    def test_compare_dictionary_type(self):
        """test if our dictionary is same as the __dict__"""
        bm = BaseModel()
        self.assertEqual(type(bm.__dict__), type(bm.to_dict()))

    def test_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())


if __name__ == '__main__':
    unittest.main()
