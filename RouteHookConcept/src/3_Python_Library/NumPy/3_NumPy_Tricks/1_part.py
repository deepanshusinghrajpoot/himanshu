# ==========================================
# NumPy Array Utilities: unique & expand_dims
# ==========================================

import numpy as np

# ==========================================
# 1️⃣ np.unique() – Find Unique Values
# ==========================================
# Returns sorted unique values from an array
# Useful for removing duplicates quickly

e = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6])
print("Original array:", e)
# Original array: [1 1 2 2 3 3 4 4 5 5 5 6 6]

print("Unique values   :", np.unique(e))
# Unique values   : [1 2 3 4 5 6]

# ⚡ Quick Tip:
# - np.unique() automatically sorts the values
# - Can also return counts and indices using:
#   np.unique(e, return_counts=True), np.unique(e, return_index=True)

# ==========================================
# 2️⃣ np.expand_dims() – Add a New Dimension
# ==========================================
# Expands the shape of an array by adding a new axis
# Useful for broadcasting or reshaping arrays

print("Expand along axis=0:\n", np.expand_dims(e, axis=0))
# [[1 1 2 2 3 3 4 4 5 5 5 6 6]]
# Shape changes from (13,) → (1, 13)

print("Expand along axis=1:\n", np.expand_dims(e, axis=1))
# [[1]
#  [1]
#  [2]
#  [2]
#  [3]
#  [3]
#  [4]
#  [4]
#  [5]
#  [5]
#  [5]
#  [6]
#  [6]]
# Shape changes from (13,) → (13, 1)

# ⚡ Quick Tips:
# - axis=0 → adds a row dimension
# - axis=1 → adds a column dimension
# - Useful when preparing arrays for np.concatenate, np.hstack, or broadcasting