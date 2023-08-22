#!/usr/bin/python3
"""Unittest module for the Place Class."""


import unittest
import pep8
from datetime import datetime
import time
from models.place import Place
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class Test_place_instance(unittest.TestCase):
    """Unittest for the place class"""

    def test_city_id_attribute(self):
        """test for city id"""
        p = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(p))
        self.assertNotIn("city_id", p.__dict__)

    def test_user_id_attribute(self):
        """tests for user id"""
        p = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(p))
        self.assertNotIn("user_id", p.__dict__)

    def test_name_attribute(self):
        """tests for name attribute"""
        p = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(p))
        self.assertNotIn("name", p.__dict__)

    def test_description_attribute(self):
        """tests for description attr"""
        p = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(p))
        self.assertNotIn("desctiption", p.__dict__)

    def test_number_rooms_attribute(self):
        """tests for rooms"""
        p = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(p))
        self.assertNotIn("number_rooms", p.__dict__)

    def test_number_bathrooms_attribute(self):
        """tests for bathrooms"""
        p = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(p))
        self.assertNotIn("number_bathrooms", p.__dict__)

    def test_max_guest_attribute(self):
        """test for guests"""
        p = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(p))
        self.assertNotIn("max_guest", p.__dict__)

    def test_price_by_night_attribute(self):
        """tests for price"""
        p = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(p))
        self.assertNotIn("price_by_night", p.__dict__)

    def test_latitude_attribute(self):
        """tests for latitude"""
        p = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(p))
        self.assertNotIn("latitude", p.__dict__)

    def test_longitude__attribute(self):
        """tests for longitude"""
        p = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(p))
        self.assertNotIn("longitude", p.__dict__)

    def test_amenity_ids_attribute(self):
        """tests for amenity"""
        p = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(p))
        self.assertNotIn("amenity_ids", p.__dict__)

    def test_two_places_unique_ids(self):
        """tests for ids"""
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.id, p2.id)

    def test_str(self):
        """checking output for __str__"""
        b_1 = Place()
        self.assertEqual(b_1.__str__(), "[" + b_1.__class__.__name__ + "]"
                         " (" + b_1.id + ") " + str(b_1.__dict__))


class TestBaseModelSave(unittest.TestCase):
    """test class for save method"""

    def setUp(self):
        """method run ofor each test in class"""
        with open("tests.json", 'w'):
            FileStorage._FileStorage__file_path = "tests.json"
            FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ destroys file for each test after running it"""
        FileStorage._FileStorage__file_path = "file.json"
        try:
            os.remove("tests.json")
        except FileNotFoundError:
            pass

    def test_save1(self):
        """checking if updated_at times are different"""
        base_4 = Place()
        old = base_4.updated_at
        base_4.save()
        new = base_4.updated_at
        self.assertLess(old, new)

    def test_save2(self):
        """test when none is passed"""
        base_5 = Place()
        with self.assertRaises(TypeError):
            base_5.save(None)

    def test_save3(self):
        """test if instance is actually stored"""
        b_2 = Place()
        b_2.save()
        b_id = "Place." + b_2.id
        with open("tests.json", "r") as f:
            self.assertIn(b_id, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_to_dict_contains_correct_keys(self):
        """tests for dicts"""
        p = Place()
        self.assertIn("id", p.to_dict())
        self.assertIn("created_at", p.to_dict())
        self.assertIn("updated_at", p.to_dict())
        self.assertIn("__class__", p.to_dict())

    def test_pep8_base(self):
        """check if class conforms pep8 quidelines"""
        style_pep = pep8.StyleGuide()
        file_result = style_pep.check_files(['models/place.py'])
        errs = file_result.get_statistics('E')
        error_messages = [f'{error[0]}:{error[1]}: {error[2]}'
                          for error in errs]


if __name__ == "__main__":
    unittest.main()
