/*


How to run MySQL Workbench Query
-------------------------------

1st way :- Click on the Thunder (Execute) icon  
2nd way :- CTRL + ENTER (Mostly used)

MySQL Reference Icon
-------------------
Click on the MySQL reference icon to see syntax and usage of commands
like CREATE DATABASE, CREATE TABLE, etc.

Example
-------
CREATE DATABASE campusx;



Note: Before working on any database, you must select the database

1st way :- USE database_name;
2nd way :- Double-click on the database name in Navigator

Example
-------
CREATE DATABASE IF NOT EXISTS campusx;
USE campusx;

CREATE TABLE users (
     user_id INTEGER PRIMARY KEY AUTO_INCREMENT,
     user_name VARCHAR(255) NOT NULL,
     email VARCHAR(255) NOT NULL UNIQUE,
     password VARCHAR(255) NOT NULL
);



Refresh Database
----------------
After clicking the Refresh icon, schema changes are visible.

Table Icons (on Hover)
---------------------

(1). Information icon  
     Shows table structure, columns, indexes, and constraints.

(2). Alter Table icon  
     Used to modify table structure (add, remove, or change columns).

(3). Select Rows icon  
     Displays table data using SELECT query.



================================================================================



DML (Data Manipulation Language)
================================

DML is used to manipulate data inside database tables.

1. INSERT : Used to add new records into a table.
2. SELECT : Used to retrieve data from a table.
3. UPDATE : Used to modify existing records.
4. DELETE : Used to remove records from a table.



================================================================================



(1). INSERT
____________

Single value
------------

INSERT INTO campusx.users (user_id, user_name, email, password)
VALUES (NULL, 'Deepanshu', 'deepanshu2345@gmail.com', '72355481p');

OR

INSERT INTO campusx.users
VALUES (NULL, 'Deepanshu', 'deepanshu2345@gmail.com', '72355481p');

Note :- Column order must match table structure.



Multiple values
---------------

INSERT INTO campusx.users VALUES
(NULL, 'Deepanshu', 'deepanshu2345@gmail.com', '73912355481p'),
(NULL, 'Himanshu', 'himanshu2345@gmail.com', '7239818955481p'),
(NULL, 'Shudhanshu', 'shudhanshu2345@gmail.com', '72363355481p'),
(NULL, 'Divyanshu', 'divyanshu2345@gmail.com', '7356355481p');



================================================================================



(2). SELECT
____________

How to import data in MySQL Workbench
------------------------------------
Right-click on the table → Select "Table Data Import Wizard"



USE campusx;

SELECT * FROM users;
-- Shows all rows and columns of the table



SELECT user_id, user_name FROM users;
-- Shows selected columns only



Alias
-----
Used to rename columns in the output.

SELECT CONCAT(user_name, password) AS user_password
FROM users;



Constants
---------
Used to add a temporary constant column in result.

SELECT user_name,
       password,
       'MALE' AS gender
FROM users;



================================================================================



DISTINCT
--------
Used to fetch only unique (non-duplicate) values.

SELECT DISTINCT name AS distinct_name
FROM movies;



================================================================================



WHERE Clause
------------
Used to filter rows before grouping or aggregation.

Ques:- Find movies released between 2005 and 2015
-------------------------------------------------
SELECT *
FROM movies
WHERE year BETWEEN 2005 AND 2015;



Ques:- Find movies whose name starts with 'A'
---------------------------------------------
SELECT *
FROM movies
WHERE LOWER(name) LIKE 'a%';



Ques:- Find movies where director and writer are the same
---------------------------------------------------------
SELECT *
FROM movies
WHERE director = writer;



Ques:- Find movies with score greater than 5 and gross less than 1000
---------------------------------------------------------------------
SELECT *
FROM movies
WHERE score > 5 AND gross < 1000;



================================================================================



(3). UPDATE
____________

Ques:- Update movie name Titanic to Border
------------------------------------------
UPDATE movies
SET name = 'Border'
WHERE name = 'Titanic';



Ques:- Update country and score for movie Border
------------------------------------------------
UPDATE movies
SET country = 'INDIA',
    score = 10
WHERE name = 'Border';



================================================================================



(4). DELETE
___________

Ques:- Delete movies with score less than 5
-------------------------------------------
DELETE
FROM movies
WHERE score < 5;



*/
