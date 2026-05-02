"""

NUMPY REVISION NOTES (DATA ANALYST + INTERVIEW)
===============================================


1️⃣ What is NumPy
=================

lll NumPy (Numerical Python) is the fundamental Python library used for scientific computing.

lll It provides a powerful multidimensional array object called ndarray and many
    functions to perform fast numerical operations.

These operations include:

• Mathematical calculations
• Logical operations
• Array shape manipulation
• Sorting and filtering
• Linear algebra
• Statistical operations
• Random number generation
• Fourier transforms


Core Concept
------------

lll The core of NumPy is the ndarray (N-dimensional array).

lll An ndarray stores homogeneous data (same data type) in a fixed-size and
    efficient structure.


Example
-------
 
import numpy as np

arr = np.array([10, 20, 30])
print(arr)

Output:
[10 20 30]



2️⃣ Why Use NumPy Instead of Python Lists
=============================================

Python built-in data structures like:

list, tuple, set, dictionary

are not optimized for heavy numerical computations.

NumPy solves this problem.


Main Idea
---------

lll NumPy is written in C language but used with Python syntax.

So we get:

• Speed from C
• Simplicity from Python




This makes numerical computations much faster than Python loops.


Example
-------

import numpy as np

a = np.array([1, 2, 3])

print(a * 2)

Output:
[2 4 6]

The multiplication happens element-wise without using loops.



3️⃣ Why NumPy is Important in Data Science
==============================================

NumPy is the foundation of the Python data science ecosystem.

lll We are also know that
    Many popular libraries are built on top of NumPy:

• Pandas      -> Data analysis
• Matplotlib  -> Data visualization
• Seaborn     -> Statistical visualization
• Scikit-learn -> Machine learning
• TensorFlow / PyTorch -> Deep learning
• NLTK / SpaCy -> Natural language processing

These libraries internally use NumPy arrays.

Therefore, NumPy is considered the backbone of Data Science in Python.



4️⃣ NumPy Arrays vs Python Lists
================================

Feature              NumPy Array                 Python List
----------------------------------------------------------------
Size                 Fixed size                  Dynamic size
Data Type            Same type only              Multiple types
Performance          Very fast                   Slower
Memory Usage         Efficient                   More memory
Math Operations      Vectorized                  Requires loops



Example
-------

Python List

a = [1, 2, 3]
result = [i * 2 for i in a]


NumPy Array

import numpy as np

a = np.array([1, 2, 3])
print(a * 2)



5️⃣ Important Properties of NumPy Arrays
========================================

NumPy arrays provide several useful attributes.


Attribute        Meaning
----------------------------------
ndim             Number of dimensions
shape            Size of array
size             Total number of elements
dtype            Data type of elements


Example
-------

import numpy as np

a = np.array([[1, 2], [3, 4]])

print(a.shape)
print(a.ndim)
print(a.size)

Output:

(2, 2)
2
4



⭐ Interview Friendly Definition
=================================

NumPy is a Python library used for fast numerical computing using
multidimensional arrays and vectorized operations.



⭐ Key Revision Points
=======================

• NumPy stands for Numerical Python
• Core object is ndarray
• Stores homogeneous data
• Faster than Python lists
• Supports vectorized operations
• Written in C but used with Python syntax
• Backbone of Data Science libraries


"""