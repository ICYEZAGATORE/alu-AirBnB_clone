#!/usr/bin/python3
""" This module defines the user class, which inherits from BaseModel """

from models.base_model import BaseModel

class User(BaseModel):
    """ user class that inherits from BaseModel. Represents a user in the 
        AirBnB   clone projects """
       
       # public class attributes
    email = ""
    password = ""
    first_name = ""
    last_name = ""     
