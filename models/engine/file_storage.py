#!/usr/bin/python3
"""Defines the class FileStorage"""


import json


class FileStorage:
    """it is used as an abstract storage engine.
    Attributes:
    __file_path(str): name of the file to save the object to
    __objects: a dictonary
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary objects"""
        lists = ["BaseModel", "User", "State", "City",
                 "Amenity", "Place", "Review"]
        class_objects = {}
        if cls:
            if cls.__name__ in lists:
                for k, v in FileStorage.__objects.items():
                    key = k.split(".")[0]
                    if key == cls.__name__:
                        class_objects[k] = v
            return class_objects
        else:
            return self.__objects

    def new(self, obj):
        """sets in __objects obj with the key <obj_class_name>.id"""
        k = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                FileStorage._objects = {}
                for k, v in objdict.items():
                    cls_name = v["__class__"]
                    # del o["__class__"]
                    FileStorage.__objects[k] = eval(cls_name)(**v)
        except FileNotFoundError:
            return

    def delete(self, obj=None):
        """Delete object from __objects"""
        if obj:
            k = "{}.{}".format(type(obj).__name__, obj.id)
            del FileStorage.__objects[k]
