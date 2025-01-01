-- Ensure the `users` database exists
CREATE DATABASE IF NOT EXISTS users;

-- Switch to the `users` database
USE users;

-- Create the `users` table if it does not exist
CREATE TABLE IF NOT EXISTS `users` (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    creation_date VARCHAR(50) NOT NULL
) AUTO_INCREMENT=1;

-- Create the admin user if it does not exist
CREATE USER IF NOT EXISTS 'admin'@'%' IDENTIFIED BY '123456';

-- Grant all privileges on the `users` database to the admin user
GRANT ALL PRIVILEGES ON users.* TO 'admin'@'%';

-- Apply the changes
FLUSH PRIVILEGES;
