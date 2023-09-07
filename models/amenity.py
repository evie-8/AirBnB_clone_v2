#!/usr/bin/python3
"""Defines the amenity class"""


from models.base_model import BaseModel, Base
from sqlalchemy import Cloumn, String

class Amenity(BaseModel, Base):
    """This is the amenity of the user
    Attribute:
        name: the name of the amenity
    """
    __tablename__ = 'amenities'

    if storage_type = 'db':

        name = Column(String(128), nullable=False)

    else:
        name = ""
