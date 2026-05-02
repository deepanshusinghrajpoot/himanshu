"""

NUMPY TRANSPOSE
===============

Import NumPy
------------

import numpy as np



Create Array
------------

a = np.arange(12).reshape(3,4)
print(a)

# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]



1️⃣ Transpose Function
======================

Transpose converts **rows into columns**
and **columns into rows**.

In simple terms, it flips the matrix
over its diagonal.



Using np.transpose()
--------------------

a = np.transpose(a)
print(a)

# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]



Explanation
-----------

Original Shape → (3 × 4)

After Transpose → (4 × 3)

Rows become columns and columns become rows.



2️⃣ Using .T Attribute
======================

NumPy also provides a shortcut for transpose.

a = a.T
print(a)

# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]



Explanation
-----------

.T is a shorthand attribute
that performs the transpose operation.



⭐ Important Points
==================

• Transpose swaps rows and columns  
• Shape changes from (n × m) → (m × n)  
• np.transpose() and .T perform the same operation  
• Commonly used in linear algebra and machine learning  



⭐ Interview Definition
======================

Transpose in NumPy is an operation that swaps
the rows and columns of a matrix, converting
an array of shape (n × m) into (m × n).

"""