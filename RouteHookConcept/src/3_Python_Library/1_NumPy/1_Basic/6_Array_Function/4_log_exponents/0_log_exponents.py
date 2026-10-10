"""

NUMPY LOGARITHMIC AND EXPONENTIAL FUNCTIONS
===========================================

Import NumPy
------------

import numpy as np



Create Array
------------

a = np.arange(12, 24).reshape(3,4)
print(a)

# [[12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]]



1️⃣ Logarithmic Function
========================

NumPy provides logarithmic functions that operate
element-wise on array values.

np.log() calculates the **natural logarithm (base e)**.



Example
-------

b = np.log(a)

print(b)

# [[2.48490665 2.56494936 2.63905733 2.7080502 ]
#  [2.77258872 2.83321334 2.89037176 2.94443898]
#  [2.99573227 3.04452244 3.09104245 3.13549422]]



Explanation
-----------

The natural logarithm is calculated for each
element of the array.



Other Logarithmic Functions
===========================

Base 10 Logarithm

print(np.log10(a))

Base 2 Logarithm

print(np.log2(a))



2️⃣ Exponential Function
========================

np.exp() calculates the exponential value:

e^x  (where e ≈ 2.718)



Example
-------

b = np.exp(a)

print(b)

# [[1.62754791e+05 4.42413392e+05 1.20260428e+06 3.26901737e+06]
#  [8.88611052e+06 2.41549528e+07 6.56599691e+07 1.78482301e+08]
#  [4.85165195e+08 1.31881573e+09 3.58491285e+09 9.74480345e+09]]



Explanation
-----------

Each element is used as the exponent of e.

Example:

exp(12) = e^12  
exp(13) = e^13  



⭐ Important Points
==================

• Logarithmic and exponential functions operate element-wise  
• np.log() calculates natural logarithm (base e)  
• np.log10() calculates base 10 logarithm  
• np.exp() calculates e raised to the power of x  
• These functions are widely used in scientific computing,
  probability, and machine learning  



⭐ Interview Definition
======================

NumPy logarithmic and exponential functions are used to
compute log and exponential values of array elements
in an element-wise manner.



"""