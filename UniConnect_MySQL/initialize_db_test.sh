#!/bin/bash

# Database credentials
DB_USER="root"
DB_PASSWORD="testtest"
DB_NAME="UniConnect_test_db"
DB_HOST="localhost"

# SQL files
SETUP_DB_SQL="setup_mysql_test.sql"
SETUP_TABLES_SQL="setup_tables_test.sql"

# Function to check if a table exists
table_exists() {
    TABLE_NAME=$1
    RESULT=$(mariadb -u$DB_USER -p$DB_PASSWORD -h$DB_HOST -e "USE $DB_NAME; SHOW TABLES LIKE '$TABLE_NAME';")
    if [[ "$RESULT" == *"$TABLE_NAME"* ]]; then
        return 0
    else
        return 1
    fi
}

# Function to check if the database exists
database_exists() {
    RESULT=$(mariadb -u$DB_USER -p$DB_PASSWORD -h$DB_HOST -e "SHOW DATABASES LIKE '$DB_NAME';")
    if [[ "$RESULT" == *"$DB_NAME"* ]]; then
        return 0
    else
        return 1
    fi
}

# Check if the database exists
if ! database_exists; then
    echo "Database $DB_NAME does not exist. Creating database and tables..."
    mariadb -u$DB_USER -p$DB_PASSWORD -h$DB_HOST < $SETUP_DB_SQL
    mariadb -u$DB_USER -p$DB_PASSWORD -h$DB_HOST $DB_NAME < $SETUP_TABLES_SQL
else
    echo "Database $DB_NAME exists. Checking tables..."
    # List of tables to check
    TABLES=("User" "Student" "Lecturer" "Course" "Enrollment" "Grade" "Lecture_Notes" "Appointment" "Payment" "Course_Lecturers")

    MISSING_TABLES=false
    for TABLE in "${TABLES[@]}"; do
        if ! table_exists $TABLE; then
            echo "Table $TABLE is missing."
            MISSING_TABLES=true
        fi
    done

    if $MISSING_TABLES; then
        echo "One or more tables are missing. Creating missing tables..."
        mariadb -u$DB_USER -p$DB_PASSWORD -h$DB_HOST $DB_NAME < $SETUP_TABLES_SQL
    else
        echo "All tables exist."
    fi
fi
