#!/usr/bin/python3
"""
Defines the courses class.
Inherits from BaseModel class.
"""
from models.base_model import BaseModel


class Course(BaseModel):
    """
    Represents a course in Uniconnect
    """
    course_code = ""
    course_name = ""
    description = ""
    lecturers = []  # List of Lecturer IDs

    def __init__(self, *args, **kwargs):
        """
        course class constructor.
        Arguments:
            args: Non keyworded arguments.
            kwargs: keyworded arguments.
        """
        super().__init__(*args, **kwargs)
