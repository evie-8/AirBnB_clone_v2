#!/usr/bin/python3
"""Defines fthe city class"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models.state import State
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """This is the city of the user
    Attributes:
        state_id: the state id
        name: the name of the state
    """
    __tablename__ = 'cities'

    if storage_type = 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), nullable=False, ForeignKey('state.id'))
        places = relationship('Place', backref='cities', cascade='all, delete')

    else:
        name = ""
        state_id = ""
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    # places = relationship("Place", cascade="all, delete", backref="cities")
