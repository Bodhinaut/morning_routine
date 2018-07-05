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

---

To drop a database:

DROP DATABASE database_name; 

For Example:

DROP DATABASE hello_world_db; 

Remember to be careful with this command! Once you drop a database, it's gone!

---
USE <database name>;
 
-- example:
USE dog_walking_app;
 
SELECT database();
---

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
---

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

--------------------------



