"""

NUMPY STACKING
==============

Import NumPy
------------

import numpy as np



1️⃣ Stacking in NumPy
=====================

Stacking is used to combine multiple NumPy arrays
into a single array.

Arrays must have **compatible shapes** for stacking.

There are two common types:

1. Horizontal Stacking
2. Vertical Stacking



Create Arrays
-------------

a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)

print(a1)

# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a2)

# [[12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]]



2️⃣ Horizontal Stacking (hstack)
================================

np.hstack() joins arrays **column-wise**.

Number of rows must be the same.



Example
-------

b = np.hstack((a1, a2))
print(b)

# [[ 0  1  2  3 12 13 14 15]
#  [ 4  5  6  7 16 17 18 19]
#  [ 8  9 10 11 20 21 22 23]]



Explanation
-----------

Shape of a1 → (3 × 4)  
Shape of a2 → (3 × 4)

After stacking → (3 × 8)



3️⃣ Vertical Stacking (vstack)
==============================

np.vstack() joins arrays **row-wise**.

Number of columns must be the same.



Example
-------

b = np.vstack((a1, a2))
print(b)

# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]]



Explanation
-----------

Shape of a1 → (3 × 4)  
Shape of a2 → (3 × 4)

After stacking → (6 × 4)



⭐ Important Points
==================

• Stacking combines multiple arrays  
• np.hstack() joins arrays horizontally (column-wise)  
• np.vstack() joins arrays vertically (row-wise)  
• Arrays must have compatible shapes  



⭐ Interview Definition
======================

Stacking in NumPy is the process of combining
multiple arrays into a single array either
horizontally or vertically.

"""