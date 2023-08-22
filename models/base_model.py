#!/usr/bin/python3
"""creating base class"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base class that defines all common attributes"""
    def __init__(self, *args, **kwargs):
        """creating instances"""
        if kwargs:
            if 'id' not in kwargs.keys():
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs.keys():
                self.created_at = datetime.today()
            if 'updated_at' not in kwargs.keys():
                self.updated_at = datetime.today()

            style = "%Y-%m-%dT%H:%M:%S.%f"
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, style)
                if k != '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def __str__(self):
        """printable representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """update the date"""
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """convert object to dictionary"""
        dicts = self.__dict__.copy()
        dicts["__class__"] = self.__class__.__name__
        dicts["created_at"] = self.created_at.isoformat()
        dicts["updated_at"] = self.updated_at.isoformat()
        return dicts
