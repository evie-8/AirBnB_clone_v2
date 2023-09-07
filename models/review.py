#!/usr/bin/python3
"""Defines the review class"""


from models.base_model import BaseModel, Base
from slqalchemy import Column, String, ForeignKey


class Review(BaseModel):
    """This is a review
    Attributes:
        place_id: the place id
        user_id: the user's id
        text: the textfield for review
    """
    __tablename__ = 'reviews'

    if storrage_type = 'db':
        test = Column(String(1024), nullable=False)
        place_id = Column(String(60), nullable=False, ForeignKey='places.id')
        user_id = Column(String(60), nullable=False, ForeignKey='users.id')

    else:
        place_id = ""
        user_id = ""
        text = ""
