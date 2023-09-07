#!/usr/bin/python3
"""Defines the place class"""


from models.base_model import BaseModel
from models import storage_type
from sqlalchemy import Column, String, Float, ForeignKey, Integer
from models import storage_type

class Place(BaseModel, Base):
    """this is the place of the user
    Attributes:
        city_id: the city id
        user_id: the user id
        name: the name of the city/place
        description: describes the place
        number_room: the number of the room
        number_bathrrom: thew number of bathrooms
        max_guest: the maximum number of guests
        price_by_night: price per night
        latitude: the location
        longitude: the location
        amenity_ids: the id of the amenity
    """
    __tablename__ = 'places'

    if storage_type = 'db':
        city_id = Column(String(60), nullable=False, ForeignKey(cities.id))
        user_id = Column(String(60), nullable=False, ForeignKey(users.id))
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number-rooms = Column(Integer, nullable=False,default=0)
        number_bathrooms = Column(Integer, nuallble=False, default=0)
        max_guest = Column(Integer, nullable=False, defualt=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, defualt=0)
        longitude = Column(Float, default=0)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
