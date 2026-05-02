# ==========================================
# NumPy: Statistics & Data Analysis Functions
# ==========================================

import numpy as np

# ==========================================
# 1️⃣ np.percentile() – Percentiles
# ==========================================
# Computes the nth percentile of array elements
# Syntax: np.percentile(array, percentile, axis=None)
# - 50th percentile → median
# - 25th percentile → lower quartile
# - 100th percentile → maximum value

a = np.arange(12)
print("Array a:", a)
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

print("100th percentile:", np.percentile(a, 100))  # 11.0
print("50th percentile (median):", np.percentile(a, 50))  # 5.5
print("25th percentile (Q1):", np.percentile(a, 25))  # 2.75

# ⚡ Quick Tips:
# - Percentiles help understand data distribution
# - Useful in statistics and outlier detection

# ==========================================
# 2️⃣ np.histogram() – Frequency Distribution
# ==========================================
# Computes the frequency of array elements in bins
# Syntax: np.histogram(array, bins)

c = np.arange(15)
hist, bin_edges = np.histogram(c, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("Histogram counts:", hist)
# [10  5  0  0  0  0  0  0  0  0]
print("Bin edges:", bin_edges)
# [  0  10  20  30  40  50  60  70  80  90 100]

# ⚡ Quick Tips:
# - `bins` defines intervals for counting
# - Useful for visualizing data distribution

# ==========================================
# 3️⃣ np.corrcoef() – Correlation Coefficient
# ==========================================
# Computes Pearson correlation coefficient
# Syntax: np.corrcoef(array1, array2)
# - Returns a matrix showing correlation between arrays
# - Values range: -1 (negative corr) → 1 (positive corr)

salary = np.array([20000, 40000, 25000, 35000, 60000])
experience = np.array([1, 3, 2, 4, 2])

corr_matrix = np.corrcoef(salary, experience)
print("Correlation matrix:\n", corr_matrix)
# [[1.         0.25344572]
#  [0.25344572 1.        ]]

# ⚡ Quick Tips:
# - Diagonal is always 1 (self-correlation)
# - Off-diagonal shows correlation between arrays
# - Useful in data analysis, regression, and ML