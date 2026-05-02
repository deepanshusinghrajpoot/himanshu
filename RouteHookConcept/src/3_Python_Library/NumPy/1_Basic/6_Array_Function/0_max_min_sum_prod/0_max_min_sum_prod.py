"""

NUMPY AGGREGATION FUNCTIONS
===========================

Import NumPy
------------

import numpy as np



Create Random Array
-------------------

a1 = np.random.random((3,3))
print(a1)

# [[0.86684959 0.93209737 0.53606197]
#  [0.60246088 0.57411336 0.63163597]
#  [0.47007492 0.68021172 0.19729166]]



Convert Values to Bigger Numbers
--------------------------------

a1 = np.round(a1 * 100)
print(a1)

# [[87. 93. 54.]
#  [60. 57. 63.]
#  [47. 68. 20.]]



1️⃣ NumPy Aggregation Functions
================================

Aggregation functions perform calculations on multiple
array elements and return a single summarized value.



Common Aggregation Functions
============================

Maximum Value
-------------

print(np.max(a1))

Minimum Value
-------------

print(np.min(a1))

Sum of All Elements
-------------------

print(np.sum(a1))

Product of All Elements
-----------------------

print(np.prod(a1))


# 93.0
# 20.0
# 549.0
# 6017268388924800.0



2️⃣ lll If we want to Row-wise and Column-wise Operations
=========================================================

Sometimes we want calculations for specific rows
or specific columns.

This is done using the "axis" parameter.



Axis Explanation
----------------

lll Then we are use axis parameter
    axis = 0 → Mean Column-wise operation  
    axis = 1 → Mean Row-wise operation



Column-wise Operations
======================

print(np.max(a1, axis=0))
print(np.min(a1, axis=0))
print(np.sum(a1, axis=0))
print(np.prod(a1, axis=0))


# [87. 93. 63.]
# [47. 57. 20.]
# [194. 218. 137.]
# [245340. 360468.  68040.]



Row-wise Operations
===================

print(np.max(a1, axis=1))
print(np.min(a1, axis=1))
print(np.sum(a1, axis=1))
print(np.prod(a1, axis=1))


# [93. 63. 68.]
# [54. 57. 20.]
# [234. 180. 135.]
# [436914. 215460.  63920.]



⭐ Important Points
==================

• Aggregation functions summarize array data  
• They return a single value or values along an axis  
• axis=0 performs column-wise operations  
• axis=1 performs row-wise operations  
• These functions are widely used in data analysis



⭐ Interview Definition
======================

Aggregation functions in NumPy perform mathematical
operations such as sum, maximum, minimum, or product
on array elements and return a summarized result.

"""