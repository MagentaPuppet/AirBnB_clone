#!/usr/bin/python3
"""Module for class User"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class that creates users"""

    place_id = ""
    user_id = ""
    text = ""
