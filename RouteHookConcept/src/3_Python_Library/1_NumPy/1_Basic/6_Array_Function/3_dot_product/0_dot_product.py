"""

NUMPY DOT PRODUCT (MATRIX MULTIPLICATION)
=========================================

Import NumPy
------------

import numpy as np



Create Two Matrices
-------------------

a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(4,3)

print(a1)

# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a2)

# [[12 13 14]
#  [15 16 17]
#  [18 19 20]
#  [21 22 23]]



1️⃣ Dot Product
===============

lll Dot product is a matrix multiplication operation
    performed between two numpy arrays.



Conditions for Dot Product
==========================

If we have two matrices:

Matrix A → (n × m)  
Matrix B → (p × q)

Condition
---------

Dot product is possible only when:

m = p



Result Shape
------------

The resulting matrix will have the shape:

(n × q)



Formula of Dot Product
======================

For matrices A and B:

C[i][j] = A[i][0]*B[0][j] +
          A[i][1]*B[1][j] +
          A[i][2]*B[2][j] + ...



Example Using NumPy
===================

print(np.dot(a1, a2))

# [[114 120 126]
#  [378 400 422]
#  [642 680 718]]



Explanation
-----------

Each row of matrix a1 is multiplied
with each column of matrix a2.



Example Calculation
-------------------

First element:

(0×12) + (1×15) + (2×18) + (3×21)

= 0 + 15 + 36 + 63

= 114



Alternative Method
==================

Matrix multiplication can also be done using:

print(a1 @ a2)



⭐ Important Points
==================

• Dot product performs matrix multiplication  
• Inner dimensions must match (m = p)  
• Result matrix shape = (n × q)  
• Commonly used in machine learning and linear algebra  



⭐ Interview Definition
======================

The dot product in NumPy is a matrix multiplication
operation where the inner dimensions of two matrices
must match, and the result is computed by multiplying
rows of the first matrix with columns of the second matrix.

"""