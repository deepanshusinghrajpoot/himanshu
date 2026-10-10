# ==========================================
# Pandas Series: head(), tail(), sample()
# ==========================================

import pandas as pd
import os

# Load dataset as Series
path_dir = os.path.dirname(__file__)
file_path = os.path.join(path_dir, '../../1_Dataset/kohli_ipl.csv')
vk = pd.read_csv(file_path, index_col='match_no').squeeze('columns')

# ------------------------------------------------
# 1️⃣ head()
# ------------------------------------------------
# Spoken Interview Definition:
# lll "Returns the first n elements of the Series. Default is 5 if n not provided."
print(vk.head())
# Output:
# match_no
# 1     1
# 2    23
# 3    13
# 4    12
# 5     1
# Name: runs, dtype: int64

print(vk.head(3))
# Output:
# match_no
# 1     1
# 2    23
# 3    13
# Name: runs, dtype: int64

# ------------------------------------------------
# 2️⃣ tail()
# ------------------------------------------------
# Spoken Interview Definition:
# lll "Returns the last n elements of the Series. Default is 5 if n not provided."
print(vk.tail())
# Output:
# match_no
# 211     0
# 212    20
# 213    73
# 214    25
# 215     7
# Name: runs, dtype: int64

print(vk.tail(3))
# Output:
# match_no
# 213    73
# 214    25
# 215     7
# Name: runs, dtype: int64

# ------------------------------------------------
# 3️⃣ sample()
# ------------------------------------------------
# Spoken Interview Definition:
# lll "Returns random n elements of the Series. Default is 1 if n not provided."
print(vk.sample())
# Example Output (random):
# match_no
# 29    24
# Name: runs, dtype: int64


# Quick Tips:
# - head() and tail() are helpful for quickly inspecting top/bottom data.
# - sample() is useful for random checks or testing subsets.
# - All these methods **do not modify the original Series**; they return a new view.