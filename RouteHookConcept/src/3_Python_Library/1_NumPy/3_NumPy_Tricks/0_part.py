# ==========================================
# NumPy Array Operations: sort, append, concatenate
# ==========================================

import numpy as np

# ==========================================
# 1️⃣ np.sort() – Sorting Arrays
# ==========================================
# Sorts array along specified axis (default axis=-1)
# Returns a sorted copy; original array is not modified

# 1D Array Example
a = np.array([92, 85, 93, 82, 6, 9, 14])
print("Original 1D array:", a)
# Original 1D array: [92 85 93 82  6  9 14]

print("Sorted 1D array  :", np.sort(a))
# Sorted 1D array  : [ 6  9 14 82 85 92 93]

# 2D Array Example
b = np.array([[84, 66, 15, 94],
              [8, 33, 25, 69]])
print("Original 2D array:\n", b)
# Original 2D array:
# [[84 66 15 94]
#  [ 8 33 25 69]]

print("Column-wise sorted 2D array:\n", np.sort(b, axis=0))
# Column-wise sorted 2D array:
# [[ 8 33 15 69]
#  [84 66 25 94]]

# ==========================================
# 2️⃣ np.append() – Adding Elements
# ==========================================
# Appends values at the end of an array along specified axis
# Creates a new array; original is not modified

# 1D Example
x = np.arange(5)
print("Original 1D array:", x)
# Original 1D array: [0 1 2 3 4]

r = np.append(x, 10)
print("Appended 1D array:", r)
# Appended 1D array: [ 0  1  2  3  4 10]

# 2D Example – Adding a column
y = np.arange(6).reshape(2, 3)
print("Original 2D array:\n", y)
# Original 2D array:
# [[0 1 2]
#  [3 4 5]]

p = np.append(y, np.ones((y.shape[0], 1)), axis=1)
print("2D array after appending column:\n", p)
# [[0. 1. 2. 1.]
#  [3. 4. 5. 1.]]

# ==========================================
# 3️⃣ np.concatenate() – Combining Arrays
# ==========================================
# Combines multiple arrays along existing axis

c = np.arange(6).reshape(2, 3)
d = np.arange(6, 12).reshape(2, 3)

# Row-wise (axis=0)
row_concat = np.concatenate((c, d), axis=0)
print("Row-wise concatenation:\n", row_concat)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

# Column-wise (axis=1)
col_concat = np.concatenate((c, d), axis=1)
print("Column-wise concatenation:\n", col_concat)
# [[ 0  1  2  6  7  8]
#  [ 3  4  5  9 10 11]]

# ==========================================
# ⚡ Quick Revision Points
# ==========================================
# - np.sort() → returns sorted copy; use axis to sort rows/columns
# - np.append() → add elements; new array created; use axis for 2D
# - np.concatenate() → join arrays along axis
# - axis=0 → operate along rows, axis=1 → operate along columns