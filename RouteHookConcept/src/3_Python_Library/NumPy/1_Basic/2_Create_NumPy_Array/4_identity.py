"""

lll CREATING NUMPY ARRAY USING IDENTITY METHOD
==============================================

Import NumPy
------------

import numpy as np



1️⃣ np.identity()
=================

Definition (Interview Friendly)
-------------------------------

np.identity() is used to create an identity matrix.

An identity matrix is a square matrix in which all diagonal
elements are 1 and all other elements are 0.


Example of Identity Matrix (3×3)

1 0 0
0 1 0
0 0 1



lll Syntax
----------

np.identity(n)

n → number of rows and columns (square matrix)



Example 1
---------

a = np.identity(3)

print(a)

Output
------

[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]



Example 2
---------

a = np.identity(4)

print(a)

Output
------

[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]



⭐ Important Points
==================

• Identity matrix is always a square matrix
• Diagonal elements are always 1
• Non-diagonal elements are always 0
• Commonly used in linear algebra
• Important in machine learning and matrix operations



⭐ Interview Quick Definition
=============================

np.identity() is a NumPy function used to create a square identity
matrix where diagonal elements are 1 and all other elements are 0.



⭐ Related Function
==================

np.eye()

It also creates an identity-like matrix but allows more flexibility
such as specifying rows and columns separately.


"""