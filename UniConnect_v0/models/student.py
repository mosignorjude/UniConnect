#!/usr/bin/python3
"""
Defines the student class.
Inherits from BaseModel class.
"""
from models.base_model import BaseModel


class Student(BaseModel):
    """
    Represents a student in Uniconnect
    """
    user_id = ""
    reg_no = ""
    program = ""
    level = ""
    cgpa = ""
    enrollment_date = ""

    def __init__(self, *args, **kwargs):
        """
        student class constructor.
        Arguments:
            args: Non keyworded arguments.
            kwargs: keyworded arguments.
        """
        super().__init__(*args, **kwargs)
