"""

NUMPY CEIL FUNCTION
===================

Import NumPy
------------

import numpy as np



Create Random Array
-------------------

a = np.random.random((3,4)) * 100
print(a)

# [[95.22645176  8.63160901 93.39623201 99.40014727]
#  [13.50924262 43.28320554 36.4093691  92.59138348]
#  [75.22974442 96.13656122 14.78703849 45.66386847]]



1️⃣ NumPy Ceil Function
======================

np.ceil() returns the **smallest integer greater than or equal to**
each element in the array.

The operation is applied **element-wise**.



Example
-------

print(np.ceil(a))

# [[ 96.   9.  94. 100.]
#  [ 14.  44.  37.  93.]
#  [ 76.  97.  15.  46.]]



Explanation
-----------

Each decimal value is rounded **up** to the nearest integer.

Example:

95.22 → 96  
8.63  → 9  
93.39 → 94  
99.40 → 100  



Difference Between Round, Floor, and Ceil
=========================================

np.round() → rounds to the nearest integer  

np.floor() → always rounds **down**  

np.ceil()  → always rounds **up**  



Example
-------

print(np.round(a))
print(np.floor(a))
print(np.ceil(a))



⭐ Important Points
==================

• np.ceil() always returns the upper integer value  
• Operation is applied element-wise  
• Useful in mathematical and numerical computations  



⭐ Interview Definition
======================

np.ceil() is a NumPy function that returns the smallest
integer greater than or equal to each element of an array.

"""