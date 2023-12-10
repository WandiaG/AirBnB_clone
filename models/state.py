#!/usr/bin/python3
"""Defines a class State that inherits properties of  BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        """Creates new instances of State.
        """
        super().__init__(*args, **kwargs)
