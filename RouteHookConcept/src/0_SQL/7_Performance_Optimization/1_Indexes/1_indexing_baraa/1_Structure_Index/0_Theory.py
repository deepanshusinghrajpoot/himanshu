
'''

                           
                             PART 3
==========================================================================

                                  Structure Indexing
                                           |
        ---------------------------------------------------------------------
        |                                                                   |
 Clustered Indexing                                            Non-Clustered Indexing         


 



 Clustered Indexing
=====================

lll Order of rows inside the data page, match with order of the index.

lll Clustered Index (B+ Tree data Structure)
    ✔ Internal Node has → INDEX PAGE (keys + child pointers)  
    ✔ Leaf Node has → DATA PAGE  


    

For Example:

     Lets make it primary key


     EMPID        NAME        ADDRESS
       1           A           City1
       4           C           City3
       5           D           City4
       2           B           City2


    When I apply index on EMPID


    EMPID INDEX
    ...........
      1
    ...........
      2
    ...........
      4
    ...........
      5
    ...........



    Data Page:
   ------------
    Page ID:1
   ............
     EmpID:1
   ............
     EmpID:4
   ............
     EmpID:5
   ............
     EmpID:2
   ............
EMP5|EMP4|EMP2|EMP1
 3    2    1    0


EMP1 point to EmpID1
EMP2 point to EmpID2
EMP4 point to EmpID4
EMP5 point to EmpID5



lll 🔹 Important Rules
-----------------------

We know that
✔ Only **1 clustered index per table**  
✔ Because data can be sorted in **only one way**  
✔ If not defined manually → DBMS uses **PRIMARY KEY**  
✔ If no PK → DBMS creates **hidden sequential column (row id)**  


  


 Non-Clustered Indexing
========================

lll Order of rows inside the data page, DOES NOT match with order of the index.

lll In Non-Clustered Index (B+ Tree Structure)
    ✔ Internal Node has → INDEX PAGE (keys + child pointers)  
    ✔ Leaf Node has also → INDEX PAGE (key + pointer to DATA ROW) 

    

For Example:

     Lets make it normal index (NOT primary key)


     EMPID        NAME        ADDRESS
       1           A           City1
       4           C           City3
       5           D           City4
       2           B           City2


    When I apply NON-CLUSTERED index on NAME 


    NAME INDEX
    ...........
      A  ------> Pointer → Page1 (EmpID:1)
    ...........
      B  ------> Pointer → Page1 (EmpID:2)
    ...........
      C  ------> Pointer → Page1 (EmpID:4)
    ...........
      D  ------> Pointer → Page1 (EmpID:5)
    ...........



    Data Page:
   ------------
    Page ID:1
   ............
     EmpID:1   Name:A
   ............
     EmpID:4   Name:C
   ............
     EmpID:5   Name:D
   ............
     EmpID:2   Name:B
   ............



    🔸 Key Point:
    Index is SEPARATE from actual data
    It stores → (Key + Pointer to Data)



🔹 Important Rules
-------------------

✔ Multiple non-clustered indexes allowed per table  
✔ Data is NOT physically sorted  
✔ Index stores pointer to actual data page  
✔ Searching is fast but requires extra lookup (Index → Data)  
✔ Takes extra storage (separate structure)  




🔹 Quick Interview Line
------------------------

Non-Clustered Index = Separate structure  
that stores key + pointer to actual data location.












Main difference between Clustered Index & Non-Clustered Index
==============================================================


🔹 Clustered Index (B+ Tree Hierarchy)
______________________________________

# Rule:
# Leaf Node = DATA PAGE
# Internal Node = INDEX PAGE

👉 Structure:

            [Root Node]  (Index Page)
                  |
        -----------------------
        |                     |
 [Intermediate Node]   [Intermediate Node]
     (Index Page)         (Index Page)
        |                     |
     ---------           ---------
     |       |           |       |
 [Leaf]   [Leaf]     [Leaf]   [Leaf]
 (DATA)   (DATA)     (DATA)   (DATA)

👉 Important:
- Leaf nodes store ACTUAL DATA (table rows)
- Data is physically sorted
- No separate data page outside index

👉 Simple Line:
# Clustered Index = "Index + Data together"



V/s



🔹 Non-Clustered Index (B+ Tree Hierarchy)
_________________________________________

# Rule:
# Leaf Node = INDEX PAGE (with pointer)
# Internal Node = INDEX PAGE

👉 Structure:

            [Root Node]  (Index Page)
                  |
        -----------------------
        |                     |
 [Intermediate Node]   [Intermediate Node]
     (Index Page)         (Index Page)
        |                     |
     ---------           ---------
     |       |           |       |
 [Leaf]   [Leaf]     [Leaf]   [Leaf]
 (Index)  (Index)    (Index)  (Index)
     |       |           |       |
     ↓       ↓           ↓       ↓
   Data    Data        Data    Data
   Page    Page        Page    Page

👉 Important:
- Leaf nodes DO NOT store data
- They store pointer (Row ID / Key)
- Data is stored separately

👉 Simple Line:
# Non-Clustered Index = "Index + Pointer to Data"



And we know sir
---------------

If table have both clustered and Non-Clustered index then:

👉 Non-Clustered Index leaf node points to Clustered Index


🔹 Combined Hierarchy
_____________________

Non-Clustered Index:

            [Root Node]
                  |
            [Intermediate]
                  |
               [Leaf]
                  |
                  ↓
        Clustered Index (B+ Tree)
                  |
               [Leaf]
                  |
               DATA ROW

👉 Flow:
Non-Clustered Index → Clustered Index → Data

👉 Reason:
- Because clustered leaf node contains actual data









              Clustered Index                         |          Non-Clustered Index
-----------------------------------------------------------------------------------------------------------

Definition : Physically sorts and stores rows         | Separate structure with pointer to the data

Number of index: One Index per table                  | Multiple indexes are allowed

Read Performance : Faster                             | Slightly slower (extra lookup)

Write Performance : Slower (data reordering)          | Faster (no data movement)

Storage Efficiency : More efficient                   | Extra storage required

Use Case : Unique column                              | Search, filter, joins
         : Range queries                              | Exact match queries
         : Less frequently updated                    | Frequently queried columns



         
              

'''