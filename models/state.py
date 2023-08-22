#!/usr/bin/python3
"""Defines the state class"""


from models.base_model import BaseModel


class State(BaseModel):
    """this is the user's state
    Attribute:
        name: the name of the state
        """

    name = ""
