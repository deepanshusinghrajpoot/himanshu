/*


Constraints in MySQL
====================

Definition
----------
Constraints are rules applied on table columns to ensure valid, accurate,
and consistent data in the database.



There are many constraint keywords in MySQL:

(1). NOT NULL
-------------
Definition
----------
NOT NULL ensures that a column cannot store NULL values.

Example
-------
name VARCHAR(255) NOT NULL



(2). UNIQUE
-----------
Definition
----------
UNIQUE ensures that all values in a column are different.

Example
-------
email VARCHAR(255) UNIQUE



(3). PRIMARY KEY
----------------
Definition
----------
PRIMARY KEY uniquely identifies each record in a table.
It does not allow NULL or duplicate values.

Example
-------
user_id INTEGER PRIMARY KEY



(4). AUTO_INCREMENT
-------------------
Definition
----------
AUTO_INCREMENT automatically generates a unique number for new records.

Example
-------
user_id INTEGER PRIMARY KEY AUTO_INCREMENT



(5). CHECK
----------
Definition
----------
CHECK ensures that column values satisfy a specific condition.

Example
-------
age INTEGER CHECK (age >= 18)



(6). DEFAULT
------------
Definition
----------
DEFAULT assigns a default value to a column when no value is provided.

Example
-------
created_at DATETIME DEFAULT CURRENT_TIMESTAMP



(7). FOREIGN KEY
----------------
Definition
----------
FOREIGN KEY creates a relationship between two tables and maintains
referential integrity.

Example
-------
customer_id INTEGER,
FOREIGN KEY (customer_id) REFERENCES customers(customer_id)



==========================================================================================



NOT NULL, UNIQUE, PRIMARY KEY, AUTO_INCREMENT
=============================================

How to apply constraints
========================



First way to apply constraint on table
______________________________________

Syntax
......
CREATE TABLE users (
     column_name data_type constraint,
     column_name data_type constraint
);

Example
-------
CREATE TABLE users (
     user_id INTEGER PRIMARY KEY AUTO_INCREMENT,
     name VARCHAR(255) NOT NULL,
     email VARCHAR(255) UNIQUE NOT NULL,
     password VARCHAR(255) NOT NULL
);



Second way to apply constraint on table
______________________________________

Syntax
......
CREATE TABLE users (
     column_name data_type,
     column_name data_type,
     ...,

     CONSTRAINT constraint_name constraint_type (column_name)
);

Why use this syntax
------------------
Used for composite keys and custom constraint names.

Example
-------
CREATE TABLE users (
     user_id INTEGER AUTO_INCREMENT NOT NULL,
     name VARCHAR(255) NOT NULL,
     email VARCHAR(255) NOT NULL,
     password VARCHAR(255) NOT NULL,

     CONSTRAINT users_email_unique UNIQUE (email),
     CONSTRAINT users_pk PRIMARY KEY (user_id, name)
);



CHECK Constraint
****************

Question
--------
Create a table with student_id, name, and age.
Age should be between 6 and 25.

Query
-----
CREATE TABLE IF NOT EXISTS students (
     student_id INTEGER PRIMARY KEY AUTO_INCREMENT,
     name VARCHAR(255) NOT NULL,
     age INTEGER CHECK (age >= 6 AND age <= 25)
);

OR

CREATE TABLE IF NOT EXISTS students (
     student_id INTEGER PRIMARY KEY AUTO_INCREMENT,
     name VARCHAR(255) NOT NULL,
     age INTEGER NOT NULL,

     CONSTRAINT student_age_check CHECK (age >= 6 AND age <= 25)
);



DEFAULT Constraint
******************

Question
--------
Create a ticket table.
If travel_date is not provided, set default date.

Query
-----
CREATE TABLE IF NOT EXISTS ticket (
     ticket_id INTEGER PRIMARY KEY AUTO_INCREMENT,
     name VARCHAR(255) NOT NULL,
     travel_date DATETIME DEFAULT CURRENT_TIMESTAMP
);



FOREIGN KEY (Most Important Constraint)
***************************************

Question
--------
Create two tables:
customers and orders.

First table: customers
----------------------
CREATE TABLE customers (
     customer_id INTEGER PRIMARY KEY AUTO_INCREMENT,
     name VARCHAR(255) NOT NULL,
     email VARCHAR(255) UNIQUE NOT NULL
);



Second table: orders
--------------------
CREATE TABLE orders (
     order_id INTEGER PRIMARY KEY AUTO_INCREMENT,
     customer_id INTEGER NOT NULL,
     date DATETIME DEFAULT CURRENT_TIMESTAMP,

     CONSTRAINT orders_fk FOREIGN KEY (customer_id)
     REFERENCES customers(customer_id)
);





Benefit of FOREIGN KEY
----------------------

Foreign Key
-----------

Definition:

lll A Foreign Key is an attribute (or set of attributes) in one table that refers to the Primary Key of another table.
lll Foreign Key is used to link two tables together.
lll Foreign is also used maintains Referential Integrity.


Referential Action
------------------
lll Defines what happens when parent table data is updated or deleted.

There are four types of referential actions:



(1). RESTRICT (Default)
-----------------------
Prevents deletion or update of parent record if child records exist.

Example
-------
If a customer has orders, deleting that customer causes
FOREIGN KEY constraint error.



(2). CASCADE
------------
Automatically deletes or updates child records when parent changes.

Example
-------
CREATE TABLE orders (
     order_id INTEGER PRIMARY KEY AUTO_INCREMENT,
     customer_id INTEGER NOT NULL,
     date DATETIME DEFAULT CURRENT_TIMESTAMP,

     CONSTRAINT orders_fk FOREIGN KEY (customer_id)
     REFERENCES customers(customer_id)
     ON DELETE CASCADE
     ON UPDATE CASCADE
);



(3). SET NULL
-------------
Sets foreign key value to NULL when parent record is deleted or updated.

Example
-------
CREATE TABLE orders (
     order_id INTEGER PRIMARY KEY AUTO_INCREMENT,
     customer_id INTEGER NULL,
     date DATETIME DEFAULT CURRENT_TIMESTAMP,

     CONSTRAINT orders_fk FOREIGN KEY (customer_id)
     REFERENCES customers(customer_id)
     ON DELETE SET NULL
     ON UPDATE SET NULL
);



(4). SET DEFAULT
----------------
Sets foreign key value to its default value when parent is deleted or updated.

Example
-------
CREATE TABLE orders (
     order_id INTEGER PRIMARY KEY AUTO_INCREMENT,
     customer_id INTEGER DEFAULT 0,
     date DATETIME DEFAULT CURRENT_TIMESTAMP,

     CONSTRAINT orders_fk FOREIGN KEY (customer_id)
     REFERENCES customers(customer_id)
     ON DELETE SET DEFAULT
     ON UPDATE SET DEFAULT
);



*/
