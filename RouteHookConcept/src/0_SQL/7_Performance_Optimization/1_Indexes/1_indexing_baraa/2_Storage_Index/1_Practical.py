'''
                     
                    Columnstore Index Syntax
                    ========================


SQL Server
----------

CREATE [CLUSTERED | NONCLUSTERED] [COLUMNSTORE] INDEX idx_tableName_columnNames 
ON tableName (column1, column2, ...)
                              |
                      Default → ROWSTORE



Rowstore
--------           
                   |      
                   |- CREATE NONCLUSTERED INDEX idx_tableName_columnName 
                   |  ON tableName (columnName)            
                   |
                   |- CREATE CLUSTERED INDEX idx_tableName_columnName 
                   |  ON tableName (columnName)
                   |


Columnstore
-----------
                   |      
                   |- CREATE NONCLUSTERED COLUMNSTORE INDEX idx_tableName_columnName 
                   |  ON tableName (column1, column2, ...)
                   |
                   |- CREATE CLUSTERED COLUMNSTORE INDEX idx_tableName 
                   |  ON tableName
                   |            |
                   |            └── ❌ Not Allowed To Specify Columns



Rules
-----

➤ You can't specify columns in CLUSTERED COLUMNSTORE INDEX  
➤ It stores full table in columnar format  



MySQL Workbench
---------------

❌ Columnstore Index NOT supported directly in MySQL  

➤ MySQL uses only ROWSTORE (B-Tree Index)  
➤ No native COLUMNSTORE feature available  



Snowflake
---------

                   |      
                   |- ❌ No Manual Index Creation Required
                   |
                   |- ✔ Automatic Columnar Storage (Default)
                   |
                   |- ✔ Uses Micro-Partitions (Columnar Format)
                   |
                   |- ✔ Automatic Optimization (No DBA effort)
                   |
                   |- ✔ Supports Clustering (Optional)
                   |      CREATE TABLE tableName 
                   |      CLUSTER BY (columnName)
                   |


Key Points
----------

➤ Snowflake is Fully Columnar (No Rowstore option)  
➤ No need to create indexes manually  
➤ Query optimization handled automatically  
➤ Designed for OLAP (Analytics workloads)  






# =================================================================================================
# Check Storage Efficiency in SQL Server (Heap vs Rowstore vs Columnstore)
# =================================================================================================

USE AdventureWorksDW2022;


# -------------------------------------------------------------------------------------------------
# 1. HEAP TABLE (No Index)
# -------------------------------------------------------------------------------------------------

SELECT *
INTO FactInternetSales_HP
FROM FactInternetSales;


# -------------------------------------------------------------------------------------------------
# 2. ROWSTORE TABLE (Clustered Index)
# -------------------------------------------------------------------------------------------------

SELECT *
INTO FactInternetSales_RS
FROM FactInternetSales;

CREATE CLUSTERED INDEX idx_FactInternetSales_RS_PK
ON FactInternetSales_RS (SalesOrderNumber, SalesOrderLineNumber);


# -------------------------------------------------------------------------------------------------
# 3. COLUMNSTORE TABLE (Clustered Columnstore Index)
# -------------------------------------------------------------------------------------------------

SELECT *
INTO FactInternetSales_CS
FROM FactInternetSales;

CREATE CLUSTERED COLUMNSTORE INDEX idx_FactInternetSales_CS
ON FactInternetSales_CS;


# -------------------------------------------------------------------------------------------------
# CHECK STORAGE (GUI METHOD)
# -------------------------------------------------------------------------------------------------

# Right Click Table → Properties → Storage


# -------------------------------------------------------------------------------------------------
# STORAGE OBSERVATION
# -------------------------------------------------------------------------------------------------

# FactInternetSales_HP (Heap)
# ---------------------------
# Data Space   : ~9,633 MB
# Index Space  : ~0 MB

# FactInternetSales_RS (Rowstore)
# -------------------------------
# Data Space   : ~9,633 MB
# Index Space  : Higher than Heap

# Reason:
# - Both store data in ROW format
# - So Data Space is SAME
# - Rowstore maintains B+ Tree index → extra index space


# FactInternetSales_CS (Columnstore)
# ----------------------------------
# Data Space   : ~1,461 MB
# Index Space  : ~0 MB

# Reason:
# - Data stored COLUMN-wise
# - Uses high compression (encoding techniques)
# - No traditional B+ Tree index


# -------------------------------------------------------------------------------------------------
# CORE CONCEPT
# -------------------------------------------------------------------------------------------------

# Heap        → No index, direct table scan
# Rowstore    → Row-wise storage + B+ Tree index
# Columnstore → Column-wise storage + compression


# -------------------------------------------------------------------------------------------------
# FINAL RANKING (Storage Efficiency)
# -------------------------------------------------------------------------------------------------

# 1. Columnstore Index  → Best (Highly Compressed)
# 2. Heap               → Medium (No index overhead)
# 3. Rowstore Index     → Least (Extra index storage)


# -------------------------------------------------------------------------------------------------
# INTERVIEW TAKEAWAY
# -------------------------------------------------------------------------------------------------

# - Columnstore drastically reduces storage using compression
# - Rowstore improves lookup but increases storage
# - Heap is simple but not efficient for large queries

# Best Use:
# - Columnstore → Analytics / Data Warehouse (OLAP)
# - Rowstore    → Transactions / Applications (OLTP)
# - Heap        → Temporary or staging tables



'''