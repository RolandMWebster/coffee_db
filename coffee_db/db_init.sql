CREATE TABLE coffee (
  id serial PRIMARY KEY,
  date_added TIMESTAMP,
  added_by VARCHAR,
  name VARCHAR,
  country_of_origin VARCHAR,
  roastery VARCHAR,
  process VARCHAR,
  varietal VARCHAR,
  elevation INT,
  tasting_notes VARCHAR
);

CREATE TABLE roastery (
  id serial PRIMARY KEY,
  name VARCHAR,
  country VARCHAR
);

CREATE TABLE process (
  id serial PRIMARY KEY,
  name VARCHAR
);

CREATE TABLE variety (
  id serial PRIMARY KEY,
  name VARCHAR
);

CREATE TABLE country (
  id serial PRIMARY KEY,
  name VARCHAR
);

CREATE TABLE coffee_user (
  id serial PRIMARY KEY,
  name VARCHAR
);

INSERT INTO coffee (id, date_added, added_by, name, country_of_origin, roastery, process, varietal, elevation, tasting_notes) VALUES
    (1, '2023-03-09 14:30:11', 'Ned', 'Finca Mumuxa', 'Guatemala', 'Carrow', 'Washed', 'Catuai', 1800, 'chocolate brownie, melon, stone fruit');

INSERT INTO roastery (id, name, country) VALUES
    (1, 'Carrow', 'Ireland');

INSERT INTO country (id, name) VALUES
    (1, 'Ireland'),
    (2, 'Guatemala');

INSERT INTO process (id, name) VALUES
    (1, 'Unknown'),
    (2, 'Washed');

INSERT INTO variety (id, name) VALUES
    (1, 'Unknown'),
    (2, 'Catuai');
  
INSERT INTO coffee_user (id, name) VALUES
    (1, 'Ned'),
    (2, 'Roland');