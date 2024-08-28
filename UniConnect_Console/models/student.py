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
    reg_no = 0
    program = ""
    faculty = ""
    department = ""
    level = 0
    cgpa = 0.0
    enrollment_date = ""
    courses = []  # list of courses id

    def __init__(self, *args, **kwargs):
        """
        student class constructor.
        Arguments:
            args: Non keyworded arguments.
            kwargs: keyworded arguments.
        """
        super().__init__(*args, **kwargs)
