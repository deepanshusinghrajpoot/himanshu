"""

NUMPY RESHAPE
=============

Import NumPy
------------

import numpy as np



Create Array
------------

a1 = np.arange(12)
print(a1)

# [0 1 2 3 4 5 6 7 8 9 10 11]



1️⃣ Reshape Function
====================

reshape() is used to change the shape (dimensions)
of a NumPy array without changing the data.



Example
-------

a1 = np.arange(12).reshape(3,4)
print(a1)

# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]



Explanation
-----------

Total elements must remain the same.

Here we have 12 elements.

Possible shapes:

12 × 1  
6 × 2  
4 × 3  
3 × 4  
2 × 6  
1 × 12



More Examples
-------------

print(np.arange(12).reshape(4,3))

# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]


print(np.arange(12).reshape(2,6))

# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]]



Automatic Dimension (-1)
------------------------

NumPy can automatically calculate one dimension.

print(np.arange(12).reshape(3,-1))

# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]



⭐ Important Points
==================

• reshape() changes the shape of an array  
• Total number of elements must remain the same  
• reshape does not change the data  
• -1 lets NumPy automatically calculate the dimension  



⭐ Interview Definition
======================

reshape() is a NumPy function used to change the
shape of an array while keeping the same data
and total number of elements.

"""