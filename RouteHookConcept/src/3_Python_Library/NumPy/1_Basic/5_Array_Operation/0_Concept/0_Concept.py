"""

NUMPY OPERATIONS
================

NumPy allows us to perform different types of mathematical
operations directly on arrays.

These operations are fast because NumPy uses vectorized
computations internally.



lll There are two main types of Operations in NumPy
===================================================

1️⃣ Scalar Operations
2️⃣ Vector Operations




1️⃣ Scalar Operations
====================

Definition (Interview Friendly)
-------------------------------

lll Scalar operations are performed between a NumPy array
    and a single numeric value (scalar).

In this operation, the scalar value is applied to every element
of the array.



Example
-------

import numpy as np

a = np.array([1, 2, 3, 4])

print(a + 2)
# [3 4 5 6]

print(a * 2)
# [2 4 6 8]

print(a - 1)
# [0 1 2 3]



lll There are two types of Scalar Operations
--------------------------------------------

lll 1. Arithmetic Operations

+   addition  
-   subtraction  
*   multiplication  
/   division  
%   modulus  
**  power  


Example
-------

print(a ** 2)
# [1 4 9 16]



lll 2. Relational Operations :return Boolean results.


Relational operations compare each element with the scalar value
and return Boolean results.

Example
-------

print(a > 2)
# [False False  True  True]

print(a == 2)
# [False  True False False]



2️⃣ Vector Operations
====================

Definition (Interview Friendly)
-------------------------------

lll Vector operations are performed between two NumPy arrays.
lll Both numpy arrays must have compatible shapes.

The operation is applied element-wise between the corresponding
elements of the arrays.




Example
-------

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
# [5 7 9]

print(a * b)
# [ 4 10 18]



Types of Vector Operations
--------------------------

1. Arithmetic Operations

+   addition  
-   subtraction  
*   multiplication  
/   division  



Example
-------

print(a - b)
# [-3 -3 -3]



2. Relational Operations

Used to compare elements of two arrays.


Example
-------

print(a > b)
# [False False False]

print(a == b)
# [False False False]



⭐ Important Points
==================

• Scalar operation → array with a single value  
• Vector operation → array with another array  
• Operations are performed element-wise  
• NumPy operations are faster than Python loops  



⭐ Interview Quick Summary
==========================

Scalar Operation → operation between array and a single value

Vector Operation → operation between two arrays (element-wise)


"""