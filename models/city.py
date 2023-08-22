#!/usr/bin/python3
"""Defines fthe city class"""


from models.base_model import BaseModel


class City(BaseModel):
    """This is the city of the user
    Attributes:
        state_id: the state id
        name: the name of the state
    """
    name = ""
    state_id = ""
