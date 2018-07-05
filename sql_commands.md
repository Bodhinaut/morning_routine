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
