#!/usr/bin/python3
"""Defines the review class"""


from models.base_model import BaseModel


class Review(BaseModel):
    """This is a review
    Attributes:
        place_id: the place id
        user_id: the user's id
        text: the textfield for review
    """

    place_id = ""
    user_id = ""
    text = ""
