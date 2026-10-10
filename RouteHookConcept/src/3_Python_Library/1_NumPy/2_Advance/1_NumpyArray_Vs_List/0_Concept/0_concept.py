"""

NUMPY ARRAY VS PYTHON LIST
==========================

NumPy arrays and Python lists are both used to store data,
but NumPy arrays are more efficient for numerical operations.

Main Differences
----------------

1. Speed
2. Memory Usage
3. Convenience



1️⃣ Speed
=========

NumPy arrays are faster than Python lists because
NumPy operations are implemented in optimized C code.

Example
-------

import numpy as np

a = np.arange(1000000)

b = a * 2   # very fast with NumPy



Python list operations are slower because they
use loops internally.



2️⃣ Memory Usage
================

NumPy arrays consume less memory compared to Python lists.

Reason
------

Python lists store references to objects,
while NumPy arrays store elements in a
continuous memory block.



3️⃣ Convenience
===============

NumPy makes mathematical operations easier.

Example with NumPy
------------------

import numpy as np

a = np.array([1,2,3,4])

print(a * 2)

# [2 4 6 8]



Example with Python List
------------------------

a = [1,2,3,4]

# We need a loop
result = []

for i in a:
    result.append(i*2)

print(result)

# [2,4,6,8]



⭐ Important Points
==================

• NumPy arrays are faster than Python lists  
• NumPy arrays use less memory  
• Mathematical operations are easier in NumPy  
• NumPy supports vectorized operations  



⭐ Interview Definition
======================

NumPy arrays are more efficient than Python lists
because they provide faster computation, lower
memory usage, and easier mathematical operations.

"""