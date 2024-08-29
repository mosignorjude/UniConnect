-- Prepares a MySQL Test server for the project.
CREATE DATABASE IF NOT EXISTS UniConnect_test_db;
CREATE USER IF NOT EXISTS 'uc_test'@'localhost' IDENTIFIED BY 'uc_test_pwd';
GRANT ALL PRIVILEGES ON UniConnect_test_db . * TO 'uc_test'@'localhost';
GRANT SELECT ON performance_schema . * TO 'uc_test'@'localhost'; 
