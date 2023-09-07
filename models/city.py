#!/usr/bin/python3
"""Defines fthe city class"""

<<<<<<< HEAD
from models import storage_type
from models.base_model import BaseModel
from sqlalchemy import Clolumn, String, ForeignKey
from sqlalchemy.orm import relationship

=======

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models.state import State
from sqlalchemy.orm import relationship


>>>>>>> de054e02cca2f4bcb0a7185a2468a28c1f596336
class City(BaseModel, Base):
    """This is the city of the user
    Attributes:
        state_id: the state id
        name: the name of the state
    """
<<<<<<< HEAD
    __tablename__ = 'cities'

    if storage_type = 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), nullable=False, ForeignKey('state.id'))
        places = relationship('Place', backref='cities', cascade='all, delete')

    else:
        name = ""
        state_id = ""
=======
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    # places = relationship("Place", cascade="all, delete", backref="cities")
>>>>>>> de054e02cca2f4bcb0a7185a2468a28c1f596336
