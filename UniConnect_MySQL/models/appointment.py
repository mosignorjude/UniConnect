#!/usr/bin/python3

from sqlalchemy import Column, String, DateTime, Text, Enum, ForeignKey
from models.base_model import BaseModel

class Appointment(BaseModel):
    """
    Represents an appointment.

    Attributes:
        appointment_date (DateTime): The date of the appointment.
        reason (Text): The reason for the appointment.
        student_id (String): The ID of the student associated with the appointment.
        lecturer_id (String): The ID of the lecturer associated with the appointment.
        status (Enum): The status of the appointment (scheduled, completed, canceled).
    """
    __tablename__ = 'appointment'
    appointment_date = Column(DateTime, nullable=False)
    reason = Column(Text)
    student_id = Column(String(36), ForeignKey('student.id'))
    lecturer_id = Column(String(36), ForeignKey('lecturer.id'))
    status = Column(Enum('scheduled', 'completed', 'canceled'), default='scheduled')
