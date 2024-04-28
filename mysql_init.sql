CREATE DATABASE IF NOT EXISTS django_db;
CREATE USER IF NOT EXISTS 'django'@'%' IDENTIFIED BY 'django';
GRANT ALL PRIVILEGES ON django_db.* TO 'django'@'%';
GRANT ALL PRIVILEGES ON `test_django_db`.* TO 'django'@'%';
GRANT ALL PRIVILEGES ON `test_%`.* TO 'django'@'%';
FLUSH PRIVILEGES;
