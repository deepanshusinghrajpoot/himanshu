
'''


=================================================================================================

INDEX
======

lll Index is Data Structure that provides quick access to data, improving query performance.



                                            Indexes
                                               |
        ---------------------------------------------------------------------------------
        |                                      |                                        |
    Structure                               Storage                                 Functions
        |                                      |                                        |
-------------------                   -------------------                      -------------------  
|                 |                   |                 |                      |                 |
Clustered    Non-Clustered            Rowstore     Columnstore                 Unique        Filtered
Index        Index                    Index        Index                       Index         Index




There are three main type of index.

1. Structure Index
     Structure Index is also devide into two type
          1. Clustered Index
          2. Non-Clustered Index
2. Storage Index
     Storage Index is also devide into two type
          1. Rowstore Index
          2. Columnstore Index
3. Function Index
     Function Index is also devide into two type
          1. Unique Index
          2. Filtered Index



          
Trade-off
.........

# lll Indexes improve READ performance but may impact WRITE performance

# Some indexes:
# - Faster for SELECT (read-heavy systems)
# - Slower for INSERT/UPDATE/DELETE (due to maintenance)



Heap Structure
--------------

# What happens if we don't use any index?

👉 Questions:
      1. How table data (rows) are actually stored?
      2. What data structure is used for indexing and how it works?

      
👉 Answer:

Heap = Table without Clustered Index


# Heap Storage Structure

- Data is stored in random order (no sorting)
- Stored in Data Pages
- No B+ Tree structure

👉 Visual:

Page 1 → [Row3, Row1]
Page 2 → [Row5, Row2]
Page 3 → [Row4, Row6]

# Data is NOT ordered


# How Data is Accessed in Heap?

- SQL Server performs FULL TABLE SCAN
- It scans all pages to find data

👉 Example:

SELECT * FROM employees WHERE id = 5;

# Without index:
- Scan Page 1 → Not found
- Scan Page 2 → Found
- Scan continues...

# Result → Slow performance



# Key Points:

- No index = No fast lookup
- Full scan required
- Poor performance for large tables
- Good for:
  - Small tables
  - Temporary data
  - Bulk inserts (fast writes)



# Important Concept:

- Heap does NOT use B+ Tree
- Only raw data pages exist
- No logical ordering



# Interview Line:

"Heap is a table without a clustered index where data is stored unordered and accessed via full table scans."







'''