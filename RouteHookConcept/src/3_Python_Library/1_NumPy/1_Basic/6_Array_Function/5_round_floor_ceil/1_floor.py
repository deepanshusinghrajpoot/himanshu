"""

NUMPY FLOOR FUNCTION
====================

Import NumPy
------------

import numpy as np



Create Random Array
-------------------

a = np.random.random((3,4)) * 100
print(a)

# [[79.48133002  6.84653763 29.60951519 50.71233211]
#  [71.23290262 52.9817514  19.07025171 77.00524632]
#  [18.29809717 58.40403796 76.93952839 36.66264004]]



1️⃣ NumPy Floor Function
========================

np.floor() returns the **largest integer less than or equal to**
each element in the array.

It works element-wise on the array.



Example
-------

print(np.floor(a))

# [[79.  6. 29. 50.]
#  [71. 52. 19. 77.]
#  [18. 58. 76. 36.]]



Explanation
-----------

Each decimal value is rounded **down** to the nearest integer.

Example:

79.48 → 79  
6.84  → 6  
29.60 → 29  
50.71 → 50  



Difference Between Round and Floor
==================================

np.round() → rounds to the nearest integer  
np.floor() → always rounds **down**  
np.ceil()  → always rounds **up**



Example
-------

print(np.ceil(a))



⭐ Important Points
==================

• np.floor() always returns the lower integer value  
• Operation is applied element-wise  
• Commonly used in mathematical computations and data processing  



⭐ Interview Definition
======================

np.floor() is a NumPy function that returns the largest
integer less than or equal to each element of an array.

"""