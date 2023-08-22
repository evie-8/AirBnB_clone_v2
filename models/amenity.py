#!/usr/bin/python3
"""Defines the amenity class"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """This is the amenity of the user
    Attribute:
        name: the name of the amenity
    """
    name = ""
