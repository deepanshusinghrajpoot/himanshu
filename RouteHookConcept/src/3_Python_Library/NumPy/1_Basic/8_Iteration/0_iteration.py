"""

NUMPY ARRAY ITERATION
=====================

Import NumPy
------------

import numpy as np



Create Arrays
-------------

a1 = np.arange(9)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(27).reshape(3,3,3)



1️⃣ Iterating Over 1D Array
===========================

print(a1)

# [0 1 2 3 4 5 6 7 8]

for item in a1:
    print(item, end=" ")

print()

# Output
# 0 1 2 3 4 5 6 7 8



Explanation
-----------

In a 1D array, each iteration directly returns an element.



2️⃣ Iterating Over 2D Array
===========================

print(a2)

# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

for row in a2:
    for col in row:
        print(col, end=" ")

print()

# Output
# 0 1 2 3 4 5 6 7 8 9 10 11



Explanation
-----------

First loop → iterates rows  
Second loop → iterates elements inside each row  



3️⃣ Iterating Over 3D Array
===========================

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

for i in a3:
    for j in i:
        for k in j:
            print(k, end=" ")

print()

# Output
# 0 1 2 3 4 5 6 7 8 9 10 11 12 ... 26



Explanation
-----------

3D arrays require three loops:

1st loop → matrix  
2nd loop → row  
3rd loop → column  



4️⃣ NumPy nditer()
==================

np.nditer() is a NumPy function used to iterate
through all elements of an array regardless
of its dimension.



Example with 2D Array
---------------------

for i in np.nditer(a2):
    print(i, end=" ")

print()

# 0 1 2 3 4 5 6 7 8 9 10 11



Example with 3D Array
---------------------

for i in np.nditer(a3):
    print(i, end=" ")

print()

# 0 1 2 3 4 5 6 ... 26



Explanation
-----------

np.nditer() converts an N-dimensional array
into a flat iteration sequence.



⭐ Important Points
==================

• Arrays can be iterated using Python loops  
• Higher dimensional arrays require nested loops  
• np.nditer() simplifies iteration for multi-dimensional arrays  
• nditer works for arrays of any dimension  



⭐ Interview Definition
======================

Array iteration in NumPy is the process of accessing
each element of an array sequentially. The np.nditer()
function allows efficient iteration over multi-dimensional arrays.

"""