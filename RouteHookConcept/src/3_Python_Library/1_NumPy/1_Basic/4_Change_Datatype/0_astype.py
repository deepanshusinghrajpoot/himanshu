"""

NUMPY TYPE CONVERSION (astype)
==============================

Import NumPy
------------

import numpy as np



1️⃣ astype()
============

Definition (Interview Friendly)
-------------------------------

lll astype() is used to change the data type of elements in a NumPy array.
    It creates a new array with the specified data type while keeping
    the original data unchanged.



Syntax
------

array.astype(new_dtype)



Example
-------

a = np.arange(10)

print(a)
# [0 1 2 3 4 5 6 7 8 9]

print(a.dtype)
# int64



Convert Data Type
-----------------

b = a.astype(np.int32)

print(b.dtype)
# int32



Important Concept
-----------------

astype() does NOT modify the original array.
It returns a new array with the new data type.



Example to Verify
-----------------

print(a.dtype)
# int64

print(b.dtype)
# int32



lll Common Data Type Conversions
==============================

np.int32   → 32-bit integer  
np.int64   → 64-bit integer  
np.float32 → 32-bit float  
np.float64 → 64-bit float  
np.bool_   → Boolean type  
np.str_    → String type  



Example (Integer to Float)
--------------------------

c = a.astype(float)

print(c)
# [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]



⭐ Important Points
==================

• astype() converts the data type of a NumPy array  
• It returns a new array and does not modify the original array  
• Useful in data preprocessing and machine learning  
• Often used when converting integers to float for calculations  



⭐ Interview Quick Definition
=============================

lll astype() is a NumPy method used to convert the data type of
    elements in an array and returns a new array with the specified type.


"""