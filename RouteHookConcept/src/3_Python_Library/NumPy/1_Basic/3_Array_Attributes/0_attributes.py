"""

NUMPY ARRAY ATTRIBUTES
======================

NumPy arrays provide several attributes that help us understand
the structure, size, and data type of the array.



Import NumPy
------------

import numpy as np



Create Sample Arrays
--------------------

a1 = np.arange(10, dtype=np.int32)

a2 = np.arange(12, dtype=float).reshape(3, 4)

a3 = np.arange(8).reshape(2, 2, 2)



Explanation
-----------

a1 → 1D array containing 10 elements

a2 → 2D array (3 rows × 4 columns)

a3 → 3D array with shape (2, 2, 2)

(2, 2, 2) means:

• 2 matrices
• each matrix is 2 × 2



Print Arrays
------------

print(a1)
# [0 1 2 3 4 5 6 7 8 9]

print(a2)
# [[ 0.  1.  2.  3.]
#  [ 4.  5.  6.  7.]
#  [ 8.  9. 10. 11.]]

print(a3)
# [[[0 1]
#   [2 3]]
#
#  [[4 5]
#   [6 7]]]



1️⃣ ndim (Number of Dimensions)
===============================

Definition (Interview Friendly)

lll ndim returns the number of dimensions of the array.

Example
-------

print(a1.ndim)   # 1
print(a2.ndim)   # 2
print(a3.ndim)   # 3



2️⃣ shape
=========

Definition (Interview Friendly)

lll shape returns the structure of the array in the form (rows, columns, depth).

Example
-------

print(a1.shape)
# (10,)
# means a1 contains 10 elements

print(a2.shape)
# (3, 4)
# means 3 rows and 4 columns

print(a3.shape)
# (2, 2, 2)
# means 2 matrices of size 2 × 2



3️⃣ size
========

Definition (Interview Friendly)

size returns the total number of elements in the array.


Example
-------

print(a1.size)
# 10

print(a2.size)
# 12

print(a3.size)
# 8



4️⃣ itemsize
============

Definition (Interview Friendly)

itemsize returns the size (in bytes) of each element in the array.


Example
-------

print(a1.itemsize)
# 4 bytes (int32)

print(a2.itemsize)
# 8 bytes (float64)

print(a3.itemsize)
# 8 bytes (int64)



5️⃣ dtype
=========

Definition (Interview Friendly)

dtype tells us the data type of the elements stored inside the NumPy array.


Example
-------

print(a1.dtype)
# int32

print(a2.dtype)
# float64

print(a3.dtype)
# int64



⭐ Important Points
==================

• ndim → number of dimensions of the array
• shape → structure of the array
• size → total number of elements
• itemsize → memory size of each element
• dtype → data type of the array elements



⭐ Interview Quick Summary
==========================

lll NumPy arrays provide several attributes that help us understand
    the structure, size, and data type of the array.

ndim      → ndim returns the number of dimensions of the array.
shape     → shape returns the structure of the array in the form (rows, columns, depth).
size      → size returns the total number of elements in the array.
itemsize  → itemsize returns the size (in bytes) of each element in the array. 
dtype     → dtype tells us the data type of the elements stored inside the NumPy array. 


"""