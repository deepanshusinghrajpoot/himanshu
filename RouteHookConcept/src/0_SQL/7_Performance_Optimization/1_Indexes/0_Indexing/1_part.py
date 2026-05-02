
"""


# =========================================================
# Indexing — PART 2
# =========================================================

# =========================================================
# What is Indexing?
# =========================================================

# Interview-Friendly Definition
# -----------------------------
# Indexing is a technique used by DBMS to improve the
# speed of data retrieval operations by creating a
# separate structure that allows faster searching.

# In simple words:
# Indexing helps to find data quickly without scanning
# the entire table.


# =========================================================
# Why Indexing is Needed?
# =========================================================

# lll Without Indexing
#     ----------------
#     DBMS scans each row one by one to find required data.
#     Time Complexity → O(N)



# Problem
# -------
# If table has millions of rows → query becomes slow



# lll With Indexing
#     ----------------
#     DBMS uses index structure to directly locate data.
#     Time Complexity → O(log N)



# Benefit
# -------
# Faster searching, insertion, and deletion


# =========================================================
# Which Data Structure is Used?
# =========================================================

#lll “Now, as we know, sir, DBMS uses a B+ Tree data structure for indexing.”

# DBMS uses:
# • B+ Tree


# ---------------------------------------------------------
# Why B+ Tree?
# ---------------------------------------------------------

# B+ Tree provides:

# • O(log N) search time
# • Balanced structure
# • Efficient range queries
# • Sequential access using linked leaf nodes


# =========================================================
# B+ Tree — Key Concept
# =========================================================

# lll We already know:

#     • B+ Tree is similar to B-Tree
#     • Main difference:

#     B-Tree
#     ------
#     Data stored in both internal and leaf nodes

#     B+ Tree
#     -------
#     Data stored only in leaf nodes (called data page) 
#     • And all internal nodes are stored index.
#     • And all leaf nodes are connected (linked list)




# Advantage
# ---------

# • Fast range queries
# • Efficient sequential traversal



# =========================================================
# B-Tree (Balanced Tree)
# =========================================================

# B-Trees are widely used in:
# • Databases
# • File systems
# • Indexing structures


# lll And we know in B tree
# -------------------------
# 1. Data is always stored in sorted order.
# 2. All leaf nodes are at the same level.
# 3. The tree remains balanced after every insertion.
# 4. Each node can have multiple keys and multiple children.



# Order of B-Tree
# ----------------
# lll If a B-Tree has order M:
#     Then
#     • Maximum children per node = M
#     • Maximum keys per node = M - 1

#     Left pointer        → values < key1
#     Right pointer       → key2 ≤ values



# Example
# -------
# 3-order B-tree

# Max children = 3
# Max keys     = 2


# Node Structure
# --------------

# Pointer | Key1 | Pointer | Key2 | Pointer

# Rules
# -----

# Left pointer        → values < key1
# Middle pointer      → key1 ≤ values < key2
# Right pointer       → key2 ≤ values



# ======================================
# Insert Elements into 3-Order B-Tree
# ======================================

# Data to insert
# --------------
# 9, 33, 75, 41, 98, 214, 126, 55, 72


# ---------------------------------------------------------
# Step 1 : Insert 9
# ---------------------------------------------------------

# Tree

# [ 9 ]


# ---------------------------------------------------------
# Step 2 : Insert 33
# ---------------------------------------------------------

# Node can hold 2 keys (max), so insert normally.

# [ 9 | 33 ]

+

# ---------------------------------------------------------
# Step 3 : Insert 75
# ---------------------------------------------------------

# Node overflow occurs (3 keys not allowed)

# Temporary node
# [ 9 | 33 | 75 ]

# Split occurs

# Middle element becomes root

#        [33]
#       /    \
#     [9]   [75]


# ------------------------------
# Step 4 : Insert 41
# -------------------------------------------

# 41 > 33 → go right

#        [33]
#       /    \
#     [9]   [41 | 75]


# ---------------------------------------------------------
# Step 5 : Insert 98
# ---------------------------------------------------------

# Insert in right node

# Temporary
# [41 | 75 | 98]

# Split

# Promote 75

#           [33 | 75]
#         /    |     \
#      [9]   [41]   [98]


# ---------------------------------------------------------
# Step 6 : Insert 214
# ---------------------------------------------------------

# 214 > 75 → go right

#           [33 | 75]
#         /    |      \
#      [9]   [41]   [98 | 214]


# ---------------------------------------------------------
# Step 7 : Insert 126
# ---------------------------------------------------------

# Insert in right node

# Temporary
# [98 | 126 | 214]

# Split

# Promote 126

# Temporary root overflow

#           [33 | 75 | 126]


# Root split occurs

#              [75]
#           /        \
#        [33]       [126]
#       /    \      /     \
#     [9]   [41] [98]   [214]


# ---------------------------------------------------------
# Step 8 : Insert 55
# ---------------------------------------------------------

# 55 < 75 → go left subtree
# 55 > 33 → go right child

#          [75]
#       /        \
#    [33]       [126]
#   /    \      /     \
# [9] [41 | 55] [98] [214]


# ---------------------------------------------------------
# Step 9 : Insert 72
# ---------------------------------------------------------

# Insert into [41 | 55]

# Temporary
# [41 | 55 | 72]

# Split

# Promote 55

# Left subtree becomes

#        [33 | 55]
#      /     |      \
#   [9]   [41]    [72]


# Final B-Tree

#              [75]
#          /          \
#      [33 | 55]      [126]
#     /    |    \     /     \
#   [9]  [41]  [72] [98]   [214]



# =========================================================
# B+ Tree
# =========================================================

# Interview-Friendly Definition
# -----------------------------
# B+ Tree is an extension of B-Tree where:

# • All actual data is stored in leaf nodes
# • Internal nodes only store keys for navigation
# • Leaf nodes are linked together for fast range queries

# Key Difference
# --------------

# B-Tree
# ------
# Data stored in internal nodes and leaf nodes.

# B+ Tree
# -------
# Data stored only in leaf nodes.



# =========================================================
# Final B+ Tree Structure
# =========================================================

# Internal Nodes

#              [75]
#          /          \
#      [33 | 55]      [126]


# Leaf Nodes (Linked)

# [9] → [41] → [72] → [98] → [214]

# Leaf nodes are connected using pointers.

# This helps in:
# • Range queries
# • Sequential data access



# =========================================================
# Quick Revision Points
# =========================================================

# ✔ B-Tree keeps data sorted
# ✔ All leaves remain at same level
# ✔ Order M → max children = M
# ✔ Keys per node = M - 1
# ✔ B+ Tree stores data only in leaf nodes
# ✔ Leaf nodes are linked in B+ Tree







DBMS uses B+ tree to manage its Data Pages and rows within the pages.
---------------------------------------------------------------------



  

   EmpID | EmpName
   ---------------
    19   |  e1                     
    25   |  e2
    30   |  e3
    17   |  e4
    6    |  e5
    1    |  e6
    5    |  e7
   





# =========================================================
# 3-Order B+ Tree Insertion (Step by Step)
# =========================================================

# Interview-Friendly Definition
# -----------------------------
# A B+ Tree is a balanced tree structure used in databases
# and indexing systems. All actual data is stored in the
# leaf nodes, and internal nodes are used only for navigation.

# Order = 3
# ---------
# Max children per node = 3
# Max keys per node     = 2

# Data to Insert
# --------------
# 19, 25, 30, 17, 6, 1, 5


# =========================================================
# Step 1 : Insert 19
# =========================================================

# Tree

# [19]

# (Single node which is both root and leaf)



Suppose data page hold only 3 row


                Data Page:1
                ...........
                  19, e1
                ...........

                ...........

                ...........
                   offset
                ...........

    one pointer of 19 point in data page 
        
    Data Page 1 | Data Block 1    
 


# =========================================================
# Step 2 : Insert 25
# =========================================================

# Node can hold 2 keys (allowed)

# [19 | 25]


                Data Page:1
                ...........
                  19, e1
                ...........
                  25, e2
                ...........

                ...........
                   offset
                ...........


    one pointer of 25 point in data page
        
    Data Page 1 | Data Block 1  




# =========================================================
# Step 3 : Insert 30
# =========================================================

# Temporary node
# [19 | 25 | 30]

# Overflow occurs → Split leaf

# In B+ Tree:
# • middle key goes to parent
# • leaf nodes remain linked

#          [25]
#        /      \
#   [19]      [25 | 30]

# Leaf link
# [19] → [25 | 30]





                Data Page:1
                ...........
                  19, e1
                ...........
                  25, e2
                ...........
                  30, e3
                ...........
                   offset
                ...........


    one pointer of 30 point in data page 1
        
    Data Page 1 | Data Block 1  


# =========================================================
# Step 4 : Insert 17
# =========================================================

# 17 < 25 → go to left leaf

# Temporary
# [17 | 19]

# Tree

#          [25]
#        /      \
# [17 | 19]   [25 | 30]

# Leaf link
# [17 | 19] → [25 | 30]





                Data Page:1
                ...........
                  25, e2
                ...........
                  30, e3
                ...........
            
                ...........
                   offset
                ...........

        
    Data Page 1 | Data Block 1  

    


    
                Data Page:2
                ...........
                  17, e4
                ...........
                  19, e1
                ...........
        
                ...........
                   offset
                ...........


    one pointer of 17 point in data page 2
        
    Data Page 2 | Data Block 1  


Note : New node pointer store in that data page where nearest node pointer store 
    

# =========================================================
# Step 5 : Insert 6
# =========================================================

# Insert into left leaf

# Temporary
# [6 | 17 | 19]

# Overflow → split

# Left leaf  : [6]
# Right leaf : [17 | 19]

# Promote 17 to parent

# Parent becomes

#           [17 | 25]
#         /     |      \
#      [6]  [17 | 19] [25 | 30]

# Leaf link
# [6] → [17 | 19] → [25 | 30]








                Data Page:1
                ...........
                  25, e2
                ...........
                  30, e3
                ...........
            
                ...........
                   offset
                ...........

        
    Data Page 1 | Data Block 1  

    


    
                Data Page:2
                ...........
                  17, e4
                ...........
                  19, e1
                ...........
        
                ...........
                   offset
                ...........

    Data Page 2 | Data Block 1 
                
    

                Data Page:3
                ...........
                  6, e5
                ...........
            
                ...........
        
                ...........
                   offset
                ...........

    one pointer of 6 point in data page 3
        
    Data Page 3 | Data Block 2 


Note : New node pointer store in that data page where nearest node pointer store 
    



# =========================================================
# Step 6 : Insert 1
# =========================================================

# 1 < 17 → go to first leaf

# Temporary
# [1 | 6]

# Tree

#           [17 | 25]
#         /     |      \
#    [1 | 6] [17 | 19] [25 | 30]

# Leaf link
# [1 | 6] → [17 | 19] → [25 | 30]







                Data Page:1
                ...........
                  25, e2
                ...........
                  30, e3
                ...........
            
                ...........
                   offset
                ...........

        
    Data Page 1 | Data Block 1  

    


    
                Data Page:2
                ...........
                  17, e4
                ...........
                  19, e1
                ...........
        
                ...........
                   offset
                ...........

    Data Page 2 | Data Block 1 
                
    

                Data Page:3
                ...........
                  6, e5
                ...........
                  1, e6
                ...........
        
                ...........
                   offset
                ...........

    one pointer of 6 point in data page 3
        
    Data Page 3 | Data Block 2 


Note : New node pointer store in that data page where nearest node pointer store 
    



# =========================================================
# Step 7 : Insert 5
# =========================================================

# Insert into first leaf

# Temporary
# [1 | 5 | 6]

# Overflow → split

# Left leaf  : [1]
# Right leaf : [5 | 6]

# Promote 5 to parent

# Parent temporary
# [5 | 17 | 25]

# Parent overflow → split internal node


# =========================================================
# Root Split
# =========================================================

# Middle key promoted → 17 becomes new root


# Final B+ Tree

#                [17]
#            /          \
#        [5]            [25]
#      /     \        /      \
#   [1]   [5 | 6]  [17 | 19] [25 | 30]


# =========================================================
# Leaf Node Links (Important Feature of B+ Tree)
# =========================================================

# [1] → [5 | 6] → [17 | 19] → [25 | 30]


# =========================================================
# Important Points for Quick Revision
# =========================================================

# ✔ B+ Tree keeps data sorted
# ✔ All leaf nodes are at same level
# ✔ Internal nodes store only keys
# ✔ Actual data stored only in leaf nodes
# ✔ Leaf nodes are linked for fast range queries


"""
