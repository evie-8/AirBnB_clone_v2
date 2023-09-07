#!/usr/bin/python3
"""Defines the state class"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import os
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """this is the user's state
    Attribute:
        name: the name of the state
        """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state",
                          cascade="all, delete")

    if (os.environ.get("HBNB_TYPE_STORAGE") != 'db'):
        @property
        def cities(self):
            """getter method"""
            from models import storage
            from models.city import City
            lists = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    lists.append(city)
            return lists
