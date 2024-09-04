#!/usr/bin/python3
from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from models.base_model import BaseModel
import datetime
class LectureNotes(BaseModel):
    """
    Represents a lecture note.

    Attributes:
        title (str): The title of the lecture note.
        content (str): The content of the lecture note.
        uploaded_date (datetime): The date and time when the lecture note was uploaded.
        course_id (str): The ID of the course associated with the lecture note.
        lecturer_id (str): The ID of the lecturer associated with the lecture note.
    """
    __tablename__ = 'lecture_notes'
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    uploaded_date = Column(DateTime, default=datetime.datetime.utcnow)
    course_id = Column(String(36), ForeignKey('course.id'))
    lecturer_id = Column(String(36), ForeignKey('lecturer.id'))
