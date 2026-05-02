"""

NUMPY SCALAR RELATIONAL OPERATIONS
==================================

Import NumPy
------------

import numpy as np



Create a Sample Array
---------------------

a1 = np.arange(12).reshape(3, 4)

print(a1)

# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]



1️⃣ Scalar Relational Operations
================================

Definition (Interview Friendly)
-------------------------------

Scalar relational operations compare each element of a NumPy array
with a single value (scalar).

The comparison is performed element-wise and the result is returned
as a Boolean array (True or False).



Example 1 : Greater Than
------------------------

a2 = a1 > 5

print(a2)

# [[False False False False]
#  [False False  True  True]
#  [ True  True  True  True]]

Explanation
-----------

Each element of the array is compared with the value 5.
If the condition is true → True
If the condition is false → False



Example 2 : Equality Check
--------------------------

a2 = a1 == 5

print(a2)

# [[False False False False]
#  [False  True False False]
#  [False False False False]]

Explanation
-----------

Only the element equal to 5 returns True.



Common Relational Operators
===========================

>   Greater than  
<   Less than  
>=  Greater than or equal to  
<=  Less than or equal to  
==  Equal to  
!=  Not equal to  



Example
-------

print(a1 < 4)

print(a1 >= 8)

print(a1 != 3)



⭐ Important Points
==================

• Relational operations compare array elements with a scalar value  
• Operations are performed element-wise  
• The result is always a Boolean array  
• These operations are commonly used in filtering and data selection  



⭐ Interview Quick Definition
=============================

Scalar relational operations in NumPy compare each element of an
array with a single value and return a Boolean array indicating
whether the condition is true or false.


"""