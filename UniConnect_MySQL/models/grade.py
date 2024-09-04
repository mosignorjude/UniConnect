#!/usr/bin/python3
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from models.base_model import BaseModel

class Grade(BaseModel):
    """
    Represents a grade for a student in a course.

    Attributes:
        grade (float): The grade value.
        grading_date (datetime): The date when the grade was assigned.
        student_id (str): The ID of the student.
        course_id (str): The ID of the course.
    """
    __tablename__ = 'grade'
    grade = Column(Float(3, 2))
    grading_date = Column(DateTime)
    student_id = Column(String(36), ForeignKey('student.id'))
    course_id = Column(String(36), ForeignKey('course.id'))
