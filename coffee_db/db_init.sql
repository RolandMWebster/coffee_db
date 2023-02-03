CREATE TABLE coffee (
  id serial PRIMARY KEY,
  name VARCHAR,
  country_of_origin VARCHAR,
  roastery VARCHAR,
  process VARCHAR,
  varietal VARCHAR,
  elevation INT
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

INSERT INTO coffee (id, name, country_of_origin, roastery, process, varietal, elevation) VALUES
    (1, 'Finca Mumuxa', 'Guatemala', 'Carrow', 'Washed', 'Catuai', 1800);

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