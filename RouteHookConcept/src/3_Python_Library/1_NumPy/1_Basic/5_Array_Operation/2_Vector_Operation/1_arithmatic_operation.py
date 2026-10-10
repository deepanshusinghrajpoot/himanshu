"""

NUMPY VECTOR ARITHMETIC OPERATIONS
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



1️⃣ Vector Arithmetic Operations
================================

Definition (Interview Friendly)
-------------------------------

Vector arithmetic operations are operations performed between
two NumPy arrays.

The operation is applied element-wise between the corresponding
elements of the arrays.



Important Rule
--------------

Both arrays must have the same shape or compatible shape
(for broadcasting).



Example 1 : Addition
--------------------

a3 = a1 + a2

print(a3)

# [[12 14 16 18]
#  [20 22 24 26]
#  [28 30 32 34]]

Explanation
-----------

Each element of a1 is added to the corresponding element of a2.



Example 2 : Multiplication
--------------------------

a3 = a1 * a2

print(a3)

# [[  0  13  28  45]
#  [ 64  85 108 133]
#  [160 189 220 253]]

Explanation
-----------

Each element of a1 is multiplied with the corresponding element
of a2.



Other Vector Arithmetic Operations
==================================

Subtraction
-----------

print(a1 - a2)



Division
--------

print(a1 / a2)



Floor Division
--------------

print(a1 // a2)



Modulus
-------

print(a1 % a2)



Power
-----

print(a1 ** 2)



⭐ Important Points
==================

• Vector operations occur between two arrays  
• Operations are performed element-wise  
• Arrays must have compatible shapes  
• NumPy performs these operations without loops  
• This concept is called vectorization and is very fast  



⭐ Interview Quick Definition
=============================

Vector arithmetic operations in NumPy are operations performed
between two arrays where the computation happens element-wise
between their corresponding elements.


"""