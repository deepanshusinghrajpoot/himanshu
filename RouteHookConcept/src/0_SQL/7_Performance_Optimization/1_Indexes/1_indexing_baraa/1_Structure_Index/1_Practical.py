'''


=================================================================================================

                                      Index Syntax
                                ------------------------


For SQL Server
--------------

CREATE [CLUSTERED | NONCLUSTERED] INDEX index_name 
ON table_name (column1, column2, ...)

       --------------------------
                  |
                  |
         Default is NONCLUSTERED


eg:

CREATE CLUSTERED INDEX IX_Customers_ID 
ON Customers (ID);

CREATE NONCLUSTERED INDEX IX_Customers_City 
ON Customers (City);

CREATE INDEX IX_Customers_Name 
ON Customers (LastName ASC, FirstName DESC);




| Feature            | MySQL           | SQL Server  |
| ------------------ | --------------- | ----------- |
| Clustered keyword  | ❌ Not supported | ✅ Supported |
| Clustered index    | PRIMARY KEY     | Explicit    |
| Multiple clustered | ❌ No            | ❌ No        |




For MySQL
==========


Create Index
------------

# MySQL creates clustered index when PRIMARY KEY is defined

ALTER TABLE database_name.table_name
ADD PRIMARY KEY (column_name);

eg:

ALTER TABLE employees 
ADD PRIMARY KEY (emp_id);



# Create Non-Clustered Index
----------------------------

CREATE INDEX idx_tableName_columnName
ON table_name(column_name);

eg:

CREATE INDEX idx_employees_city 
ON top_50_sql_faang_practice.employees (city(100));



# Drop Index in MySQL
----------------------

🔹 Drop Non-Clustered Index

DROP INDEX index_name 
ON table_name;

eg:

DROP INDEX idx_employees_city 
ON top_50_sql_faang_practice.employees;



🔹 Drop Primary Key (Clustered Index)

ALTER TABLE table_name
DROP PRIMARY KEY;

eg:

ALTER TABLE employees
DROP PRIMARY KEY;





Composite Index
===============

CREATE INDEX idx_table_col1_col2
ON table_name(column1, column2);

eg:

CREATE INDEX idx_employees_role_city 
ON top_50_sql_faang_practice.employees (role(100), city(100));



SELECT *
FROM top_50_sql_faang_practice.employees
WHERE role='SDE1' AND city='Noida';



RULE: Column Order Matters
--------------------------

# Index works based on column order
# Correct usage (matches index order)

WHERE role='SDE1' AND city='Noida'   ✔ Uses Index

# Wrong usage (order mismatch)

WHERE city='Noida' AND role='SDE1'   ❌ May not fully use index





Rule: Leftmost Prefix Rule
--------------------------

# Index works only if query starts from first column

Example Index: (A, B, C, D)

-- Index WILL be used

A
A, B
A, B, C
A, B, C, D


-- Index will NOT be used

B
A, C
B, C, D
C
D



# Example Queries

-- Uses index
SELECT * 
FROM employees
WHERE role='SDE1';

-- Uses index
SELECT * 
FROM employees
WHERE role='SDE1' AND city='Noida';

-- Does NOT use index properly
SELECT * 
FROM employees
WHERE city='Noida';


'''