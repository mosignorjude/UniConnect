#!/usr/bin/python3
"""
Defines the enrollment class.
Inherits from BaseModel class.
"""
from models.base_model import BaseModel
import datetime


class Enrollment(BaseModel):
    """
    Represents an enrollment in Uniconnect
    """

    reg_no = 0  # ID of the Student
    course_id = ""   # ID of the Course
    enrollment_date = datetime.datetime.now()

    def __init__(self, *args, **kwargs):
        """
        enrollment class constructor.
        Arguments:
            args: Non keyworded arguments.
            kwargs: keyworded arguments.
        """
        super().__init__(*args, **kwargs)
