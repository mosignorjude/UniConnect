#!/usr/bin/python3
"""
Defines the lecturer class.
Inherits from BaseModel class.
"""
from sqlalchemy import Column, String, Enum, ForeignKey
from models.base_model import BaseModel

class Lecturer(BaseModel):
    __tablename__ = 'lecturer'
    department = Column(String(100))
    program = Column(String(100))
    contact = Column(String(15))
    rank = Column(Enum('Assistant Professor', 'Associate Professor', 'Professor'), nullable=False)
    user_id = Column(String(36), ForeignKey('user.id'), unique=True)

    def __str__(self):
        return f"<Lecturer(id='{self.id}', department='{self.department}', program='{self.program}', contact='{self.contact}', rank='{self.rank}', user_id='{self.user_id}', created_at='{self.created_at}', updated_at='{self.updated_at}')>"
