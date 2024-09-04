#!/usr/bin/python3
"""
This code sets up the database connection and creates the necessary tables for the UniConnect application.

The code performs the following steps:
1. Imports the necessary modules from SQLAlchemy.
2. Imports the required models from the application.
3. Creates a database engine using the specified connection string.
4. Creates the tables defined in the models using the metadata.
5. Sets up a session factory and a scoped session for database operations.

Note: Make sure to replace 'username' and 'password' in the connection string with the actual credentials for your MySQL database.
"""
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.user import User
from models.student import Student
from models.lecturer import Lecturer
from models.course import Course
from models.enrollment import Enrollment
from models.grade import Grade
from models.lecture_notes import LectureNotes
from models.appointment import Appointment
from models.payment import Payment
from models.course_lecturers import CourseLecturers

# Create the engine
engine = create_engine('mysql+pymysql://root:testtest@localhost/UniConnect_test_db')

# Drop all existing tables using raw SQL
# WARNING THIS IS FOR DROPPING IF THE DB IS BROKEN , COMMENT OUT ON PRODUCTION
with engine.connect() as connection:
    connection.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))
    result = connection.execute(text("SHOW TABLES;"))
    tables = [row[0] for row in result]
    for table in tables:
        connection.execute(text(f"DROP TABLE IF EXISTS `{table}`;"))
    connection.execute(text("SET FOREIGN_KEY_CHECKS = 1;"))

# Create all tables
Base.metadata.create_all(engine, checkfirst=True)

# Set up the session factory and scoped session
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

# Define the storage object
class Storage:
    def __init__(self):
        self.engine = engine
        self.session = Session

storage = Storage()
