-- create database
CREATE DATABASE testdb;

-- create table for messages
\c testdb;

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    message TEXT NOT NULL
);

-- insert some initial data
INSERT INTO messages (message) VALUES
    ('Hello, World!'),
    ('This is a test message.');
