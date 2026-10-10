# ==========================================
# NumPy: Cumulative Functions
# ==========================================

import numpy as np

# ==========================================
# 1️⃣ np.cumsum() – Cumulative Sum
# ==========================================
# Computes the cumulative sum of array elements along a specified axis
# Syntax: np.cumsum(array, axis=None)

# 1D Example
a = np.arange(12, 24)
print("Array a:", a)
# [12 13 14 15 16 17 18 19 20 21 22 23]

print("Cumulative sum (1D):", np.cumsum(a))
# [ 12  25  39  54  70  87 105 124 144 165 187 210]

# 2D Example
b = np.arange(12, 24).reshape(3, 4)
print("Array b:\n", b)
# [[12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]]

print("Cumulative sum (flattened):", np.cumsum(b))
# [ 12  25  39  54  70  87 105 124 144 165 187 210]

print("Cumulative sum along columns (axis=0):\n", np.cumsum(b, axis=0))
# [[12 13 14 15]
#  [28 30 32 34]
#  [48 51 54 57]]

print("Cumulative sum along rows (axis=1):\n", np.cumsum(b, axis=1))
# [[12 25 39 54]
#  [16 33 51 70]
#  [20 41 63 86]]

# ⚡ Quick Tips:
# - axis=0 → cumulative sum column-wise
# - axis=1 → cumulative sum row-wise
# - Useful in running totals and time-series analysis

# ==========================================
# 2️⃣ np.cumprod() – Cumulative Product
# ==========================================
# Computes the cumulative product of array elements along a specified axis
# Syntax: np.cumprod(array, axis=None)

# 1D Example
print("Cumulative product (1D):", np.cumprod(a))
# [ 12 156 2184 32760 524160 8910720 160392960 3047466240 60949324800 1279935820800 28158588057600 647647525324800]

# 2D Example
print("Cumulative product (flattened):", np.cumprod(b))
# [ 12 156 2184 32760 524160 8910720 160392960 3047466240 60949324800 1279935820800 28158588057600 647647525324800]

print("Cumulative product along columns (axis=0):\n", np.cumprod(b, axis=0))
# [[  12   13   14   15]
#  [ 192  221  252  285]
#  [3840 4641 5544 6555]]

print("Cumulative product along rows (axis=1):\n", np.cumprod(b, axis=1))
# [[    12    156   2184  32760]
#  [    16    272   4896  93024]
#  [    20    420   9240 212520]]

# ⚡ Quick Tips:
# - axis=0 → cumulative product column-wise
# - axis=1 → cumulative product row-wise
# - Useful in compound interest, probability, or growth computations