#!/usr/bin/python3
"""Defines the state class"""


from models.base_model import BaseModel
from sqlalchemy import Column, String

class State(BaseModel):
    """this is the user's state
    Attribute:
        name: the name of the state
        """
    __tabelname__ = 'states'

    if storage_type = 'db':

        name = Column(String(128), nullable=False)

    else:

        name = ""
