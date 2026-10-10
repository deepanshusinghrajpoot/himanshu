# ==========================================
# NumPy: Advanced Array Manipulation
# ==========================================

import numpy as np

# ==========================================
# 1️⃣ np.isin() – Membership Check
# ==========================================
# Checks if elements of one array are in another array
# Syntax: np.isin(array, test_elements)
# Returns a boolean array
# Useful for filtering or condition checks

a = np.arange(25)
print("Membership check:", np.isin(a, [2, 3, 4, 9]))
# [False False  True  True  True False False False False  True False ... ]

# Extract elements present in another array
print("Filtered elements:", a[np.isin(a, [2, 3, 4, 9, 5000])])
# [2 3 4 9]

# ⚡ Quick Tips:
# - Use for filtering arrays based on a condition
# - Handles arrays of different sizes efficiently

# ==========================================
# 2️⃣ np.flip() – Reverse Array
# ==========================================
# Reverses the order of elements along a specified axis
# Syntax: np.flip(array, axis=None)
# - axis=None → flip both rows and columns
# - axis=0 → flip vertically (rows)
# - axis=1 → flip horizontally (columns)

b = np.arange(12).reshape(3, 4)
print("Original array:\n", b)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print("Flip both axes:\n", np.flip(b))
# [[11 10  9  8]
#  [ 7  6  5  4]
#  [ 3  2  1  0]]

print("Flip axis=0 (vertical):\n", np.flip(b, axis=0))
# [[ 8  9 10 11]
#  [ 4  5  6  7]
#  [ 0  1  2  3]]

print("Flip axis=1 (horizontal):\n", np.flip(b, axis=1))
# [[ 3  2  1  0]
#  [ 7  6  5  4]
#  [11 10  9  8]]

# ⚡ Quick Tips:
# - np.flip preserves the shape of the array
# - Useful for reversing sequences, rows, or columns

# ==========================================
# 3️⃣ np.put() – Replace Specific Elements
# ==========================================
# Replaces elements at specific indices with given values
# Syntax: np.put(array, indices, values)
# Works on the flattened array

m = np.arange(9)
print("Original array:", m)
# [0 1 2 3 4 5 6 7 8]

np.put(m, [3, 4], [333, 444])
print("After np.put:", m)
# [  0   1   2 333 444   5   6   7   8]

# ⚡ Quick Tips:
# - Indices are based on flattened array
# - Useful for targeted replacement without loops