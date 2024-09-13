#!/usr/bin/python3
""" Defines the Place class that inherits from BaseModel """

from models.base_model import BaseModel

class Place(BaseModel):
    """ Represents an accomodation in the system """
    
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_of_rooms = 0
    number_of_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = [] #List of amenity ids, defult is set to an empty list
