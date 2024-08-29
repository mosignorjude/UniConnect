#!/usr/bin/python3
"""
Defines the lecturer class.
Inherits from BaseModel class.
"""
from models.base_model import BaseModel


class Lecturer(BaseModel):
    """
    Represents a lecturer in Uniconnect
    """
    user_id = ""
    department = ""
    program = ""
    contact = ""
    rank = ""

    def __init__(self, *args, **kwargs):
        """
        lecturer class constructor.
        Arguments:
            args: Non keyworded arguments.
            kwargs: keyworded arguments.
        """
        super().__init__(*args, **kwargs)
