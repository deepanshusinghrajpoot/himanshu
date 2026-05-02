import numpy as np


# Working with Missing Values (np.nan)
# ====================================

# np.nan represents a missing or undefined value in NumPy.

a = np.array([1, 2, 3, 4, np.nan, 6])

print(a)
# [ 1.  2.  3.  4. nan  6.]


# Detect missing values
# ---------------------

print(np.isnan(a))

# Output
# [False False False False  True False]


# Remove missing values using Boolean Indexing
# --------------------------------------------

print(a[~np.isnan(a)])

# Output
# [1. 2. 3. 4. 6.]








# Important NumPy Functions for Missing Values
# ============================================

# Functions
# np.isnan()   → Detect missing values
# np.nanmean() → Mean ignoring NaN
# np.nansum()  → Sum ignoring NaN
# np.nanmax()  → Maximum value ignoring NaN


# Example
# -------

a = np.array([10, 20, np.nan, 40, 50, np.nan])

print("Original Array:")
print(a)


# Detect missing values
print("\nCheck Missing Values:")
print(np.isnan(a))


# Mean ignoring NaN
print("\nMean (ignoring NaN):")
print(np.nanmean(a))


# Sum ignoring NaN
print("\nSum (ignoring NaN):")
print(np.nansum(a))


# Maximum ignoring NaN
print("\nMax (ignoring NaN):")
print(np.nanmax(a))



'''
Original Array:
[10. 20. nan 40. 50. nan]

Check Missing Values:
[False False  True False False  True]

Mean (ignoring NaN):
30.0

Sum (ignoring NaN):
120.0

Max (ignoring NaN):
50.0
'''