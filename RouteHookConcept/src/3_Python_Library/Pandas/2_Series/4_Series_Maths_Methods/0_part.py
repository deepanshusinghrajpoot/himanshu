import pandas as pd
import numpy as np
import os

# ===============================
# Load datasets
# ===============================
path_dir = os.path.dirname(__file__)
file_path1 = os.path.join(path_dir, '../../1_Dataset/kohli_ipl.csv')
file_path2 = os.path.join(path_dir, '../../1_Dataset/bollywood.csv')
file_path3 = os.path.join(path_dir, '../../1_Dataset/subs.csv')

vk = pd.read_csv(file_path1).squeeze('columns')
movies = pd.read_csv(file_path2).squeeze('columns')
subs = pd.read_csv(file_path3).squeeze('columns')


# ===============================
# 1️⃣ count()
# ===============================
# lll Spoken: "Returns number of non-NaN(missing) elements in the Series"
print(vk.count())
# Output:
# match_no    215
# runs        215
# dtype: int64

print(vk.count().values[0])
print(vk.count().values[1])
# Output:
# 215
# 215


# ===============================
# 2️⃣ sum()
# ===============================
# lll Spoken: "Returns the sum of all elements in the Series"
print(subs.sum())
# Output: 49510


# ===============================
# 3️⃣ product()
# ===============================
# lll Spoken: "Returns the product of all elements in the Series (may overflow)"
print(subs.product())
# Output: 0  (due to integer overflow)


# ===============================
# 4️⃣ mean, median, mode, std, var
# ===============================
# lll Spoken definitions:
# mean: Returns avg of all elements in a series
# median: Returns middle element after sorting
# mode: Returns most frequent element
# std: standard deviation, spread of data
# var: variance, squared spread of data

print(vk.mean())
# Output:
# match_no    108.000000
# runs         30.855814
# dtype: float64

print(vk.median())
# Output:
# match_no    108.0
# runs         24.0
# dtype: float64

print(vk.std())
# Output:
# match_no    62.209324
# runs        26.229801
# dtype: float64

print(vk.var())
# Output:
# match_no    3870.000000
# runs         688.002478
# dtype: float64


print(subs.mean())
# Output: 135.64383561643837

print(subs.median())
# Output: 123.0

print(subs.mode())
# Output:
# 0    105
# Name: Subscribers gained, dtype: int64

print(subs.std())
# Output: 62.6750230372527

print(subs.var())
# Output: 3928.1585127201565


# ===============================
# 5️⃣ min() / max()
# ===============================
# Spoken:
# min(): returns smalest element in a series
# max(): returns largest element in a series

print(subs.min())
print(subs.max())
# Output:
# 33
# 396

print(vk.min())
print(vk.max())
# Output:
# match_no    1
# runs        0
# dtype: int64
# match_no    215
# runs        113
# dtype: int64


# ===============================
# 6️⃣ describe()
# ===============================
# Spoken: "Returns a statistical summary of the Series or DataFrame:
# count, mean, std, min, max, 25%, 50%, 75% percentiles
# For categorical data, it returns count, unique, top, freq"

print(vk.describe())
# Output:
#         match_no        runs
# count  215.000000  215.000000
# mean   108.000000   30.855814
# std     62.209324   26.229801
# min      1.000000    0.000000
# 25%     54.500000    9.000000
# 50%    108.000000   24.000000
# 75%    161.500000   48.000000
# max    215.000000  113.000000

print(subs.describe())
# Output:
# count    365.000000
# mean     135.643836
# std       62.675023
# min       33.000000
# 25%       88.000000
# 50%      123.000000
# 75%      177.000000
# max      396.000000
# Name: Subscribers gained, dtype: float64

print(movies.describe())
# Output:
#                           movie          lead
# count                      1500          1500
# unique                     1497           566
# top     Tanu Weds Manu: Returns  Akshay Kumar
# freq                          2            48







# lll count(): "Returns number of non-NaN(missing) elements in the Series"
# lll sum(): "Returns the sum of all elements in the Series"
# lll product(): "Returns the product of all elements in the Series (may overflow)"
# lll mean(): Returns avg of all elements in a series
# lll median(): Returns middle element after sorting
# lll mode(): Returns most frequent element
# lll std(): standard deviation, spread of data
# lll var(): variance, squared spread of data
# lll min(): returns smalest element in a series
# lll max(): returns largest element in a series
# lll describe(): "Returns a statistical summary of the Series or DataFrame:
#              count, mean, std, min, max, 25%, 50%, 75% percentiles
#              For categorical data, it returns count, unique, top, freq"