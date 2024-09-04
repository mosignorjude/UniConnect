#!/usr/bin/python3
"""
Defines the courses class.
Inherits from BaseModel class.
"""
from sqlalchemy import Column, String, Text, Integer, DateTime
from models.base_model import BaseModel

class Course(BaseModel):
    __tablename__ = 'course'
    course_name = Column(String(100), nullable=False)
    course_code = Column(String(20), unique=True, nullable=False)
    description = Column(Text)
    lecturers = Column(Text)
    course_credits = Column(Integer, nullable=False)
    schedule = Column(DateTime)
    syllabus = Column(Text)
