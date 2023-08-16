-- Creates the database hbtn_0d_usa
-- use the created database to create a table cities
-- id must be an integer, primary key and not null
-- stated_id column must be a foreign key
-- references id of the state table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
id INT AUTO_INCREMENT PRIMARY KEY,
state_id INT NOT NULL, 
name VARCHAR(256) NOT NULL,
FOREIGN KEY(state_id) references states(id)
);
