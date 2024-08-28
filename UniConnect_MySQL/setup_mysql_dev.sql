-- Prepares a MySQL server for the project.
CREATE DATABASE IF NOT EXISTS UniConnect_dev_db;
CREATE USER IF NOT EXISTS 'uc_dev'@'localhost' IDENTIFIED BY 'uc_dev_pwd';
GRANT ALL PRIVILEGES ON UniConnect_dev_db . * TO 'uc_dev'@'localhost';
GRANT SELECT ON performance_schema . * TO 'uc_dev'@'localhost';          
