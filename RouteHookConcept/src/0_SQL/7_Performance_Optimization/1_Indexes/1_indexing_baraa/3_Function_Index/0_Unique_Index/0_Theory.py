'''


    Functions
        |                   
-------------------                  
|                 |               
Unique        Filtered
Index         Index





Unique Index
------------

Ensures no duplicate values exist in specific column.

Benefits
   1. Enforce uniqueness 
   2. Slightly increase query performance



We already know clustered index have B+ Tree structure where index page store at internal nodes
and data page store at leaf node.

Unique Index enforce data page contain only uniqueness data.


Performance
   - Writing to an unique index is slower than non-unique.
   - Reading from an unique index is faster than non-unique.


   
'''