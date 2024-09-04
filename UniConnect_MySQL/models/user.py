#!/usr/bin/python3
"""
Defines the user class.
Inherits from BaseModel class.
"""
from sqlalchemy import Column, String, DateTime, Enum, BLOB
from models.base_model import BaseModel

class User(BaseModel):
    __tablename__ = 'user'
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    profile_picture = Column(BLOB)
    user_type = Column(Enum('student', 'lecturer'), nullable=False)

    def __str__(self):
        return f"<User(id='{self.id}', first_name='{self.first_name}', last_name='{self.last_name}', email='{self.email}', user_type='{self.user_type}')>"
