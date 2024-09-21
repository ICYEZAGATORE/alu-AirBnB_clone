#!/usr/bin/python3
""" Defines the class Review that inherits from BaseModel """

from models.base_model import BaseModel

class Review(BaseModel):
    """ represents a review for a place in the system """
    
    place_id = ""
    user_id = ""
    text = ""
