'''


Index Management
================


|
|------[1] Monitor Index Usage
|



List all indexes on a specific table
------------------------------------


In SQL Server
.............

Syntax : sp_helpindex 'db_name.table_name'

eg:
sp_helpindex 'top_50_sql_faang_practice.employees'


# Sample Output (Simplified)

+----------------------+---------------------------+---------------------------+
| index_name           | index_description         | index_keys                |
+----------------------+---------------------------+---------------------------+
| PK_employees         | clustered, unique         | emp_id                    |
| IX_employees_city    | nonclustered              | city                      |
| IX_emp_role_city     | nonclustered              | role, city                |
+----------------------+---------------------------+---------------------------+


# Column Explanation:

index_name
----------
- Name of the index
- Used for identification and operations (DROP, ALTER)

index_description
-----------------
- Type of index
- Example values:
  - clustered / nonclustered
  - unique / non-unique
- Tells how index is structured

index_keys
----------
- Columns used in the index
- Order matters (important for performance)



In MySql Workbench
..................

Syntax : SHOW INDEX FROM db_name.table_name;

eg:
SHOW INDEX FROM top_50_sql_faang_practice.employees;


# Sample Output (Simplified)

+------------+------------+--------------+--------------+-------------+-----------+
| Table      | Key_name   | Column_name  | Seq_in_index | Non_unique  | Index_type|
+------------+------------+--------------+--------------+-------------+-----------+
| employees  | PRIMARY    | emp_id       | 1            | 0           | BTREE     |
| employees  | idx_city   | city         | 1            | 1           | BTREE     |
| employees  | idx_role   | role         | 1            | 1           | BTREE     |
| employees  | idx_role   | city         | 2            | 1           | BTREE     |
+------------+------------+--------------+--------------+-------------+-----------+


# Column Explanation:

Table
-----
- Table name where index exists

Key_name
--------
- Index name
- PRIMARY = clustered index (in InnoDB)

Column_name
-----------
- Column used in index

Seq_in_index
------------
- Order of column in composite index
- 1 = first column, 2 = second column

Non_unique
----------
- 0 → Unique index
- 1 → Non-unique index

Index_type
----------
- Type of index structure
- Usually BTREE (default in MySQL)



# Mapping (SQL Server vs MySQL)

SQL Server           → MySQL
-----------------------------------------
index_name           → Key_name
index_description    → Non_unique + Index_type
index_keys           → Column_name + Seq_in_index



# Interview Line:

"SQL Server uses sp_helpindex to list indexes, while MySQL uses SHOW INDEX, 
providing similar information with different column names."













=================================================================================================

Monitoring Index Usage
======================


In SQL Server
_____________


Sys
---

# SQL Server has 'sys' system schema
# It stores metadata about tables, indexes, views, constraints, etc.



=================================================================================================
indexes
.......

SELECT * FROM sys.indexes;


# Sample Output (Important Columns)

+-----------+---------------------+----------+------------------+-------------+-------------+--------------+-------------+
| object_id | name                | index_id | type_desc        | is_primary  | is_unique   | is_disabled  | fill_factor |
+-----------+---------------------+----------+------------------+-------------+-------------+--------------+-------------+
| 101       | PK_employees        | 1        | CLUSTERED        | 1           | 1           | 0            | 0           |
| 101       | idx_city            | 2        | NONCLUSTERED     | 0           | 0           | 0            | 0           |
| 101       | idx_role_city       | 3        | NONCLUSTERED     | 0           | 0           | 0            | 0           |
+-----------+---------------------+----------+------------------+-------------+-------------+--------------+-------------+


# Column Explanation:

object_id
---------
- Unique ID of table (used to join with sys.tables)

name
----
- Name of index

index_id
--------
- Internal ID of index
- 1 = Clustered Index
- >1 = Non-Clustered Index

type_desc
---------
- Type of index
- CLUSTERED / NONCLUSTERED / HEAP

is_primary
----------
- 1 = Primary Key index

is_unique
---------
- 1 = Unique index

is_disabled
-----------
- 1 = Index is disabled (not used by optimizer)

fill_factor
-----------
- Defines how full index pages should be (0 = default)
- Helps reduce page splits



=================================================================================================
tables
......

SELECT * FROM sys.tables;


# Sample Output

+-----------+------------+---------------------+---------------------+--------------+
| object_id | name       | create_date         | modify_date         | is_ms_shipped|
+-----------+------------+---------------------+---------------------+--------------+
| 101       | employees  | 2022-01-01 10:00:00 | 2023-05-01 12:00:00 | 0            |
| 102       | orders     | 2022-02-01 09:00:00 | 2023-06-01 11:00:00 | 0            |
+-----------+------------+---------------------+---------------------+--------------+


# Column Explanation:

object_id
---------
- Unique identifier of table

name
----
- Table name

create_date
-----------
- When table was created

modify_date
-----------
- Last modification time

is_ms_shipped
-------------
- 1 = System table
- 0 = User table



=================================================================================================
Dynamic Management View (DMV)
............................

SELECT * FROM sys.dm_db_index_usage_stats;


# Sample Output (Important Columns)

+-----------+----------+-------------+------------+-------------+-------------+---------------------+---------------------+
| object_id | index_id | user_seeks  | user_scans | user_lookups| user_updates| last_user_seek      | last_user_scan      |
+-----------+----------+-------------+------------+-------------+-------------+---------------------+---------------------+
| 101       | 1        | 5000        | 200        | 50          | 1000        | 2024-01-10 10:00:00 | 2024-01-10 09:00:00 |
| 101       | 2        | 100         | 3000       | 200         | 800         | 2024-01-09 08:00:00 | 2024-01-09 07:00:00 |
+-----------+----------+-------------+------------+-------------+-------------+---------------------+---------------------+


# Column Explanation:

object_id
---------
- Table ID (join with sys.tables)

index_id
--------
- Index ID (join with sys.indexes)

user_seeks
----------
- Number of times index used for SEEK operations
- Best usage (fast lookup)

user_scans
----------
- Number of full scans on index
- Less efficient

user_lookups
------------
- Extra lookup operations (Key Lookup)
- Happens when index doesn’t cover query

user_updates
------------
- Number of insert/update/delete operations
- High value = maintenance cost

last_user_seek
--------------
- Last time index used for seek

last_user_scan
--------------
- Last time index used for scan



=================================================================================================
Important Understanding
-----------------------

# Seek  → Fast (Good)
# Scan  → Slow (Bad for large tables)
# Lookup → Extra cost (optimize with covering index)
# Updates → Write overhead



=================================================================================================
Interview Insight
-----------------

# Good Index:
- High user_seeks
- Low user_scans

# Bad / Unused Index:
- user_seeks = 0
- High user_updates

# Action:
- Remove unused index
- Optimize scan-heavy index



=================================================================================================
Final Interview Line
--------------------

"SQL Server uses sys schema and DMV views like sys.dm_db_index_usage_stats to monitor index performance 
using metrics like seeks, scans, lookups, and updates."



=================================================================================================
Monitor Index Usage (SQL Server)
=================================================================================================

SELECT 
        tbl.name AS TableName,
        idx.name AS IndexName,
        idx.type_desc AS IndexType,
        idx.is_primary_key AS IsPrimaryKey,
        idx.is_unique AS IsUnique,
        idx.is_disabled AS IsDisabled,
        s.user_seeks AS UserSeeks,
        s.user_scans AS UserScans,
        s.user_lookups AS UserLookups,
        s.user_updates AS UserUpdates,
        COALESCE(s.last_user_seek, s.last_user_scan) AS LastUpdate
FROM sys.indexes idx
JOIN sys.tables tbl
    ON idx.object_id = tbl.object_id
LEFT JOIN sys.dm_db_index_usage_stats s
    ON s.object_id = idx.object_id
    AND s.index_id = idx.index_id
ORDER BY tbl.name, idx.name;



=================================================================================================

Query Output (Sample Data)
-------------------------


+------------+------------------+--------------+--------------+----------+------------+-----------+-----------+-------------+-------------+---------------------+
| TableName  | IndexName        | IndexType    | IsPrimaryKey | IsUnique | IsDisabled | UserSeeks | UserScans | UserLookups | UserUpdates | LastUpdate          |
+------------+------------------+--------------+--------------+----------+------------+-----------+-----------+-------------+-------------+---------------------+
| employees  | PK_employees     | CLUSTERED    | 1            | 1        | 0          | 12000     | 300       | 100         | 2500        | 2026-03-20 10:30:00 |
| employees  | idx_city         | NONCLUSTERED | 0            | 0        | 0          | 200       | 8000      | 500         | 2000        | 2026-03-19 09:00:00 |
| employees  | idx_role_city    | NONCLUSTERED | 0            | 0        | 0          | 150       | 400       | 50          | 900         | 2026-03-18 08:20:00 |
| employees  | idx_salary       | NONCLUSTERED | 0            | 0        | 0          | 0         | 50        | 5           | 700         | 2026-02-10 07:00:00 |
+------------+------------------+--------------+--------------+----------+------------+-----------+-----------+-------------+-------------+---------------------+



=================================================================================================

Observations
------------

🔹 PK_employees
- Very high UserSeeks ✅ → Frequently used
- Best index → KEEP

🔹 idx_city
- High UserScans ❌ → Inefficient
- Many lookups → performance issue
👉 Action: Optimize (maybe composite index)

🔹 idx_role_city
- Balanced usage ✅
- Low lookups → good design
👉 Action: KEEP

🔹 idx_salary
- UserSeeks = 0 ❌
- Still has updates → overhead
👉 Action: DROP candidate





++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++









=================================================================================================

In MySQL Workbench
------------------


Information Schema
------------------

# MySQL uses INFORMATION_SCHEMA instead of sys schema
# It stores metadata about tables, indexes, columns, etc.



=================================================================================================
indexes
.......

SELECT * 
FROM INFORMATION_SCHEMA.STATISTICS
WHERE TABLE_SCHEMA = 'top_50_sql_faang_practice';


# Sample Output (Important Columns)

+------------+------------+--------------+--------------+-------------+------------+
| TABLE_NAME | INDEX_NAME | COLUMN_NAME  | SEQ_IN_INDEX | NON_UNIQUE  | INDEX_TYPE |
+------------+------------+--------------+--------------+-------------+------------+
| employees  | PRIMARY    | emp_id       | 1            | 0           | BTREE      |
| employees  | idx_city   | city         | 1            | 1           | BTREE      |
| employees  | idx_role   | role         | 1            | 1           | BTREE      |
| employees  | idx_role   | city         | 2            | 1           | BTREE      |
+------------+------------+--------------+--------------+-------------+------------+


# Column Explanation:

TABLE_NAME
----------
- Name of table

INDEX_NAME
----------
- Name of index (PRIMARY = clustered index in InnoDB)

COLUMN_NAME
-----------
- Column used in index

SEQ_IN_INDEX
------------
- Position of column in composite index
- 1 = first column, 2 = second column

NON_UNIQUE
----------
- 0 = Unique index
- 1 = Non-unique index

INDEX_TYPE
----------
- Type of index (BTREE is default)



=================================================================================================
tables
......

SELECT * 
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'top_50_sql_faang_practice';


# Sample Output

+------------+------------+--------------+---------------------+---------------------+
| TABLE_NAME | ENGINE     | TABLE_ROWS   | CREATE_TIME         | UPDATE_TIME         |
+------------+------------+--------------+---------------------+---------------------+
| employees  | InnoDB     | 2000000      | 2022-01-01 10:00:00 | 2023-05-01 12:00:00 |
| orders     | InnoDB     | 500000       | 2022-02-01 09:00:00 | 2023-06-01 11:00:00 |
+------------+------------+--------------+---------------------+---------------------+


# Column Explanation:

TABLE_NAME
----------
- Table name

ENGINE
------
- Storage engine (InnoDB = supports indexing, transactions)

TABLE_ROWS
----------
- Approximate number of rows

CREATE_TIME
-----------
- When table was created

UPDATE_TIME
-----------
- Last update time



=================================================================================================
Index Usage (Alternative to DMV)
................................

# MySQL does NOT provide exact DMV like SQL Server ❌
# But we can use STATUS variables


SHOW GLOBAL STATUS LIKE 'Handler_read%';


# Sample Output

+--------------------------+---------+
| Variable_name            | Value   |
+--------------------------+---------+
| Handler_read_key         | 5000    |
| Handler_read_next        | 200     |
| Handler_read_rnd         | 50      |
| Handler_read_rnd_next    | 3000    |
+--------------------------+---------+


# Column Explanation:

Handler_read_key
----------------
- Index seek count (GOOD)

Handler_read_next
-----------------
- Index scan (range scan)

Handler_read_rnd
----------------
- Random read using index

Handler_read_rnd_next
---------------------
- Full table scan (BAD)



=================================================================================================
Important Understanding
-----------------------

# Handler_read_key      → Fast lookup (Good)
# Handler_read_next     → Sequential scan
# Handler_read_rnd_next → Full table scan (Bad)



=================================================================================================
Interview Insight
-----------------

# Good Index:
- High Handler_read_key

# Problem:
- High Handler_read_rnd_next → Missing index or poor query

# Action:
- Add index
- Optimize query



=================================================================================================
Final Interview Line
--------------------

"MySQL uses INFORMATION_SCHEMA for index metadata and STATUS variables like Handler_read_key to estimate index usage, 
unlike SQL Server which provides detailed DMV statistics."






=================================================================================================
Monitor Index Usage (MySQL Workbench)
=================================================================================================

-- MySQL does NOT have direct DMV like SQL Server
-- So we use INFORMATION_SCHEMA + STATUS metrics

SELECT 
    TABLE_NAME AS TableName,
    INDEX_NAME AS IndexName,
    COLUMN_NAME AS ColumnName,
    SEQ_IN_INDEX AS SeqInIndex,
    NON_UNIQUE AS NonUnique,
    INDEX_TYPE AS IndexType
FROM INFORMATION_SCHEMA.STATISTICS
WHERE TABLE_SCHEMA = 'top_50_sql_faang_practice'
ORDER BY TABLE_NAME, INDEX_NAME, SEQ_IN_INDEX;




=================================================================================================

Query Output (Sample Data)
-------------------------

+------------+------------------+--------------+-------------+------------+-----------+
| TableName  | IndexName        | ColumnName   | SeqInIndex  | NonUnique  | IndexType |
+------------+------------------+--------------+-------------+------------+-----------+
| employees  | PRIMARY          | emp_id       | 1           | 0          | BTREE     |
| employees  | idx_city         | city         | 1           | 1          | BTREE     |
| employees  | idx_role_city    | role         | 1           | 1          | BTREE     |
| employees  | idx_role_city    | city         | 2           | 1          | BTREE     |
| employees  | idx_salary       | salary       | 1           | 1          | BTREE     |
+------------+------------------+--------------+-------------+------------+-----------+



=================================================================================================

Index Usage Approximation (MySQL)
--------------------------------

SHOW GLOBAL STATUS LIKE 'Handler_read%';


# Sample Output

+--------------------------+--------+
| Variable_name            | Value  |
+--------------------------+--------+
| Handler_read_key         | 12000  |
| Handler_read_next        | 300    |
| Handler_read_rnd         | 100    |
| Handler_read_rnd_next    | 8000   |
+--------------------------+--------+



=================================================================================================

Observations
------------

🔹 PRIMARY (emp_id)
- High Handler_read_key ✅ → Frequently used
👉 Action: KEEP (clustered index)

🔹 idx_city
- High Handler_read_rnd_next ❌ → Full table scans happening
👉 Action: Optimize (maybe composite index)

🔹 idx_role_city
- Composite index → supports filtering
👉 Action: KEEP (good for queries with role + city)

🔹 idx_salary
- Rarely used
- Still increases write cost
👉 Action: DROP candidate



=================================================================================================

Important Mapping (SQL Server vs MySQL)
--------------------------------------

UserSeeks     → Handler_read_key
UserScans     → Handler_read_next / rnd_next
UserLookups   → Not directly available
UserUpdates   → Not directly available



=================================================================================================

Final Interview Line
--------------------

"MySQL does not provide direct index usage stats like SQL Server, but we estimate usage using INFORMATION_SCHEMA and Handler_read metrics."

'''