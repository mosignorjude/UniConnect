-- Sets up the tables for UniConnect.
USE UniConnect_test_db;

CREATE TABLE IF NOT EXISTS User (
    user_id VARCHAR(36) PRIMARY KEY, -- UUID stored as VARCHAR
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    profile_picture BLOB,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    user_type ENUM('student', 'lecturer') NOT NULL,
    CHECK (user_type IN ('student', 'lecturer'))
);

CREATE TABLE IF NOT EXISTS Student (
    student_id VARCHAR(36) PRIMARY KEY, -- UUID stored as VARCHAR
    reg_no VARCHAR(20) UNIQUE NOT NULL, -- Mapping to Python's `reg_no`
    program VARCHAR(100),               -- Added to match Python class
    faculty VARCHAR(100),               -- Added to match Python class
    department VARCHAR(100),            -- Added to match Python class
    level ENUM('100', '200', '300', '400', '500') NOT NULL,
    cgpa FLOAT(3, 2),
    enrollment_date DATETIME,
    courses TEXT,                       -- Assuming list of course IDs is stored as a JSON string or similar
    user_id VARCHAR(36) UNIQUE,
    FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Lecturer (
    lecturer_id VARCHAR(36) PRIMARY KEY, -- UUID stored as VARCHAR
    department VARCHAR(100),
    program VARCHAR(100),               -- Added to match Python class
    contact VARCHAR(15),                -- Renamed to match Python class
    rank ENUM('Assistant Professor', 'Associate Professor', 'Professor') NOT NULL,
    user_id VARCHAR(36) UNIQUE,
    FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Course (
    course_id VARCHAR(36) PRIMARY KEY, -- UUID stored as VARCHAR
    course_name VARCHAR(100) NOT NULL,
    course_code VARCHAR(20) UNIQUE NOT NULL,
    description TEXT,
    lecturers TEXT,                   -- Assuming list of lecturer IDs is stored as a JSON string or similar
    course_credits INT NOT NULL,
    schedule DATETIME,
    syllabus TEXT
);

CREATE TABLE IF NOT EXISTS Enrollment (
    enrollment_id VARCHAR(36) PRIMARY KEY, -- UUID stored as VARCHAR
    reg_no VARCHAR(20),                    -- Mapping to Python's `reg_no`
    course_id VARCHAR(36),                 -- Mapping to Python's `course_id`
    enrollment_date DATETIME,
    FOREIGN KEY (reg_no) REFERENCES Student(reg_no),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

CREATE TABLE IF NOT EXISTS Grade (
    grade_id VARCHAR(36) PRIMARY KEY, -- UUID stored as VARCHAR
    grade FLOAT(3, 2),
    grading_date DATETIME,
    student_id VARCHAR(36),
    course_id VARCHAR(36),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

CREATE TABLE IF NOT EXISTS Lecture_Notes (
    note_id VARCHAR(36) PRIMARY KEY, -- UUID stored as VARCHAR
    title VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    uploaded_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    course_id VARCHAR(36),
    lecturer_id VARCHAR(36),
    FOREIGN KEY (course_id) REFERENCES Course(course_id),
    FOREIGN KEY (lecturer_id) REFERENCES Lecturer(lecturer_id)
);

CREATE TABLE IF NOT EXISTS Appointment (
    appointment_id VARCHAR(36) PRIMARY KEY, -- UUID stored as VARCHAR
    appointment_date DATETIME NOT NULL,
    reason TEXT,
    student_id VARCHAR(36),
    lecturer_id VARCHAR(36),
    status ENUM('scheduled', 'completed', 'canceled') DEFAULT 'scheduled',
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (lecturer_id) REFERENCES Lecturer(lecturer_id)
);

CREATE TABLE IF NOT EXISTS Payment (
    payment_id VARCHAR(36) PRIMARY KEY, -- UUID stored as VARCHAR
    payment_type ENUM('fees', 'other') NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATETIME,
    reference_number VARCHAR(50) UNIQUE NOT NULL,
    student_id VARCHAR(36),
    FOREIGN KEY (student_id) REFERENCES Student(student_id)
);

CREATE TABLE IF NOT EXISTS Course_Lecturers (
    course_lecturer_id VARCHAR(36) PRIMARY KEY, -- UUID stored as VARCHAR
    course_id VARCHAR(36),
    lecturer_id VARCHAR(36),
    FOREIGN KEY (course_id) REFERENCES Course(course_id),
    FOREIGN KEY (lecturer_id) REFERENCES Lecturer(lecturer_id)
);
