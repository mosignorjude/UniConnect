#!/usr/bin/python3

from sqlalchemy import Column, String, Enum, DECIMAL, DateTime, ForeignKey
from models.base_model import BaseModel

class Payment(BaseModel):
    """
    Represents a payment made by a student.

    Attributes:
        payment_type (str): The type of payment (fees or other).
        amount (float): The amount of the payment.
        payment_date (datetime): The date of the payment.
        reference_number (str): The unique reference number of the payment.
        student_id (str): The ID of the student who made the payment.
    """
    __tablename__ = 'payment'
    payment_type = Column(Enum('fees', 'other'), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    payment_date = Column(DateTime)
    reference_number = Column(String(50), unique=True, nullable=False)
    student_id = Column(String(36), ForeignKey('student.id'))
