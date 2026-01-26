/*

How to Run a Query in MySQL Workbench
====================================

1st Way :- Click the ⚡ Thunder icon  
2nd Way :- CTRL + ENTER (most commonly used)

📌 After every command, you can check syntax using the MySQL Reference icon

Example :-
CREATE DATABASE CampusX;



lll DDL Commands for Database
=============================

DDL = Data Definition Language  
Used to define and manage database structure.

1. CREATE :- used to create a database  
2. DROP   :- used to permanently delete a database  



(1). CREATE Database
___________________

Syntax
......
CREATE DATABASE database_name;

Example
......
CREATE DATABASE campusx;

✅ Better & Safer Way
--------------------
Prevents error if the database already exists.

CREATE DATABASE IF NOT EXISTS campusx;



(2). DROP Database
_________________

Syntax
......
DROP DATABASE database_name;

Example
......
DROP DATABASE campusx;

✅ Better & Safer Way
--------------------
Prevents error if the database does not exist.

DROP DATABASE IF EXISTS campusx;




lll DDL Commands for Tables
=========================== 

1. CREATE   :- used to create a new table in a database  
2. DROP     :- used to permanently delete a table  
3. TRUNCATE :- used to delete all rows from a table but Table structure, columns, indexes, and constraints remain unchanged. 
4. ALTER    :- used to modify table structure  



ALTER allows:
(i). Add column  
(ii). Delete column  
(iii). Modify column  



(1). CREATE Table
_________________

Syntax
......
CREATE TABLE table_name (
    column_name data_type,
    column_name data_type
);

Example
......
CREATE TABLE users (
    user_id INTEGER,
    name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);



(2). DROP Table
_______________

Syntax
......
DROP TABLE table_name;

Example
......
DROP TABLE users;

✅ Better Way
-------------
DROP TABLE IF EXISTS users;



(3). TRUNCATE Table
___________________

⚠ Important Concept
-------------------
TRUNCATE deletes all rows from a table.  
Table structure, columns, indexes, and constraints remain unchanged.

Syntax
......
TRUNCATE TABLE table_name;

Example
......
TRUNCATE TABLE users;



(4). ALTER Table
________________

Used to modify table structure.



(i). Add Column
---------------

Add one column
..............
ALTER TABLE users
ADD COLUMN address VARCHAR(255) NOT NULL;

Add column at specific position
...............................
ALTER TABLE users
ADD COLUMN address VARCHAR(255) NOT NULL AFTER email;

Add multiple columns
....................
ALTER TABLE users
ADD COLUMN address VARCHAR(255) NOT NULL AFTER name,
ADD COLUMN joining_date DATETIME DEFAULT CURRENT_TIMESTAMP;



(ii). Delete Column
-------------------

Syntax
......
ALTER TABLE table_name DROP COLUMN column_name;

Example
......
ALTER TABLE users DROP COLUMN address;

Delete multiple columns
.......................
ALTER TABLE users
DROP COLUMN address,
DROP COLUMN joining_date;



(iii). Modify Column
--------------------

Used to change data type or constraints of an existing column.

Syntax
......
ALTER TABLE table_name
MODIFY COLUMN column_name data_type constraint;

Example
......
ALTER TABLE users
MODIFY COLUMN address INTEGER;


*/
