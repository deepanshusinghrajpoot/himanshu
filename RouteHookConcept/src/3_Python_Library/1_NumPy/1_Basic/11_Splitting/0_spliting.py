"""

NUMPY SPLITTING
===============

Import NumPy
------------

import numpy as np



1️⃣ Splitting in NumPy
=====================

Splitting is used to divide a NumPy array into multiple
smaller arrays.

There are two common ways:

1. Horizontal Splitting
2. Vertical Splitting



Create Array
------------

a1 = np.arange(12).reshape(2,6)

print(a1)

# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]]



2️⃣ Horizontal Splitting (hsplit)
=================================

np.hsplit() splits an array **column-wise**.

Example
-------

b = np.hsplit(a1, 3)
print(b)

# [array([[0, 1],
#         [6, 7]]),
#
#  array([[2, 3],
#         [8, 9]]),
#
#  array([[ 4,  5],
#         [10, 11]])]



Explanation
-----------

Original shape → (2 × 6)

After split into 3 parts → each part becomes (2 × 2)



3️⃣ Vertical Splitting (vsplit)
===============================

np.vsplit() splits an array **row-wise**.

Example
-------

b = np.vsplit(a1, 2)
print(b)

# [array([[0, 1, 2, 3, 4, 5]]),
#  array([[ 6,  7,  8,  9, 10, 11]])]



Explanation
-----------

Original shape → (2 × 6)

After split into 2 parts → each part becomes (1 × 6)



⭐ Important Points
==================

• Splitting divides arrays into multiple parts  
• np.hsplit() splits arrays horizontally (column-wise)  
• np.vsplit() splits arrays vertically (row-wise)  
• Arrays must be divisible according to the number of splits  



⭐ Interview Definition
======================

Splitting in NumPy is the process of dividing an array
into multiple smaller arrays either horizontally
or vertically.

"""