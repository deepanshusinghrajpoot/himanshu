"""

lll CREATING NUMPY ARRAY USING ONES, ZEROS AND RANDOM METHOD
============================================================

In NumPy, we often need arrays filled with default values such as
all ones, all zeros, or random numbers.

NumPy provides special functions for this purpose.



Import NumPy
------------

import numpy as np



1️⃣ np.ones()
=============

Definition (Interview Friendly)
-------------------------------

np.ones() is used to create a NumPy array filled with the value 1.

It is commonly used when we need an array initialized with ones.


lll Syntax
-----------

np.ones(shape)

shape → representing as tuple (rows, columns)


Example 1
---------

a = np.ones((2, 4))
print(a)

Output
------

[[1. 1. 1. 1.]
 [1. 1. 1. 1]]


Example 2
---------

a = np.ones((3, 4))
print(a)

Output
------

[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1]]



2️⃣ np.zeros()
==============

Definition (Interview Friendly)
-------------------------------

np.zeros() is used to create a NumPy array filled with the value 0.

It is useful when initializing arrays for calculations or placeholders.


lll Syntax
-----------

np.zeros(shape)


Example 1
---------

b = np.zeros((2, 3))
print(b)

Output
------

[[0. 0. 0.]
 [0. 0. 0.]]


Example 2
---------

b = np.zeros((4, 3))
print(b)

Output
------

[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]



3️⃣ np.random.random()
======================

Definition (Interview Friendly)
-------------------------------

np.random.random() is used to create an array filled with random
numbers between 0 and 1.


lll Syntax
-----------

np.random.random(shape)


Example 1
---------

c = np.random.random((2, 3))
print(c)

Example Output
--------------

[[0.46591611 0.16022309 0.16493077]
 [0.04637306 0.71743148 0.36342391]]


Example 2
---------

c = np.random.random((3, 2))
print(c)

Example Output
--------------

[[0.79392437 0.36191602]
 [0.99344198 0.67920164]
 [0.81194107 0.76044937]]



⭐ Important Points
==================

• np.ones() creates an array filled with 1  
• np.zeros() creates an array filled with 0  
• np.random.random() generates random values between 0 and 1  
• These functions require the shape as a tuple (rows, columns)  
• These methods are commonly used for initialization in data analysis and machine learning



⭐ Interview Quick Summary
==========================

lll np.ones()  → create array filled with 1  
lll np.zeros() → create array filled with 0  
lll np.random.random() → create array with random numbers between 0 and 1


"""