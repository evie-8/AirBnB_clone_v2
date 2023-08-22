#!/usr/bin/python3
"""Defines the place class"""


from models.base_model import BaseModel


class Place(BaseModel):
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
