CREATE TABLE humans(
    human_id SERIAL PRIMARY KEY,
    fname VARCHAR(25) NOT NULL,
    lname VARCHAR(25) NOT NULL,
    email VARCHAR(100) NOT NULL
);

INSERT INTO humans (fname, lname, email) VALUES ('Bob', 'Personne','bpersonne@yahoo.com');
INSERT INTO humans (fname, lname, email) VALUES ('Jane', 'Doe','jdoe@gmail.com');
INSERT INTO humans (fname, lname, email) VALUES ('Jasmine', 'Debugger','jdebugs@hotmail.com');
INSERT INTO humans (fname, lname, email) VALUES ('John', 'Doe','john_doe@gmail.com');
INSERT INTO humans (fname, lname, email) VALUES ('Jane', 'Hacks','jhacks@gmail.com');

CREATE TABLE animals(
    animal_id SERIAL PRIMARY KEY,
    human_id INTEGER REFERENCES humans,
    name VARCHAR(50) NOT NULL,
    animal_species VARCHAR(25) NOT NULL,
    birth_year INTEGER
);

INSERT INTO animals (human_id, name, animal_species, birth_year) VALUES (1,'Fluffy','cat',2010);
INSERT INTO animals (human_id, name, animal_species, birth_year) VALUES (2,'Squiggles','snake',2016);
INSERT INTO animals (human_id, name, animal_species, birth_year) VALUES (3,'Fido','dog',2015);
INSERT INTO animals (human_id, name, animal_species, birth_year) VALUES (2,'Birdy','bird',2017);
INSERT INTO animals (human_id, name, animal_species, birth_year) VALUES (4,'Bubbles','fish',NULL);
INSERT INTO animals (human_id, name, animal_species, birth_year) VALUES (2,'Mr. Hops','rabbit',NULL);
INSERT INTO animals (human_id, name, animal_species, birth_year) VALUES (5,'Bugs','rabbit',2016);
INSERT INTO animals (human_id, name, animal_species, birth_year) VALUES (1,'Cuddles','cat',NULL);
INSERT INTO animals (human_id, name, animal_species, birth_year) VALUES (5,'Buster','dog',2011);
INSERT INTO animals (human_id, name, animal_species, birth_year) VALUES (5,'Twinkie','dog',2014);
INSERT INTO animals (human_id, name, animal_species, birth_year) VALUES (4,'Fluffster','dog',2013);
INSERT INTO animals (human_id, name, animal_species, birth_year) VALUES (1,'Twinkles','cat',2014);
