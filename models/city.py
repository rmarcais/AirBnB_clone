#!/usr/bin/python3
"""city.py
This module defines the class City.
"""


from models.base_model import BaseModel


class City(BaseModel):
    """This class defines the name of the city"""
    state_id = ""
    name = ""
