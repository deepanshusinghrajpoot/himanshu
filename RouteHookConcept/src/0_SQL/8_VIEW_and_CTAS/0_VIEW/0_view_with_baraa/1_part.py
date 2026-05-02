'''


View Level
==========

Definition:
lll A View is a virtual table based on the result of a SQL query.
    It does not store actual data in the database.

Key Concept:
- A View stores only the SQL query, not the data
- Data is fetched from underlying tables when the view is used

Spoken:
"A view is a virtual table that is created using a query.
 It does not store data, it only stores the query."


lll “They act as a virtual data layer similar to data marts in data warehouses.”





Use Case
--------

“Views are used to store complex business logic for reuse.”
“They help hide query complexity by providing a simple interface to users.”
“Views improve data security by hiding sensitive rows and columns.”
“They provide flexibility by allowing changes without affecting users.”
“Views can present data in multiple languages or formats.”
“They act as a virtual data layer similar to data marts in data warehouses.”







How View Works
==============

Step-by-Step Flow:

1. User writes:
   SELECT * FROM view_name WHERE condition;

2. Database internally:
   - Fetches the query defined inside the view
   - Executes that query on actual (physical) tables

3. Result:
   - Data is returned as if it is coming from a table

Spoken:
"When we query a view, the database runs the stored query behind the view,
fetches data from the actual tables, and returns the result."


View vs Table
=============

View                          | Table
-----------------------------|-------------------------
No Data Storage              | Stores actual data
Virtual Table                | Physical Table
Stores Query Only            | Stores Data
Slower (query runs each time)| Faster (data already stored)
Mostly Read-Only             | Supports Read and Write
Easy to Maintain             | Maintenance depends on design

Spoken:
"A view does not store data and works like a virtual table,
while a table stores actual data physically in the database."


Advantages of View
==================

- Simplifies complex queries
- Improves security (hide sensitive data)
- Reusable query logic
- Provides abstraction

Spoken:
"Views help in simplifying queries and controlling access to data."


Disadvantages of View
=====================

- Slower performance compared to tables
- Depends on underlying tables
- Complex views may not support updates

Spoken:
"Views can be slower because the query runs every time,
and complex views are not always updatable."


SQL Commands for View (DDL)
===========================

- CREATE VIEW
- ALTER VIEW
- DROP VIEW


Example:

CREATE VIEW emp_view AS
SELECT name, salary
FROM employees
WHERE salary > 50000;

Spoken:
"We use CREATE VIEW to define a view,
ALTER VIEW to modify it,
and DROP VIEW to delete it."




'''