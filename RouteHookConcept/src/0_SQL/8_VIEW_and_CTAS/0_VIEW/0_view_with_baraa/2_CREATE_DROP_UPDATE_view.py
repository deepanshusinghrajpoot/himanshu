'''


SQL Views
=========

DDL Commands for View
---------------------
CREATE VIEW → Use to Create a new view
CREATE OR REPLACE VIEW → Use to Create a new view or update existing view
ALTER VIEW → Use to Modify existing view structure (if supported)
DROP VIEW → Use to Delete an existing view

(Note: UPDATE is not a DDL command for views.)







CREATE VIEW
===========

Syntax:
-------

CREATE VIEW view_name AS
SELECT column1, column2
FROM table_name
WHERE condition;

Spoken:
"CREATE VIEW is used to define a virtual table using a SQL query."


Project Folder Structure (Before Creating View)
-----------------------------------------------

project/
│
├── database/
│   ├── tables.sql        -- Contains table creation scripts
│   ├── data.sql          -- Contains insert statements
│   └── views.sql         -- Contains all view definitions
│
├── queries/
│   └── test_views.sql    -- Queries to test views
│
└── README.md


Example
-------



=====================================  CREATE ========================================

-- File: views.sql

USE top_50_sql_faang_practice;

CREATE VIEW V_Expensive_Salary AS
SELECT e.city,
       e.role,
       SUM(e.salary) AS total_expense
FROM employees e
GROUP BY e.city, e.role;



CREATE OR REPLACE VIEW V_Expensive_Salary AS
SELECT e.city,
       e.role,
       SUM(e.salary) AS total_expense
FROM employees e
GROUP BY e.city, e.role;



-- File: test_views.sql

SELECT * FROM V_Expensive_Salary;













DROP VIEW
=========

Syntax:
-------

DROP VIEW view_name;

Example:

DROP VIEW V_Expensive_Salary;








UPDATE VIEW
===========

(There is no direct UPDATE command for views in DDL)


First Way (Drop and Recreate)
-----------------------------

DROP VIEW V_Expensive_Salary;

CREATE VIEW V_Expensive_Salary AS
SELECT e.city,
       SUM(e.salary) AS total_expense
FROM employees e
GROUP BY e.city;



Second Way (Using ALTER VIEW)
-----------------------------

Syntax:

ALTER VIEW view_name AS
SELECT column1, column2
FROM table_name;

Example:

ALTER VIEW V_Expensive_Salary AS
SELECT e.city,
       SUM(e.salary) AS total_expense
FROM employees e
GROUP BY e.city;










Important Notes
===============

- Views do not store data, only the query
- Always use alias names for better readability
- Use views to simplify complex queries
- Views can be reused like tables






Final Takeaway (Interview Line)
==============================

"A view is created using CREATE VIEW,
modified using ALTER VIEW,
and removed using DROP VIEW.
It acts as a reusable virtual table based on a query."



'''