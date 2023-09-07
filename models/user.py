#!/usr/bin/python3
""" Defines the user class"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationships
from models import storage_type

class User(BaseModel, Base):
    """This represents the user
    Attributes:
        email: the email of the user
        password: the password of the use
        first_name: the user's first name
        last_name: the user's last name
        """
    __tablename__ = 'users'
    if storage_type == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nuallble=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship('Place', backref='user', cascade='all, delete')
        reviews = relationship('Review', backref='user', cascade='all, delete')

    else:

        email = ""
        password = ""
        first_name = ""
        last_name = ""
