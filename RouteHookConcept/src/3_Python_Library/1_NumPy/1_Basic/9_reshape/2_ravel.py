"""

NUMPY RAVEL
===========

Import NumPy
------------

import numpy as np



Create Array
------------

a = np.arange(12).reshape(4,3)
print(a)

# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]



1️⃣ ravel() Function
====================

np.ravel() is used to convert a multi-dimensional
array into a 1D array.

It flattens the array while keeping the same data.



Example
-------

b = np.ravel(a)
print(b)

# [ 0  1  2  3  4  5  6  7  8  9 10 11]



Explanation
-----------

Original Shape → (4 × 3)

After ravel() → (12,)

All elements are placed into a single row.



Alternative Method
------------------

We can also use:

print(a.ravel())



Difference Between ravel() and flatten()
========================================

ravel()

• Returns a view of the original array  
• Faster and memory efficient  


flatten()

• Returns a copy of the array  
• Changes do not affect the original array  



Example
-------

print(a.flatten())



⭐ Important Points
==================

• ravel() converts N-dimensional arrays into 1D arrays  
• The number of elements remains the same  
• ravel() returns a view of the original array  
• flatten() returns a copy  



⭐ Interview Definition
======================

np.ravel() is a NumPy function used to flatten a
multi-dimensional array into a one-dimensional array.

"""