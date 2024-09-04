#!/usr/bin/python3
"""
Defines the student class.
Inherits from BaseModel class.
"""
from sqlalchemy import Column, String, Enum, Float, DateTime, Text, ForeignKey
from models.base_model import BaseModel

class Student(BaseModel):
    __tablename__ = 'student'
    reg_no = Column(String(20), unique=True, nullable=False)
    program = Column(String(100))
    faculty = Column(String(100))
    department = Column(String(100))
    level = Column(Enum('100', '200', '300', '400', '500'), nullable=False)
    cgpa = Column(Float(3, 2))
    enrollment_date = Column(DateTime)
    courses = Column(Text)
    user_id = Column(String(36), ForeignKey('user.id'), unique=True)

    def __str__(self):
        return f"<Student(id='{self.id}', first_name='{self.first_name}', last_name='{self.last_name}', email='{self.email}', user_type='{self.user_type}')>"
