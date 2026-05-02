"""

NUMPY STATISTICAL FUNCTIONS
===========================

Import NumPy
------------

import numpy as np



Create Random Array
-------------------

a1 = np.random.random((3,3))
print(a1)

# [[0.71784455 0.4423148  0.69608817]
#  [0.37596665 0.65152445 0.5799981 ]
#  [0.59651534 0.3789232  0.51824972]]



Convert Values to Larger Numbers
--------------------------------

a1 = np.round(a1 * 100)
print(a1)

# [[72. 44. 70.]
#  [38. 65. 58.]
#  [60. 38. 52.]]



1️⃣ NumPy Statistical Functions
===============================

Statistical functions help analyze the distribution of data
inside a NumPy array.



Mean (Average Value)
--------------------

print(np.mean(a1))



Median (Middle Value)
---------------------

print(np.median(a1))



Standard Deviation
------------------

print(np.std(a1))



Variance
--------

print(np.var(a1))


# 55.22222222222222
# 58.0
# 12.272623352430289
# 150.61728395061726



lll Explanation
---------------

Mean
Average of all elements.

Median
Middle element after sorting the data.

Standard Deviation
Shows how much the data deviates from the mean.

Variance
Square of the standard deviation.



2️⃣ Row-wise and Column-wise Statistics
=======================================

We can calculate statistics for specific rows
or specific columns using the "axis" parameter.



Axis Explanation
----------------

axis = 0 → Column-wise operation  
axis = 1 → Row-wise operation  



Column-wise Operations
======================

print(np.mean(a1, axis=0))
print(np.median(a1, axis=0))
print(np.std(a1, axis=0))
print(np.var(a1, axis=0))


# [56.66666667 49.         60.        ]
# [60. 44. 58.]
# [14.07914139 11.5758369   7.48331477]
# [198.22222222 134.          56.        ]



Row-wise Operations
===================

print(np.mean(a1, axis=1))
print(np.median(a1, axis=1))
print(np.std(a1, axis=1))
print(np.var(a1, axis=1))


# [62.         53.66666667 50.        ]
# [70. 58. 52.]
# [12.75408431 11.4406682   9.09212113]
# [162.66666667 130.88888889  82.66666667]



⭐ Important Points
==================

• Statistical functions help summarize data  
• Mean gives the average value  
• Median gives the middle value  
• Standard deviation measures spread of data  
• Variance is the square of standard deviation  
• axis=0 performs column-wise operations  
• axis=1 performs row-wise operations  



⭐ Interview Definition
======================

NumPy statistical functions are used to calculate descriptive
statistics such as mean, median, variance, and standard deviation
from array data.

"""




