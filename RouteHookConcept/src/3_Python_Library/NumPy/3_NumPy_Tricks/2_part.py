# ==========================================
# NumPy: Conditional & Extremum Functions
# ==========================================

import numpy as np

# ==========================================
# 1️⃣ np.where() – Conditional Indexing & Replacement
# ==========================================
# Returns indices where a condition is True
# Syntax: np.where(condition, value_if_true, value_if_false)

a = np.arange(40, 60)
print("Original array:", a)
# Original array: [40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59]

# Indices where values > 50
print("Indices where a > 50:", np.where(a > 50))
# Indices where a > 50: (array([11, 12, 13, 14, 15, 16, 17, 18, 19]),)

# Replace all values > 50 with 0
print("Replace values > 50 with 0:", np.where(a > 50, 0, a))
# [40 41 42 43 44 45 46 47 48 49 50  0  0  0  0  0  0  0  0  0]

# Replace all even elements with 0
print("Replace even elements with 0:", np.where(a % 2 == 0, 0, a))
# [ 0 41  0 43  0 45  0 47  0 49  0 51  0 53  0 55  0 57  0 59]

# ⚡ Quick Tips:
# - Use np.where() for conditional filtering or element-wise replacement
# - Can combine multiple conditions using & (and) or | (or)

# ==========================================
# 2️⃣ np.argmax() – Index of Maximum Value
# ==========================================
# Returns the index of the maximum value in an array
# Can specify axis for multidimensional arrays

print("Index of max in a:", np.argmax(a))
# 19

b = np.arange(12, 24).reshape(3, 4)
print("2D array b:\n", b)
# [[12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]]

print("Index of max along columns (axis=0):", np.argmax(b, axis=0))
# [2 2 2 2]

# ⚡ Quick Tips:
# - axis=0 → find max in each column
# - axis=1 → find max in each row

# ==========================================
# 3️⃣ np.argmin() – Index of Minimum Value
# ==========================================
# Returns the index of the minimum value in an array

print("Index of min in a:", np.argmin(a))
# 0

print("Index of min along columns (axis=0):", np.argmin(b, axis=0))
# [0 0 0 0]

# ⚡ Quick Tips:
# - axis parameter works same as np.argmax
# - Useful for quickly locating extremum positions in arrays