"""

lll CREATING NUMPY ARRAY USING LINSPACE
=======================================

Import NumPy
------------

import numpy as np



1️⃣ np.linspace()
=================

Definition (Interview Friendly)
-------------------------------

np.linspace() is used to generate evenly spaced numbers between
two specified values.

Unlike np.arange(), it generates a fixed number of values
between the start and end range.


lll Syntax
-----------

np.linspace(start, stop, num)

It is contain tree argument
first argument indicate → starting value that is included
Second argument indicate  → ending value that is also included
third argument indicate   → number of values to generate



Example 1
---------

a = np.linspace(-10, 10, 10)
print(a)

Output
------

[-10.          -7.77777778  -5.55555556  -3.33333333  -1.11111111
   1.11111111   3.33333333   5.55555556   7.77777778  10.        ]



Example 2
---------

a = np.linspace(5, 10, 6)
print(a)

Output
------

[ 5.  6.  7.  8.  9. 10.]



⭐ Important Points
==================

• np.linspace() generates evenly spaced numbers
• Start and stop values are included
• The third argument specifies the number of elements
• Useful when we need a fixed number of points
• Often used in plotting graphs and numerical analysis



⭐ Difference Between arange() and linspace()
=============================================

np.arange()

• Uses step size
• Stop value is NOT included
• Example → np.arange(1,10,2)


np.linspace()

• Uses number of elements
• Stop value is included
• Example → np.linspace(1,10,5)



⭐ Interview Quick Definition
=============================

np.linspace() is a NumPy function used to generate evenly spaced
numbers between a start and end value based on a specified number
of elements.


"""