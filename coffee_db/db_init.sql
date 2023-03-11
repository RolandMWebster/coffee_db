CREATE TABLE coffee (
  id serial PRIMARY KEY,
  name VARCHAR,
  country_of_origin VARCHAR,
  roastery VARCHAR,
  process VARCHAR,
  varietal VARCHAR,
  elevation INT,
  tasting_notes VARCHAR,
  added_by VARCHAR,
  date_added TIMESTAMP
);

CREATE TABLE roastery (
  id serial PRIMARY KEY,
  name VARCHAR,
  country VARCHAR,
  UNIQUE (name, country)
);

CREATE TABLE process (
  id serial PRIMARY KEY,
  name VARCHAR UNIQUE
);

CREATE TABLE variety (
  id serial PRIMARY KEY,
  name VARCHAR UNIQUE
);

CREATE TABLE country (
  id serial PRIMARY KEY,
  name VARCHAR UNIQUE
);

CREATE TABLE coffee_user (
  id serial PRIMARY KEY,
  name VARCHAR UNIQUE
);

INSERT INTO coffee (id, name, country_of_origin, roastery, process, varietal, elevation, tasting_notes, added_by, date_added) VALUES
    (1, 'Finca Mumuxa', 'Guatemala', 'Carrow', 'Washed', 'Catuai, Caturra', 1800, 'chocolate brownie, melon, stone fruit', 'Ned', '2023-03-09 14:30:11');

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
    (2, 'Catuai'),
    (3, 'Caturra');
  
INSERT INTO coffee_user (id, name) VALUES
    (1, 'Ned'),
    (2, 'Roland');