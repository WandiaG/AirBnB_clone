#!/usr/bin/python3
"""Defines a class Review  that inherits from BaseModel"""
from models.base_model import BaseModel


class Review (BaseModel):
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Creates new instances of Review.
        """
        super().__init__(*args, **kwargs)
