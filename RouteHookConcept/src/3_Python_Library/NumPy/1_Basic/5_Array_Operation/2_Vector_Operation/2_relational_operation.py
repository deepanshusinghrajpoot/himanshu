"""

NUMPY VECTOR RELATIONAL OPERATIONS
==================================

Import NumPy
------------

import numpy as np



Create Two Arrays
-----------------

a1 = np.arange(12).reshape(3, 4)
a2 = np.arange(12, 24).reshape(3, 4)

print(a1)

# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a2)

# [[12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]]



1️⃣ Vector Relational Operations
================================

Definition
----------

Vector relational operations compare the elements of two NumPy arrays.

The comparison is performed element-wise between the corresponding
elements of both arrays.

The result is a Boolean array (True or False).



Example : Equality Check
------------------------

a3 = a1 == a2
print(a3)

# [[False False False False]
#  [False False False False]
#  [False False False False]]

Explanation
-----------

Each element of a1 is compared with the corresponding element of a2.

Example comparisons:

0 == 12 → False  
1 == 13 → False  
2 == 14 → False  

Since none of the values are equal, all results are False.



Other Vector Relational Operations
==================================

Greater Than
------------

print(a1 > a2)



Less Than
---------

print(a1 < a2)



Greater Than or Equal To
------------------------

print(a1 >= a2)



Less Than or Equal To
---------------------

print(a1 <= a2)



Not Equal
---------

print(a1 != a2)



⭐ Important Points
==================

• Comparison happens element-wise  
• Both arrays must have the same shape or compatible shape  
• Result is always a Boolean array  
• Commonly used for filtering data in NumPy and Pandas



⭐ Interview Definition
======================

Vector relational operations in NumPy compare corresponding elements
of two arrays and return a Boolean array indicating whether the
condition is True or False.

"""