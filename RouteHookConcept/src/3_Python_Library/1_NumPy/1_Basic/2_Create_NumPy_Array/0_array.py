"""

lll CREATING NUMPY ARRAY USING ARRAY METHOD
============================================

In NumPy, arrays are created using the function:

np.array()

This function converts Python sequences like lists or tuples into
NumPy arrays.

Syntax
------

np.array(object, dtype=None)

It is contain two argument
first argument indicate -> object → list, tuple, or nested sequence
second argument indicate ->  dtype  → optional parameter used to specify the data type



Import NumPy
------------

import numpy as np



1️⃣ Creating a 1D Array (Vector)
================================

A 1D array contains elements arranged in a single row.

Example
-------

a = np.array([1, 2, 3])

print(a)
print(type(a))


Output
------

[1 2 3]
<class 'numpy.ndarray'>



2️⃣ Creating a 2D Array (Matrix)
================================

A 2D array contains rows and columns.

Example
-------

b = np.array([[1, 2, 3],
              [4, 5, 6]])

print(b)


Output
------

[[1 2 3]
 [4 5 6]]



3️⃣ Creating a 3D Array (Tensor)
================================

A 3D array contains multiple 2D arrays stacked together.

Example
-------

c = np.array([[[1, 2],
               [3, 4],
               [5, 6],
               [7, 8]]])

print(c)


Output
------

[[[1 2]
  [3 4]
  [5 6]
  [7 8]]]



⭐ Important Note
================

When NumPy creates an array, it automatically assigns a default
data type based on the values provided.

For example:

np.array([1,2,3]) → integer array



4️⃣ Specifying Data Type (dtype)
================================

We can specify the data type of an array using the dtype parameter.


Example 1 : Float Data Type
---------------------------

d = np.array([1, 2, 3], dtype=float)

print(d)

Output
------

[1. 2. 3.]



Example 2 : Boolean Data Type
-----------------------------

e = np.array([1, 2, 3], dtype=bool)

print(e)

Output
------

[ True  True  True ]



lll Common NumPy Data Types
============================

int        → Integer numbers
float      → Decimal numbers
bool       → True or False
str        → String values



⭐ Interview Important Points
=============================

• NumPy arrays are created using np.array()  
• Arrays can be 1D, 2D, or multi-dimensional  
• NumPy arrays store homogeneous data (same data type)  
• The dtype parameter allows us to control the data type  
• The default dtype depends on the input values  


"""