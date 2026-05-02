'''


=================================================================================================

                              Filter Index Syntax
                        ==============================


In SQL Server
-------------

CREATE [UNIQUE] [NONCLUSTERED] INDEX idx_tableName_columnName 
ON table_name (column1, column2, ... )
WHERE [Condition];


# Example:

CREATE NONCLUSTERED INDEX idx_employees_active
ON employees (city)
WHERE status = 'Active';



Rules
-----

# - “Filtered index is always non-clustered because it stores only a subset of rows, while clustered index must store the complete table.”
# - Cannot create filtered index on clustered index
# - Cannot create filtered index on columnstore index
# - Works only on subset of data (based on condition)







In MySQL Workbench
------------------

# MySQL does NOT support Filtered Index directly ❌

# Alternative: Use Partial Indexing technique (via WHERE condition simulation)




# Method 1: Use Composite Index
................................


CREATE INDEX idx_employees_status_city
ON employees(status, city);

# Query:

SELECT *
FROM employees
WHERE status = 'Active' AND city = 'Noida';




# Method 2: Use Generated Column (Best Alternative)
...................................................


ALTER TABLE employees
ADD active_flag TINYINT 
GENERATED ALWAYS AS (status = 'Active') STORED;

CREATE INDEX idx_active_flag
ON employees(active_flag);


# Query:

SELECT *
FROM employees
WHERE active_flag = 1;




# Method 3: Use Prefix Index (for text columns)
...............................................

CREATE INDEX idx_employees_city
ON employees(city(100));


# Notes:

# - MySQL indexes always apply to FULL table
# - No direct WHERE condition in index creation
# - Generated columns simulate filtered index behavior







# Interview Line:
-----------------

# "SQL Server supports filtered indexes using WHERE clause,
# while MySQL does not support them directly and uses workarounds like generated columns."





'''