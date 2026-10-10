"""

NUMPY INDEXING
==============

Import NumPy
------------

import numpy as np



Create Arrays
-------------

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)



1️⃣ Indexing in 1D Array
========================

print(a1)

# [0 1 2 3 4 5 6 7 8 9]



Access Elements
---------------

print(a1[0])   # first element
print(a1[-1])  # last element
print(a1[1])   # second element


# 0
# 9
# 1



Explanation
-----------

In a 1D array, we access elements using a single index.

Index starts from 0.



2️⃣ Indexing in 2D Array
========================

print(a2)

# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]



Access Elements
---------------

print(a2[1,2])  # row = 1, column = 2
print(a2[2,3])  # row = 2, column = 3
print(a2[0,0])  # row = 0, column = 0


# 6
# 11
# 0



Explanation
-----------

For 2D arrays we use:

array[row_index, column_index]

Row index → horizontal position  
Column index → vertical position



3️⃣ Indexing in 3D Array
========================

print(a3)

# [[[0 1]
#   [2 3]]
#
#  [[4 5]
#   [6 7]]]



Access Elements
---------------

print(a3[0,0,1])
print(a3[1,0,1])
print(a3[1,1,0])


# 1
# 5
# 6



Explanation
-----------

For 3D arrays we use:

array[depth, row, column]

Depth → which 2D matrix  
Row → row inside the matrix  
Column → column inside the matrix



⭐ Important Points
==================

• Indexing is used to access specific elements of an array  
• Index starts from 0  
• Negative indexing accesses elements from the end  
• For multidimensional arrays we use multiple indices



⭐ Interview Definition
======================

Indexing in NumPy is used to access specific elements of an array
using their position or index.



"""