-- Database initialization: create table, insert default values.

CREATE TABLE numapp (
    item_id VARCHAR (50) NOT NULL,
    duration INT NOT NULL);

-- Insert 4 default values
INSERT INTO numapp (item_id, duration)
VALUES ('a', 5), ('b', 12), ('c', 24), ('d', 48);
