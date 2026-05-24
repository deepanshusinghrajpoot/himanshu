
'''


=========================================================================================================================================
 SQL Partitions
=========================================================================================================================================


🔹 Definition
lll SQL Partitioning means dividing a large table into smaller parts (partitions)
    But logically, it is still treated as one single table.

🔹 lll We use Partitioning because
          It Improves query performance
          It Reduces full table scan
          It Supports parallel processing → faster execution
    
🔹 Real-World Example
       Suppose a table contains 3 years of data → 2024, 2025, 2026
       Old data is rarely accessed
       So, we partition data year-wise

       
👉 Example:

Partition 1 → 2024
Partition 2 → 2025
Partition 3 → 2026

🔹 How it works
When you query 2025 data
SQL engine only scans 2025 partition
Instead of scanning the entire table



'''














'''


=========================================================================================================================================
 MySQL Partitioning – Step-by-Step (Interview + Practical)
=========================================================================================================================================

lll “In MySQL, the partition column must always be included in the primary key, 
     otherwise table creation fails.”


-- Instead:
-- ✅ Partitioning is defined inside CREATE TABLE
-- ✅ Uses RANGE, LIST, HASH, KEY partitioning


-------------------------------------------------------------
🔹 One-Line Summary
-------------------------------------------------------------

-- "In MySQL, partitioning is defined at table level using RANGE/LIST/HASH,
-- unlike SQL Server which uses partition function and scheme."





Important Rule
================

Case 1: No PRIMARY KEY
_______________________

✅ Partitioning works normally.

Example:

CREATE TABLE orders (
    order_id INT,
    order_date DATE
)
PARTITION BY RANGE (YEAR(order_date));



No issue because: no PRIMARY KEY
                  no UNIQUE KEY


                  
Case 2: PRIMARY KEY Exists
___________________________

Then: Partition column must be included in the PRIMARY KEY.

Wrong Example

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    order_date DATE
)
PARTITION BY RANGE (YEAR(order_date));

❌ Error because:

partition column = order_date
PRIMARY KEY missing order_date



Correct Example
________________


CREATE TABLE orders (
    order_id INT,
    order_date DATE,
    PRIMARY KEY(order_id, order_date)
)
PARTITION BY RANGE (YEAR(order_date));


✅ Works successfully.
        Why MySQL Allows Your Current Tables

Because currently:

no uniqueness enforcement
no primary key indexing issue
MySQL does not need partition column inside key

So your examples are perfectly fine.









Type Of Partitioning
=====================


-- 🔹 1. RANGE Partitioning (Most Used)
----------------------------------------
--       Use: Date-based data (orders, logs)


CREATE TABLE orders (
    order_id INT,
    order_date DATE
)
PARTITION BY RANGE (YEAR(order_date)) (
    PARTITION p2023 VALUES LESS THAN (2024),
    PARTITION p2024 VALUES LESS THAN (2025),
    PARTITION pmax  VALUES LESS THAN (MAXVALUE)
);

| Partition | Stores Data                       |
| --------- | --------------------------------- |
| p2023     | Year < 2024                       |
| p2024     | Year < 2025                       |
| **pmax**  | **Year ≥ 2025 (all future data)** |


------------------------------------------------ 



-- 🔹 2. LIST Partitioning
---------------------------
--       Use: Category/Region data

CREATE TABLE customers (
    id INT,
    city VARCHAR(50)
)
PARTITION BY LIST COLUMNS(city) (
    PARTITION p_north VALUES IN ('Delhi', 'Lucknow'),
    PARTITION p_south VALUES IN ('Chennai', 'Bangalore')
);

-- How it works:
-- 'Lucknow' → p_north
-- 'Chennai' → p_south


------------------------------------------------

-- 🔹 3. HASH Partitioning
---------------------------
--     Use: Even data distribution

CREATE TABLE users (
    user_id INT
)
PARTITION BY HASH(user_id)
PARTITIONS 4;

-- How it works:
-- user_id % 4 decides partition
-- e.g., 5 % 4 = 1 → goes to partition 1


------------------------------------------------

-- 🔹 4. KEY Partitioning
--------------------------
--     Use: Auto hashing (no manual logic)

CREATE TABLE transactions (
    txn_id INT
)
PARTITION BY KEY(txn_id)
PARTITIONS 4;

-- How it works:
-- MySQL uses internal hash
-- Data distributed automatically


------------------------------------------------

-- 🔥 One-Line Summary
-- RANGE/LIST → value-based
-- HASH/KEY   → distribution-based








'''















'''



==========================================================================================================================================
 SQL Server Partitioning – Interview Spoken Notes
==========================================================================================================================================

-- 🔹 Definition
-- Partitioning splits a large table into smaller parts 
-- but keeps it as one logical table for querying


------------------------------------------------
🔹 Step 1: PARTITION FUNCTION
------------------------------------------------ 

-- Short Definition:
-- Defines HOW data will be divided (based on column values)

CREATE PARTITION FUNCTION PartitionByYear (DATE)
AS RANGE LEFT FOR VALUES ('2024-12-31', '2025-12-31', '2026-12-31');

-- How it works:
-- <= 2024 → Partition 1
-- <= 2025 → Partition 2
-- <= 2026 → Partition 3
-- > 2026  → Partition 4


------------------------------------------------
🔹 Step 2: FILEGROUPS
------------------------------------------------ 

-- Short Definition:
-- Logical containers to store partitions physically

ALTER DATABASE SalesDB ADD FILEGROUP FG_2024;
ALTER DATABASE SalesDB ADD FILEGROUP FG_2025;
ALTER DATABASE SalesDB ADD FILEGROUP FG_2026;
ALTER DATABASE SalesDB ADD FILEGROUP FG_2027;

-- Note:
-- PRIMARY = default filegroup


------------------------------------------------
🔹 Step 3: ADD FILES (.ndf)
------------------------------------------------

-- Short Definition:
-- Physical files mapped to filegroups

ALTER DATABASE SalesDB ADD FILE
(
   NAME = P_2024,
   FILENAME = 'C:\SQLData\P_2024.ndf'
) TO FILEGROUP FG_2024;

ALTER DATABASE SalesDB ADD FILE
(
   NAME = P_2025,
   FILENAME = 'C:\SQLData\P_2025.ndf'
) TO FILEGROUP FG_2025;

ALTER DATABASE SalesDB ADD FILE
(
   NAME = P_2026,
   FILENAME = 'C:\SQLData\P_2026.ndf'
) TO FILEGROUP FG_2026;

ALTER DATABASE SalesDB ADD FILE
(
   NAME = P_2027,
   FILENAME = 'C:\SQLData\P_2027.ndf'
) TO FILEGROUP FG_2027;


------------------------------------------------
🔹 Step 4: PARTITION SCHEME
------------------------------------------------ 

-- Short Definition:
-- Maps partitions to filegroups

CREATE PARTITION SCHEME SchemePartitionByYear
AS PARTITION PartitionByYear
TO (FG_2024, FG_2025, FG_2026, FG_2027);

-- Rule:
-- 3 boundaries → 4 partitions → 4 filegroups


------------------------------------------------
🔹 Step 5: CREATE PARTITIONED TABLE
------------------------------------------------

CREATE TABLE Sales.Orders_Partitioned 
(
     OrderID INT,
     OrderDate DATE,
     Sales INT
)
ON SchemePartitionByYear (OrderDate);

-- How it works:
-- Data is automatically stored in correct partition
-- based on OrderDate


------------------------------------------------
🔹 Step 6: INSERT DATA
------------------------------------------------

INSERT INTO Sales.Orders_Partitioned VALUES (1, '2023-05-15', 100);
INSERT INTO Sales.Orders_Partitioned VALUES (2, '2024-07-15', 100);

-- 2023 → goes to first partition
-- 2024 → goes to second partition


------------------------------------------------
🔹 CHECK PARTITION DATA
------------------------------------------------

SELECT 
      p.partition_number AS PartitionNumber,
      f.name AS FilegroupName,
      p.rows AS NumberOfRows
FROM sys.partitions p
JOIN sys.destination_data_spaces dds 
     ON p.partition_number = dds.destination_id
JOIN sys.filegroups f 
     ON dds.data_space_id = f.data_space_id
WHERE OBJECT_NAME(p.object_id) = 'Orders_Partitioned';


------------------------------------------------
🔹 Key Benefits (Interview)
------------------------------------------------

-- Faster query (partition pruning)
-- Better performance on large data
-- Parallel processing
-- Easy data management (archive/delete)


------------------------------------------------
🔹 One-Line Interview Answer
------------------------------------------------

-- "In SQL Server, partitioning is done using partition function 
-- and partition scheme, where function defines boundaries and 
-- scheme maps data to filegroups for better performance."






'''