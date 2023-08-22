#!/usr/bin/python3
"""tests for file storage module"""


import os
import unittest
import json
import pep8
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from datetime import datetime
from models import storage


class TestFileStorage(unittest.TestCase):
    """tests from class FileStorage"""

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

    def test_pep8_filestorages(self):
        """check if class conforms pep8 quidelines"""
        style_pep = pep8.StyleGuide()
        file_result = style_pep.check_files(['models/engine/file_storage.py'])
        errs = file_result.get_statistics('E')
        error_messages = [f'{error[0]}:{error[1]}: {error[2]}'
                          for error in errs]
        self.assertEqual(errs, [], f'errors: \n{chr(10).join(error_messages)}')

    def test_filepath(self):
        """test type"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_object(self):
        """test type of object"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_instance(self):
        """test for instance type"""
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_wrong(self):
        """pass wrong type"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage(self):
        """test if its an instance of filestorage"""
        self.assertIsInstance(storage, FileStorage)

    def test_new_attr(self):
        """tests where new has arguments"""
        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 1)

    # testing new function

    def test_new(self):
        """testing for if instances are added"""
        base = BaseModel()
        user = User()
        amenity = Amenity()
        review = Review()
        state = State()
        place = Place()
        city = City()

        storage.new(base)
        storage.new(city)
        storage.new(amenity)
        storage.new(review)
        storage.new(user)
        storage.new(state)
        storage.new(place)

        self.assertIn("BaseModel." + base.id, storage.all().keys())
        self.assertIn(base, storage.all().values())
        self.assertIn("User." + user.id, storage.all().keys())
        self.assertIn(user, storage.all().values())
        self.assertIn("City." + city.id, storage.all().keys())
        self.assertIn(city, storage.all().values())
        self.assertIn("Amenity." + amenity.id, storage.all().keys())
        self.assertIn(amenity, storage.all().values())
        self.assertIn("Review." + review.id, storage.all().keys())
        self.assertIn("State." + state.id, storage.all().keys())
        self.assertIn(state, storage.all().values())
        self.assertIn("Place." + place.id, storage.all().keys())
        self.assertIn(place, storage.all().values())
        self.assertIn(review, storage.all().values())

    def test_new_None(self):
        """passing none as argument"""
        with self.assertRaises(AttributeError):
            storage.new(None)

    # tests for all function

    def test_all(self):
        """type of return type ofr storage.all"""
        self.assertEqual(dict, type(storage.all()))

    def test_all_none(self):
        """passing none"""
        with self.assertRaises(TypeError):
            storage.all(None)

    # tests for save function

    def test_save_none(self):
        """passing none to save function"""
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_save(self):
        """tests for save file"""
        base = BaseModel()
        user = User()
        amenity = Amenity()
        review = Review()
        state = State()
        place = Place()
        city = City()

        storage.new(base)
        storage.new(user)
        storage.new(state)
        storage.new(place)
        storage.new(city)
        storage.new(amenity)
        storage.new(review)
        storage.save()

        texts = ""
        with open("tests.json", "r") as files:
            texts = files.read()
            self.assertIn("BaseModel." + base.id, texts)
            self.assertIn("Amenity." + amenity.id, texts)
            self.assertIn("Review." + review.id, texts)
            self.assertIn("User." + user.id, texts)
            self.assertIn("State." + state.id, texts)
            self.assertIn("Place." + place.id, texts)
            self.assertIn("City." + city.id, texts)

    # tests for reload function

    def test_reload(self):
        """tests for how relaod function works"""
        base = BaseModel()
        user = User()
        amenity = Amenity()
        review = Review()
        state = State()
        place = Place()
        city = City()

        storage.new(base)
        storage.new(user)
        storage.new(state)
        storage.new(place)
        storage.new(city)
        storage.new(amenity)
        storage.new(review)
        storage.save()

        FileStorage._FileStorage__objects = {}
        storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base.id, objs)
        self.assertIn("User." + user.id, objs)
        self.assertIn("State." + state.id, objs)
        self.assertIn("Place." + place.id, objs)
        self.assertIn("City." + city.id, objs)
        self.assertIn("Amenity." + amenity.id, objs)
        self.assertIn("Review." + review.id, objs)

    def test_reload_none(self):
        """none is passed"""
        with self.assertRaises(TypeError):
            storage.reload(None)
