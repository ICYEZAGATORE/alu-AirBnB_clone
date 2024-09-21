#!/usr/bin/python3
""" Defines the state class that inherits from BaseModel This class represents a state in the system """

from models.base_model import BaseModel

class State(BaseModel):
    """ Represents a state in the system """
    
    #public attribute default is an empty string
    
    name = ""
