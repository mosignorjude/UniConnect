#!/usr/bin/python3
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel

class CourseLecturers(BaseModel):
    """
    Represents the relationship between courses and lecturers.

    Attributes:
        course_id (str): The ID of the course.
        lecturer_id (str): The ID of the lecturer.
    """
    __tablename__ = 'course_lecturers'
    course_id = Column(String(36), ForeignKey('course.id'))
    lecturer_id = Column(String(36), ForeignKey('lecturer.id'))
