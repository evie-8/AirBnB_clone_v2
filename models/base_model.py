#!/usr/bin/python3
"""creating base class"""


import uuid
from datetime import datetime
from models import storage
from sqlalchemy.ext.declarative import declarative_base
from model import storage_type

Base = declarative_base()

class BaseModel:
    """Base class that defines all common attributes"""

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)


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

    def delete(self):
        """elete the current instance from the storage """
        models.storage.delete(self)
