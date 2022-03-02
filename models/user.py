#!/usr/bin/python3
"""user.py
This module defines the class User.
"""


from models.base_model import BaseModel


class User(BaseModel):
    """This class defines the user's informations"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
