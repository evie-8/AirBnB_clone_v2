#!/usr/bin/python3
"""Unittest module for the Amenity Class."""


import unittest
import pep8
from datetime import datetime
from models.amenity import Amenity
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class Test_amenity_instances(unittest.TestCase):

    """ Unittest for testing the amnenity class"""

    def test_no_args(self):
        """tests for class type"""
        self.assertEqual(Amenity, type(Amenity()))

    def test_id(self):
        """tests for id type"""
        self.assertEqual(str, type(Amenity().id))

    def test_two_amenities_unique_ids(self):
        """tests for unique ids"""
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.id, a2.id)

    def test_name_attr(self):
        """test fro name attribute"""
        self.assertEqual(str, type(Amenity().name))

    def test_str(self):
        """checking output for __str__"""
        b_1 = Amenity()
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
        base_4 = Amenity()
        old = base_4.updated_at
        base_4.save()
        new = base_4.updated_at
        self.assertLess(old, new)

    def test_save2(self):
        """test when none is passed"""
        base_5 = Amenity()
        with self.assertRaises(TypeError):
            base_5.save(None)

    def test_save3(self):
        """test if instance is actually stored"""
        b_2 = Amenity()
        b_2.save()
        b_id = "Amenity." + b_2.id
        with open("tests.json", "r") as f:
            self.assertIn(b_id, f.read())


class Test_amenity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_name_attribute(self):
        """tests for name attribute"""
        a = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", a.__dict__)

    def test_pep8_base(self):
        """check if class conforms pep8 quidelines"""
        style_pep = pep8.StyleGuide()
        file_result = style_pep.check_files(['model/amenity.py'])
        errs = file_result.get_statistics('E')
        error_messages = [f'{error[0]}:{error[1]}: {error[2]}'
                          for error in errs]


if __name__ == "__main__":
    unittest.main()
