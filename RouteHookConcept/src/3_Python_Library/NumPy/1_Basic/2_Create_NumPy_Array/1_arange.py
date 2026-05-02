"""

lll CREATING NUMPY ARRAY USING ARANGE AND RESHAPE METHOD
========================================================

Import NumPy
------------

import numpy as np



1️⃣ np.arange()
================

Definition (Interview Friendly)
-------------------------------

np.arange() is used to create a NumPy array with evenly spaced values 
within a specified range.

It works similar to Python's built-in range() function, but it returns
a NumPy array instead of a list.


lll Syntax
----------

np.arange(start, stop, step)

It is contain three argument
first argument indicate → starting value that is included
Second argument indicate  → ending value that is excluded
third argument indicate   → difference between consecutive numbers


Example 1
---------

a = np.arange(1, 11, 2)
print(a)

Output
------

[1 3 5 7 9]


Example 2
---------

a = np.arange(-11, 0, 2)
print(a)

Output
------

[-11  -9  -7  -5  -3  -1]


Important Points
----------------

• Works similar to Python range()
• Stop value is NOT included
• Returns a NumPy array
• Commonly used for creating sequences of numbers
• Frequently used in data analysis and simulations



2️⃣ reshape()
=============

Definition (Interview Friendly)
-------------------------------

reshape() is used to change the shape (dimensions) of a NumPy array 
without changing its data.

It reorganizes the elements into rows and columns.


Syntax
------

array.reshape(rows, columns)

It is contain two argument
first argument indicate → number of row
Second argument indicate  → number of column


Important Rule
--------------
Total elements must remain the same.


Example:
12 elements → can reshape into

3 × 4  
4 × 3  
6 × 2  


Example 1
---------

b = np.arange(1, 13).reshape(3, 4)

print(b)

Output
------

[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]



Example 2
---------

b = np.arange(1, 13).reshape(4, 3)

print(b)

Output
------

[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]



Example 3
---------

b = np.arange(1, 13).reshape(6, 2)

print(b)

Output
------

[[ 1  2]
 [ 3  4]
 [ 5  6]
 [ 7  8]
 [ 9 10]
 [11 12]]



⭐ Interview Important Points
=============================

• np.arange() creates arrays with evenly spaced values
• reshape() changes the structure of an array
• reshape does NOT change the total number of elements
• Total elements = rows × columns must remain equal
• reshape is widely used in machine learning and data preprocessing


"""