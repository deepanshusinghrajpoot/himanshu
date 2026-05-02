import numpy as np


# Broadcasting
# ============

# Broadcasting describes how NumPy performs arithmetic
# operations on arrays with different shapes.

# The smaller array is "broadcast" across the larger array
# so that they become compatible for operations.



# Case 1: Same Shape Arrays
# -------------------------

a = np.arange(6).reshape(2, 3)
b = np.arange(6, 12).reshape(2, 3)

print(a)
# [[0 1 2]
#  [3 4 5]]

print(b)
# [[ 6  7  8]
#  [ 9 10 11]]

# Element-wise addition
print(a + b)

# [[ 6  8 10]
#  [12 14 16]]



# Case 2: Different Shape Arrays
# ------------------------------

m = np.arange(6).reshape(2, 3)
n = np.arange(3).reshape(1, 3)

print(m)
# [[0 1 2]
#  [3 4 5]]

print(n)
# [[0 1 2]]

# Broadcasting happens here
print(m + n)

# [[0 2 4]
#  [3 5 7]]