https://www.w3schools.com/sql/sql_quickref.asp

MySQL
----------------------

Syllabus and Curriculum 

Challenges, Querys, aggregate functions, logical operators, etc.. will all be covered, 

interlated data, one to many, JOINS secitons 12 and 13

instagram database clone will be a project!! This is good, 

last part, lots of data, put in database, write code to answer real questions, 

node.js, and building web app, at the very end, 

went to SQL built in editor to mess with stuff, 
------------------------------

How the course works? 
Talking, introduce content, set the stage, can skip, then the lectures are important, 

slides, diagrams and animations, 

excercisea and activites are important, 

rapid fire, general ,and entire chalenge sections, 

do them all, learn, 

Database vs coding language? 
install stuff, 
-------------------------------------------------------
MySQL
What is a databse?
1. A collection of data
2. A method for accessing and manipulating that data
Why do they matter?

What is a databse? - 1. A collection of data, files, a phone book, f_name l_name phone_book

find ned flanders, easy, find all people named ned, hard, this is why databases are importanant, 

2. A method for accessing and manipulating that data

Database vs Database Management System RDMS DMS etc.. 
Data and have an interface are 2 different things, 

you have your app, you have a database, WE talk to the DBMS, it talks to the database, 
it is the communication between our application and our database, 

What is a Database?
A structured set of computerized data with an accessible interface

----------------------------------------------------------------------------------------------------------------

MySQL vs SQL

Structred Query Language 
SQL is the language we use to 'talk' to our databse, find all users, find all who are 18 etc..
delete, add etc.. these are queires, talks to our database for us, 
SELECT ....... this is a query!

MySQL is a RDMS, we are writing with SQL, 
SQL looks the same in MySQL and PostgreSQL

There are slight syntax differences, but there is a standard, SQL standard, they have to implmnt

Once you learn SQL, easy to switch around, 
DBMS are unique for the feautres they offer, not at their core, secuirty, swiftness and permissions 
change, but not the core, 

MySQL is a DBMS that implement the SQL (strucutred query language) 

Currently using CLoud 9 IDE
not any more :__)

---- 

database server 
multiple databases all in the same database, 
how to create individual walled off databases inside of our server

camel case or snake case, just stick with it for best practice, 
be consistent, 

delete table with drop database, delete tables too 

----

how to use databases, use <data base name>

select database(); we are using null??

--------------------------------------------------

TABLES! :)

database is just a bunch of tables, in a relational database at least, 
tabular data, 

tables hold the data, 

name breed and age, can be many other things obviously, 

columns (headers) - name breed and age 
rows are data in the table, 

databases are made up of lots of tables, 

apps and data are complicated, lots to keep check of, 

-------------------------------------------------------

data types - really important obviously, 
name text breed text age integer, have data that matches, becuase what if you 
Calculate "cat age"
Age * 7 

int whole number, ranges to ma value of 2147483647

varchar - variable-length string, between 1 and 255 characters, 
name varchar(100)
breed varchar(100)
age int

-----
tweets table 
- username (max 15 chars)
- tweet content (max 140 chars)
- number of favorites

----------------

insert data and retirve in back out,  how and when to get like, 5 things you need for example, 
like the last 5 users . 

-------------------------

adding data to your tables -- important and common, how to get data in the table and out 
INSERT INTO cats(name, age)
VALUES ('Jetson', 7);

THE ORDER MATTERS WHEN YOU ARE INSERTING 


multiple insert
mysql> INSERT INTO cats(name, age)
    -> VALUES ('Peanut', 2),
    -> ('Butter', 4),
    -> ('Jelly', 7);
Query OK, 3 rows affected (0.27 sec)
--------------------

note on warnings 

SHOW WARNINGS; 

to see warnings, data truncated for example, 

warnings go away, python can help you manage your warmings, 

------------
what is NULL in the table?
'the value is not known' no specified value, 
YES means they are permitted to be null, 

if null is permitted, lets say you INSERT INTO cats() VALUES(); 
then everything is null, so specify NOT NULL when you create the table, 
that way people are forced to enter data, 

----
how to specify default values?

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


---------------------

OUR DATA NEEDS TO BE UNIQUE identied, need to be unique, 

ASSIGN AN ID, THE UNIQUE IDENTIFIER, 
THE PRIMARY KEY -- UNIQUQUE IDENTIFIER ON THE ROW
WHATEVE FIELD WE MAKE THE PRIMARY KEY, IT HAS TO BE UNIQUE, 


----
good idea to make the username a primary key so you cannot have the same username in your database
dont manually enter a primary key, AUTO_INCREMENT 

---------------

IMPORTATN ON TO CRUD 
CREATE
READ
UPDATE
DELETE
----------------------
4 BASIC ACTIONS TO OUR DATA

WE CAN CREATE WITH INSERT,  WE CAN READ WITH SELECT, NOW LOOK HOW TO UPDATE AND 
DELETE, 


RENAME JOIN ALIAS
ALIASES EASIER TO READ RESULTS 

ALIASES

SELECT cat_id AS id, name FROM cats;

------------

FINISHED CRUD 

MOVING onto STRING FUNCTIONS IN SQL

Running SQL files; 

reading data out, aggregate funcitons, etc.. 

specifically string funcitons, 

RUNNING SQL FILES, then run when ready, 


This works:

SELECT UPPER(CONCAT(author_fname, ' ', author_lname)) AS "full name in caps"
FROM books;
While this does not:

SELECT CONCAT(UPPER(author_fname, ' ', author_lname)) AS "full name in caps" 
FROM books;
UPPER only takes one argument and CONCAT takes two or more arguments, so they can't be switched in that way.

You could do it this way, however:

SELECT CONCAT(UPPER(author_fname), ' ', UPPER(author_lname)) AS "full name in caps" 
FROM books;
But, the first example above would be better (more DRY*) because you wouldn't need to call UPPER two times.

*Don't Repeat Yourself
