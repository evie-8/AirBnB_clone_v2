#!/usr/bin/python3
"""Unittest module for the State Class."""


import unittest
from datetime import datetime
import time
from models.state import State
import re
import pep8
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class Test_state_instances(unittest.TestCase):
    """the test case for state class"""

    def test_no_args(self):
        """tests for class type"""
        self.assertEqual(State, type(State()))

    def test_conatins_all_instances(self):
        """tests for instance"""
        s = State()
        self.assertEqual(str(type(s)), "<class 'models.state.State'>")
        self.assertIsInstance(s, State)
        self.assertTrue(issubclass(type(s), BaseModel))

    def test_two_states_unique_ids(self):
        """tests for ids"""
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.id, s2.id)

    def test_name(self):
        """test for name attribute"""
        self.assertEqual(str, type(State().name))

    def test_str(self):
        """checking output for __str__"""
        b_1 = State()
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
        base_4 = BaseModel()
        old = base_4.updated_at
        base_4.save()
        new = base_4.updated_at
        self.assertLess(old, new)

    def test_save2(self):
        """test when none is passed"""
        base_5 = State()
        with self.assertRaises(TypeError):
            base_5.save(None)

    def test_save3(self):
        """test if instance is actually stored"""
        b_2 = State()
        b_2.save()
        b_id = "State." + b_2.id
        with open("tests.json", "r") as f:
            self.assertIn(b_id, f.read())


class TestState_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the State class."""

    def test_to_dict_contains_correct_keys(self):
        """tests for dicts"""
        s = State()
        self.assertIn("id", s.to_dict())
        self.assertIn("created_at", s.to_dict())
        self.assertIn("updated_at", s.to_dict())
        self.assertIn("__class__", s.to_dict())

    def test_pep8_base(self):
        """check if class conforms pep8 quidelines"""
        style_pep = pep8.StyleGuide()
        file_result = style_pep.check_files(['models/state.py'])
        errs = file_result.get_statistics('E')
        error_messages = [f'{error[0]}:{error[1]}: {error[2]}'
                          for error in errs]


if __name__ == "__main__":
    unittest.main()
