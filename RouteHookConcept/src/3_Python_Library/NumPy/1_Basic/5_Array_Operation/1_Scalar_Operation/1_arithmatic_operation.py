"""

NUMPY SCALAR ARITHMETIC OPERATIONS
==================================

Import NumPy
------------

import numpy as np



1️⃣ Scalar Arithmetic Operations
================================

Definition (Interview Friendly)
-------------------------------

Scalar arithmetic operations are operations performed between
a NumPy array and a single numeric value (scalar).

The operation is applied to every element of the array.



Example
-------

a1 = np.arange(12).reshape(3, 4)

print(a1)

# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]



Power Operation
---------------

a2 = a1 ** 2

print(a2)

# [[  0   1   4   9]
#  [ 16  25  36  49]
#  [ 64  81 100 121]]



Explanation
-----------

Each element of array a1 is squared individually.



Other Scalar Arithmetic Operations
==================================

We can perform many arithmetic operations between a NumPy array
and a scalar value.


Addition
--------

print(a1 + 2)



Subtraction
-----------

print(a1 - 2)



Multiplication
--------------

print(a1 * 2)



Division
--------

print(a1 / 2)



Floor Division
--------------

print(a1 // 2)



Modulus
-------

print(a1 % 2)



Power
-----

print(a1 ** 2)



⭐ Important Points
==================

• Scalar operations apply a single value to every array element  
• Operations are performed element-wise  
• NumPy performs these operations without loops  
• This is called vectorized computation and is very fast  



⭐ Interview Quick Definition
=============================

Scalar arithmetic operations in NumPy are operations performed
between a NumPy array and a single value, where the operation
is applied to each element of the array.


"""