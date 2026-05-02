"""

NUMPY SLICING
=============

Import NumPy
------------

import numpy as np



Create Arrays
-------------

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(27).reshape(3,3,3)



1️⃣ Slicing in 1D Array
=======================

print(a1)

# [0 1 2 3 4 5 6 7 8 9]



Basic Slicing
-------------

print(a1[0:5])      # elements from index 0 to 4
print(a1[-1:-4:-1]) # reverse slice
print(a1[1:8])      # elements from index 1 to 7


# [0 1 2 3 4]
# [9 8 7]
# [1 2 3 4 5 6 7]



Slicing Syntax
--------------

array[start : stop : step]

start → starting index  
stop  → ending index (excluded)  
step  → jump between elements  



2️⃣ Slicing in 2D Array
=======================

print(a2)

# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]



Examples
--------

print(a2[1, :])      # row 1, all columns
print(a2[:, 3])      # all rows, column 3
print(a2[0, 1:4])    # row 0, columns 1 to 3
print(a2[1:, 1:])    # rows 1 to end, columns 1 to end
print(a2[::2, ::3])  # step slicing
print(a2[::2, 1::2])
print(a2[0:2, 1:])


# [4 5 6 7]
# [ 3  7 11]
# [1 2 3]
# [[ 5  6  7]
#  [ 9 10 11]]
# [[ 0  3]
#  [ 8 11]]
# [[ 1  3]
#  [ 9 11]]
# [[1 2 3]
#  [5 6 7]]



Explanation
-----------

a2[row_slice , column_slice]

Example:

a2[1:,1:]

Row → from index 1 onward  
Column → from index 1 onward  



3️⃣ Slicing in 3D Array
=======================

print(a3)

# [[[ 0  1  2]
#   [ 3  4  5]
#   [ 6  7  8]]

#  [[ 9 10 11]
#   [12 13 14]
#   [15 16 17]]

#  [[18 19 20]
#   [21 22 23]
#   [24 25 26]]]



Examples
--------

print(a3[::2, :, :])

# OR

print(a3[::2])

# [[[ 0  1  2]
#   [ 3  4  5]
#   [ 6  7  8]]

#  [[18 19 20]
#   [21 22 23]
#   [24 25 26]]]



Select Row From Specific Matrix
--------------------------------

print(a3[1,1,:])

# [12 13 14]



Step Slicing
------------

print(a3[::2, 0, ::2])

# [[ 0  2]
#  [18 20]]



⭐ Important Points
==================

• Slicing extracts a portion of an array  
• Syntax → array[start : stop : step]  
• Works for 1D, 2D, and higher dimensional arrays  
• Multiple indices are used for multidimensional arrays  



⭐ Interview Definition
======================

Slicing in NumPy is used to extract a subset of elements
from an array using start, stop, and step indices.

"""