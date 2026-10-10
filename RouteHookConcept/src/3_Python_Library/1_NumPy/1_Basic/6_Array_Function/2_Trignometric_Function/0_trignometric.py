"""

NUMPY TRIGONOMETRIC FUNCTIONS
==============================

Import NumPy
------------

import numpy as np



Create Random Array
-------------------

a1 = np.random.random((3,3))
print(a1)

# [[0.70967957 0.39609203 0.90612566]
#  [0.49092346 0.77692045 0.85468796]
#  [0.44305515 0.81291122 0.87472664]]



Convert Values to Larger Numbers
--------------------------------

a1 = np.round(a1 * 100)
print(a1)

# [[71. 40. 91.]
#  [49. 78. 85.]
#  [44. 81. 87.]]



1️⃣ NumPy Trigonometric Functions
=================================

NumPy provides mathematical trigonometric functions
that operate element-wise on arrays.

These functions are mainly used in:

• scientific computing  
• physics simulations  
• signal processing  
• engineering calculations  

They are **less commonly used in data science**.



Example : Sine Function
-----------------------

print(np.sin(a1))

# [[ 0.95105465  0.74511316  0.10598751]
#  [-0.95375265  0.51397846 -0.17607562]
#  [ 0.01770193 -0.62988799 -0.82181784]]



Explanation
-----------

The sine function is applied to each element
of the array individually.



Other Trigonometric Functions
=============================

Cosine
------

print(np.cos(a1))


Tangent
-------

print(np.tan(a1))


Inverse Sine
------------

print(np.arcsin(a1))


Inverse Cosine
--------------

print(np.arccos(a1))


Inverse Tangent
---------------

print(np.arctan(a1))



⭐ Important Points
==================

• Trigonometric functions operate element-wise  
• They return values based on mathematical trigonometry  
• Used mostly in scientific and engineering calculations  
• Not commonly used in everyday data analysis  



⭐ Interview Definition
======================

NumPy trigonometric functions perform mathematical
trigonometry operations such as sine, cosine, and tangent
on array elements in an element-wise manner.




The Six Functions:
Sine (sin): Opposite / Hypotenuse.
Cosine (cos): Adjacent / Hypotenuse.
Tangent (tan): Opposite / Adjacent.
Cosecant (csc or cosec): Hypotenuse / Opposite (1/sin).
Secant (sec): Hypotenuse / Adjacent (1/cos).
Cotangent (cot): Adjacent / Opposite (1/tan).

"""


import numpy as np

