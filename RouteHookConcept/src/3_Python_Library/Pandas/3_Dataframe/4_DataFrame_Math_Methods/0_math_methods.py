
import numpy as np
import pandas as pd

import os





path_dir = os.path.dirname(__file__)

path_file_movies = os.path.join(path_dir, '../../1_Dataset/movies.csv')
path_file_ipl_matches = os.path.join(path_dir, '../../1_Dataset/ipl-matches.csv')


movies = pd.read_csv(path_file_movies)
ipl_matches = pd.read_csv(path_file_ipl_matches)






student_dict = {
    'iq':[100, 90, 120, 80, 0, 0],
    'marks':[80, 70, 100, 50, 0, 0],
    'package':[10, 7, 14, 2, 0, 0]
}

students = pd.DataFrame(student_dict)

print(students)
#     iq  marks  package
# 0  100     80       10
# 1   90     70        7
# 2  120    100       14
# 3   80     50        2
# 4    0      0        0
# 5    0      0        0






# ==================================================
# Math Methods (Pandas DataFrame)
# ==================================================

# These methods perform mathematical and statistical
# calculations on DataFrame data.



# ==================================================
# Axis Argument (Very Important)
# ==================================================

# Interview Definition
# axis specifies the direction along which the operation
# is performed in a DataFrame.
#
# axis = 0 → column-wise operation (vertical)
# axis = 1 → row-wise operation (horizontal)
#
# Default axis = 0



# ==================================================
# sum()
# ==================================================

# Interview Definition
# sum() returns the total sum of values along the
# specified axis in a DataFrame.

print(students.sum())

# iq         390
# marks      300
# package     33
# dtype: int64


print(students.sum(axis=0))   # column wise sum
# iq         390
# marks      300
# package     33
# dtype: int64


print(students.sum(axis=1))   # row wise sum
# 0    190
# 1    167
# 2    234
# 3    132
# 4      0
# 5      0
# dtype: int64



# ==================================================
# count()
# ==================================================

# Interview Definition
# count() returns the number of non-null values
# present in the DataFrame.

print(students.count())

# iq         6
# marks      6
# package    6
# dtype: int64


print(students.count(axis=1))

# 0    3
# 1    3
# 2    3
# 3    3
# 4    3
# 5    3
# dtype: int64



# ==================================================
# product()
# ==================================================

# Interview Definition
# product() returns the multiplication of values
# along the specified axis.

print(students.product())

# iq         0
# marks      0
# package    0
# dtype: int64


print(students.product(axis=1))

# 0     80000
# 1     44100
# 2    168000
# 3      8000
# 4         0
# 5         0
# dtype: int64



# ==================================================
# Mean
# ==================================================

# Interview Definition
# Mean is the average value of a dataset calculated
# by dividing the sum of values by the total number
# of observations.

# mean() returns the average of values.

print(students.mean())

# iq         65.0
# marks      50.0
# package     5.5
# dtype: float64


print(students.mean(axis=1))



# ==================================================
# Median
# ==================================================

# Interview Definition
# Median is the middle value of a dataset when the
# values are arranged in ascending or descending order.

# median() returns the median of values.

print(students.median())

# iq         85.0
# marks      60.0
# package     4.5
# dtype: float64


print(students.median(axis=1))



# ==================================================
# Mode
# ==================================================

# Interview Definition
# Mode is the value that appears most frequently
# in a dataset.

# mode() returns the most frequent value.

print(students.mode())

#    iq  marks  package
# 0   0      0        0



# ==================================================
# Standard Deviation
# ==================================================

# Interview Definition
# Standard deviation measures the amount of variation
# or dispersion of values from the mean.

# std() returns the standard deviation.

print(students.std())

# iq         52.057660
# marks      41.952354
# package     5.787918
# dtype: float64



# ==================================================
# Variance
# ==================================================

# Interview Definition
# Variance measures how far the values in a dataset
# are spread out from the mean.

# var() returns the variance of values.

print(students.var())

# iq         2710.0
# marks      1760.0
# package      33.5
# dtype: float64



# ==================================================
# Minimum
# ==================================================

# Interview Definition
# min() returns the smallest value present in
# the DataFrame.

print(students.min())

# iq         0
# marks      0
# package    0
# dtype: int64


print(students.min(axis=1))



# ==================================================
# Maximum
# ==================================================

# Interview Definition
# max() returns the largest value present in
# the DataFrame.

print(students.max())

# iq         120
# marks      100
# package     14
# dtype: int64


print(students.max(axis=1))



# ==================================================
# Quick Interview Revision
# ==================================================

# lll In Pandas we can perform mathematical operations 
#     both row-wise and column-wise using the axis parameter.
#     axis=0 → indicating column wise
#     axis=1 → indicating row wise

# ----------------------
# lll Common Parameters 
# ----------------------

# In pandas mathematical method has parameter

# axis ->
# 0 : column-wise sum (default)
# 1 : row-wise sum

# skipna ->
# True  : ignores NaN values (default)
# False : includes NaN effect

# numeric_only ->
# True  : only numeric columns
# False : all possible columns





# sum()      → total of values
# count()    → number of non-null values
# product()  → multiplication of values
# mean()     → average value
# median()   → middle value
# mode()     → most frequent value
# std()      → standard deviation
# var()      → variance
# min()      → smallest value
# max()      → largest value
#
# axis=0 → column wise
# axis=1 → row wise


