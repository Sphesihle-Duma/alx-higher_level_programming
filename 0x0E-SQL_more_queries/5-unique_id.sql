-- Creates the table unique_id
-- The default value for id column should be 1
CREATE TABLE IF NOT EXISTS unique_id(
id INT DEFAULT 1 UNIQUE,
name VARCHAR(256)
);
