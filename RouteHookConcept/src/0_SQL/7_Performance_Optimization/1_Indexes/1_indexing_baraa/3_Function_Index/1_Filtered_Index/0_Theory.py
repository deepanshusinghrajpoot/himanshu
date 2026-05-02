'''



Filtered Index
==============


An index that includes only rows meeting the specified conditions.



We already know clustered index have B+ Tree structure where index page store at internal nodes
and data page store at leaf node.

but 

In Filter Index B+ Tree leaf node contain index page and this index page contain that data index
which fulfill specific condition.

Now leaf node index page point to the data page



gpt give hierarchy of B+ tree for filter index




Benefits of filter index
------------------------
   - Targeted Optimization
   - Reduce storage : Less data in the index

   
'''