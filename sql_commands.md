mysql commands

show databases;
list current databses that exist in the mysql server 

CREATE DATABASES <name>;

List available databases:

show databases; 

The general command for creating a database:

CREATE DATABASE database_name; 

A specific example:

CREATE DATABASE soap_store; 

---------------------------------------------------

To drop a database:

DROP DATABASE database_name; 

For Example:

DROP DATABASE hello_world_db; 

Remember to be careful with this command! Once you drop a database, it's gone!

---------------------
USE <database name>;
 
-- example:
USE dog_walking_app;
 
SELECT database();
---------------------------------

CREATE TABLE tablename
  (
    column_name data_type,
    column_name data_type
  );
CREATE TABLE cats
  (
    name VARCHAR(100),
    age INT
  );

----------------------------------------------

SHOW TABLES;
 
SHOW COLUMNS FROM tablename;
 
DESC tablename;

-----------------------------------
Dropping Tables
DROP TABLE <tablename>; 

A specific example:

DROP TABLE cats; 

Be careful with this command!
-------------------------------------

example

CREATE TABLE pastries
  (
    name VARCHAR(100),
    quantity INT
  );
 
SHOW TABLES;
 
DESC pastries;
 
DROP TABLE pastries;

-------------------------------------

Inserting Data

The "formula":

INSERT INTO table_name(column_name) VALUES (data);
For example:

INSERT INTO cats(name, age) VALUES ('Jetson', 7);

-------------------------

mysql> INSERT INTO cats(name, age)
    -> VALUES('Blue', 1);
Query OK, 1 row affected (0.33 sec)

----------------------------

show values in a table

SELECT * FROM cats; 

---------------------------
multiple insert 

INSERT INTO table_name 
            (column_name, column_name) 
VALUES      (value, value), 
            (value, value), 
            (value, value);

----------------------------------------
example

INSERT Challenge Solution Code
CREATE TABLE people
  (
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    age INT
  );
INSERT INTO people(first_name, last_name, age)
VALUES ('Tina', 'Belcher', 13);
INSERT INTO people(age, last_name, first_name)
VALUES (42, 'Belcher', 'Bob');
INSERT INTO people(first_name, last_name, age)
VALUES('Linda', 'Belcher', 45)
  ,('Phillip', 'Frond', 38)
  ,('Calvin', 'Fischoeder', 70);
DROP TABLE people; 

SELECT * FROM people; 

show tables; 

-------------------------

Then view the warning:

SHOW WARNINGS; 

Try inserting a cat with incorrect data types:

INSERT INTO cats(name, age) VALUES('Lima', 'dsfasdfdas'); 

Then view the warning:

SHOW WARNINGS; 
note, warning will go away after you enter another command, 

----------------------------------
NULL and NOT NULL Code
Try inserting a cat without an age:

INSERT INTO cats(name) VALUES('Alabama'); 

SELECT * FROM cats; 

Try inserting a nameless and ageless cat:

INSERT INTO cats() VALUES(); 


Define a new cats2 table with NOT NULL constraints:



CREATE TABLE cats2
  (
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL
  );
DESC cats2; 

Now try inserting an ageless cat:

INSERT INTO cats2(name) VALUES('Texas'); 

View the new warnings:

SHOW WARNINGS; 

SELECT * FROM cats2; 

Do the same for a nameless cat:

INSERT INTO cats2(age) VALUES(7); 

SHOW WARNINGS; 

------------------------------

CODE: Setting Default Values 
Define a table with a DEFAULT name specified:

CREATE TABLE cats3
  (
    name VARCHAR(20) DEFAULT 'no name provided',
    age INT DEFAULT 99
  );
Notice the change when you describe the table:

DESC cats3; 

Insert a cat without a name:

INSERT INTO cats3(age) VALUES(13); 

Or a nameless, ageless cat:

INSERT INTO cats3() VALUES(); 

Combine NOT NULL and DEFAULT:

CREATE TABLE cats4
  (
    name VARCHAR(20) NOT NULL DEFAULT 'unnamed',
    age INT NOT NULL DEFAULT 99
  );
  
Notice The Difference:

INSERT INTO cats() VALUES();
 
SELECT * FROM cats;
 
INSERT INTO cats3() VALUES();
 
SELECT * FROM cats3;
 
INSERT INTO cats3(name, age) VALUES('Montana', NULL);
 
SELECT * FROM cats3;
 
INSERT INTO cats4(name, age) VALUES('Cali', NULL);

-----------------------------------------
PRIMARY KEYS

CODE: Primary Keys
Define a table with a PRIMARY KEY constraint:

CREATE TABLE unique_cats
  (
    cat_id INT NOT NULL,
    name VARCHAR(100),
    age INT,
    PRIMARY KEY (cat_id)
  );
DESC unique_cats; 

Insert some new cats:

INSERT INTO unique_cats(cat_id, name, age) VALUES(1, 'Fred', 23);
 
INSERT INTO unique_cats(cat_id, name, age) VALUES(2, 'Louise', 3);
 
INSERT INTO unique_cats(cat_id, name, age) VALUES(1, 'James', 3);
Notice what happens:

SELECT * FROM unique_cats; 

Adding in AUTO_INCREMENT:

CREATE TABLE unique_cats2 (
    cat_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    PRIMARY KEY (cat_id)
);
INSERT a couple new cats:

INSERT INTO unique_cats2(name, age) VALUES('Skippy', 4);
INSERT INTO unique_cats2(name, age) VALUES('Jiff', 3);
INSERT INTO unique_cats2(name, age) VALUES('Jiff', 3);
INSERT INTO unique_cats2(name, age) VALUES('Jiff', 3);
INSERT INTO unique_cats2(name, age) VALUES('Skippy', 4);
Notice the difference:

SELECT * FROM unique_cats2; 

MANDATORY MEANS NOT NULL
--------------------------

able Constraints Exercise Solution
Defining The employees table:

CREATE TABLE employees (
    id INT AUTO_INCREMENT NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    middle_name VARCHAR(255),
    age INT NOT NULL,
    current_status VARCHAR(255) NOT NULL DEFAULT 'employed',
    PRIMARY KEY(id)
);
Another way of defining a primary key:



CREATE TABLE employees (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    middle_name VARCHAR(255),
    age INT NOT NULL,
    current_status VARCHAR(255) NOT NULL DEFAULT 'employed'
);
A test INSERT:

INSERT INTO employees(first_name, last_name, age) VALUES
('Dora', 'Smith', 58);

---------------------

CODE: Preparing Our Data
Let's drop the existing cats table:

DROP TABLE cats; 

Recreate a new cats table:

CREATE TABLE cats 
  ( 
     cat_id INT NOT NULL AUTO_INCREMENT, 
     name   VARCHAR(100), 
     breed  VARCHAR(100), 
     age    INT, 
     PRIMARY KEY (cat_id) 
  ); 
DESC cats; 

And finally insert some new cats:

INSERT INTO cats(name, breed, age) 
VALUES ('Ringo', 'Tabby', 4),
       ('Cindy', 'Maine Coon', 10),
       ('Dumbledore', 'Maine Coon', 11),
       ('Egg', 'Persian', 4),
       ('Misty', 'Tabby', 13),
       ('George Michael', 'Ragdoll', 9),
       ('Jackson', 'Sphynx', 7);
-------------------

SELECT * FROM cats;
* means all columns, 

SELECT Expression
what columns do you want? 
SELECT name, age FROM cats; 

CODE: Official Introduction to SELECT
Section 5, Lecture 70
Various Simple SELECT statements:
SELECT * FROM cats; 

SELECT name FROM cats; 

SELECT age FROM cats; 

SELECT cat_id FROM cats; 

SELECT name, age FROM cats; 

SELECT cat_id, name, age FROM cats; 

SELECT age, breed, name, cat_id FROM cats; 

SELECT cat_id, name, age, breed FROM cats; 



SELECT name FROM cats; 

---------------------------------------------

WHERE clause, - what we want to delte what we want to update, 

where used all the time, update and delete, specific, 

CODE: Introduction to WHERE
Select by age:

SELECT * FROM cats WHERE age=4; 

Select by name:

SELECT * FROM cats WHERE name='Egg'; 

Notice how it deals with case:

SELECT * FROM cats WHERE name='egG'; 

------------------------
CODE: Select Challenges Solution
SELECT cat_id FROM cats; 

SELECT name, breed FROM cats; 

SELECT name, age FROM cats WHERE breed='Tabby'; 

SELECT cat_id, age FROM cats WHERE cat_id=age; 

SELECT * FROM cats WHERE cat_id=age; 

----------------

CODE: Introduction to Aliases

SELECT cat_id AS id, name FROM cats;
 
SELECT name AS 'cat name', breed AS 'kitty breed' FROM cats;
 
DESC cats;

----------------------

UPDATE ALTER EXISTING DATA, MADE A MISTAKE???? FOR GOT PASSOWRKD USER, CHANGE 
PROFILE PICTURE ON FACEBOOK, ETC......

UPDATE cats SET breed='Shorthair'
WHERE breed='Tabby';

--------------------------
CODE: Updating Data
Change tabby cats to shorthair:

UPDATE cats SET breed='Shorthair' WHERE breed='Tabby'; 

Another update:

UPDATE cats SET age=14 WHERE name='Misty'; 
-------------------------
rememebr you can always update by unique id, 
also check with select firs,t 
check if the name is there etc.... 


CODE: Update Challenges Solution
SELECT * FROM cats WHERE name='Jackson';
 
UPDATE cats SET name='Jack' WHERE name='Jackson';
 
SELECT * FROM cats WHERE name='Jackson';
 
SELECT * FROM cats WHERE name='Jack';
 
SELECT * FROM cats WHERE name='Ringo';
 
UPDATE cats SET breed='British Shorthair' WHERE name='Ringo';
 
SELECT * FROM cats WHERE name='Ringo';
 
SELECT * FROM cats;
 
SELECT * FROM cats WHERE breed='Maine Coon';
 
UPDATE cats SET age=12 WHERE breed='Maine Coon';
 
SELECT * FROM cats WHERE breed='Maine Coon';

-------------------

DELETE 
DELETE FROM cats WHERE name='egg';

DELETE FROM cats; -- DELETES ALL ENTRIES IN TABLE SHIT

CODE: DELETING DATA
DELETE FROM cats WHERE name='Egg';
 
SELECT * FROM cats;
 
SELECT * FROM cats WHERE name='egg';
 
DELETE FROM cats WHERE name='egg';
 
SELECT * FROM cats;
 
DELETE FROM cats;

-------------------

CODE: DELETE Challenges Solution
SELECT * FROM cats WHERE age=4;
 
DELETE FROM cats WHERE age=4;
 
SELECT * FROM cats WHERE age=4;
 
SELECT * FROM cats;
 
SELECT *  FROM cats WHERE cat_id=age;
 
DELETE FROM cats WHERE cat_id=age;
 
DELETE FROM cats;
 
SELECT * FROM cats;

--------------

CODE: CRUD Exercise Create Solution
Section 6, Lecture 91
SELECT database();
 
CREATE DATABASE shirts_db;
 
use shirts_db;
 
SELECT database();
 
CREATE TABLE shirts
  (
    shirt_id INT NOT NULL AUTO_INCREMENT,
    article VARCHAR(100),
    color VARCHAR(100),
    shirt_size VARCHAR(100),
    last_worn INT,
    PRIMARY KEY(shirt_id)
  );
 
DESC shirts;
 
INSERT INTO shirts(article, color, shirt_size, last_worn) VALUES
('t-shirt', 'white', 'S', 10),
('t-shirt', 'green', 'S', 200),
('polo shirt', 'black', 'M', 10),
('tank top', 'blue', 'S', 50),
('t-shirt', 'pink', 'S', 0),
('polo shirt', 'red', 'M', 5),
('tank top', 'white', 'S', 200),
('tank top', 'blue', 'M', 15);
 
SELECT * FROM shirts;
 
INSERT INTO shirts(color, article, shirt_size, last_worn) 
VALUES('purple', 'polo shirt', 'medium', 50);
 
SELECT * FROM shirts;

--------------------
SELECT article, color FROM shirts;
 
SELECT * FROM shirts WHERE shirt_size='M';
 
SELECT article, color, shirt_size, last_worn FROM shirts WHERE shirt_size='M';

-----------

SELECT * FROM shirts WHERE article='polo shirt';
 
UPDATE shirts SET shirt_size='L' WHERE article='polo shirt';
 
SELECT * FROM shirts WHERE article='polo shirt';
 
SELECT * FROM shirts;
 
SELECT * FROM shirts WHERE last_worn=15;
 
UPDATE shirts SET last_worn=0 WHERE last_worn=15;
 
SELECT * FROM shirts WHERE last_worn=15;
 
SELECT * FROM shirts WHERE last_worn=0;
 
SELECT * FROM shirts WHERE color='white';
 
UPDATE shirts SET color='off white', shirt_size='XS' WHERE color='white';
 
SELECT * FROM shirts WHERE color='white';
 
SELECT * FROM shirts WHERE color='off white';
 
SELECT * FROM shirts;

-----------
SELECT * FROM shirts;
 
SELECT * FROM shirts WHERE last_worn=200;
 
DELETE FROM shirts WHERE last_worn=200;
 
SELECT * FROM shirts WHERE article='tank top';
 
DELETE FROM shirts WHERE article='tank top';
 
SELECT * FROM shirts WHERE article='tank top';
 
SELECT * FROM shirts;
 
DELETE FROM shirts;
 
SELECT * FROM shirts;
 
DROP TABLE shirts;
 
show tables;
 
DESC shirts;
-----------

CREATE TABLE cats
    (
        cat_id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(100),
        age INT,
        PRIMARY KEY(cat_id)
    );
 
mysql-ctl cli
 
use cat_app;
 
source first_file.sql
 
DESC cats;
 
 
 
INSERT INTO cats(name, age)
VALUES('Charlie', 17);
 
INSERT INTO cats(name, age)
VALUES('Connie', 10);
 
SELECT * FROM cats;
 
source testing/insert.sql
-------------------------------

CONCAT 
String functions 

goolge - mysql string functions, mysql documenations, :) 
sort  stuf in cartain ways obvious, important, 

how combine? 
what if i want full names? 
CONCAT(x, y, z)
CONCAT(column, anotherColumn)


CONCAT_WS - with seperator, 

SELECT CONCAT(title, '-', author_fname, '-', author_lname) FROM books;
or ....
first thing you pass in is what you want the seperator to be

