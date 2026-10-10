"""

NUMPY ROUND FUNCTION
====================

Import NumPy
------------

import numpy as np



Create Random Array
-------------------

a = np.random.random((3,4)) * 100
print(a)

# [[ 9.33533001 90.40754085 90.96596428 54.52208479]
#  [59.24282997 57.96265227 20.2291623  35.12527506]
#  [99.13721999 97.51871327 97.79781569  9.34037616]]



1️⃣ NumPy Round Function
========================

np.round() is used to round the values of array elements.

It works element-wise on the array.



Example
-------

print(np.round(a))

# [[ 9. 90. 91. 55.]
#  [59. 58. 20. 35.]
#  [99. 98. 98.  9.]]



Explanation
-----------

Each value in the array is rounded to the nearest integer.

Example:

9.33  →  9  
90.40 → 90  
90.96 → 91  



2️⃣ Round to Specific Decimal Places
====================================

We can also round numbers to a specific number
of decimal places.

Syntax
------

np.round(array, decimals)



Example
-------

print(np.round(a, 2))



⭐ Important Points
==================

• np.round() rounds array elements to the nearest value  
• Operation is applied element-wise  
• decimals parameter controls the precision  
• Commonly used in data cleaning and result formatting  



⭐ Interview Definition
======================

np.round() is a NumPy function used to round the
elements of an array to the nearest integer or
specified number of decimal places.

"""