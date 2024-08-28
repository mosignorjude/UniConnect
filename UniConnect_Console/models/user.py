#!/usr/bin/python3
"""
Defines the user class.
Inherits from BaseModel class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user in Uniconnect
    """
    user_id = ""
    first_name = ""
    last_name = ""
    email = ""
    password = ""

    def __init__(self, *args, **kwargs):
        """
        user class constructor.
        Arguments:
            args: Non keyworded arguments.
            kwargs: keyworded arguments.
        """
        super().__init__(*args, **kwargs)
