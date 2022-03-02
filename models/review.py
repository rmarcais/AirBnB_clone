#!/usr/bin/python3
"""review.py
This module defines the class Review.
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines the review"""
    place_id = ""
    user_id = ""
    text = ""
