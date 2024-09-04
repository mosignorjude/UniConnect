#!/usr/bin/python3

from sqlalchemy import Column, String, DateTime, ForeignKey
from models.base_model import BaseModel

class Enrollment(BaseModel):
    """
    Represents an enrollment of a student in a course.

    Attributes:
        reg_no (str): The registration number of the student.
        course_id (str): The ID of the course.
        enrollment_date (DateTime): The date of enrollment.
    """
    __tablename__ = 'enrollment'
    reg_no = Column(String(20), ForeignKey('student.reg_no'))
    course_id = Column(String(36), ForeignKey('course.id'))
    enrollment_date = Column(DateTime)
