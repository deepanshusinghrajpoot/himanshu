# ==========================================
# Pandas Series: value_counts(), sort_values(), sort_index()
# ==========================================

import pandas as pd
import os

# Load datasets
path_dir = os.path.dirname(__file__)
file_path1 = os.path.join(path_dir, '../../1_Dataset/bollywood.csv')
file_path2 = os.path.join(path_dir, '../../1_Dataset/kohli_ipl.csv')

movies = pd.read_csv(file_path1, index_col='movie').squeeze('columns')
vk = pd.read_csv(file_path2, index_col='match_no').squeeze('columns')

# ------------------------------------------------
# 1️⃣ value_counts()
# ------------------------------------------------
# Spoken Interview Definition:
# lll "Returns frequency of each unique value in descending order by default."
# Useful for categorical data analysis.


print(movies.value_counts())
# Example Output:
# Akshay Kumar        48
# Amitabh Bachchan    45
# Ajay Devgn          38
# Salman Khan         31
# ...
# Name: lead, Length: 566, dtype: int64

# ------------------------------------------------
# 2️⃣ sort_values()
# ------------------------------------------------
# Spoken Interview Definition:
# lll "Sorts Series by its values. Default is ascending=True. Not permanent unless inplace=True."
# Can chain with head() to get top values.

print(vk.sort_values())
print(vk.sort_values(ascending=False))


# Method chaining example:
# Find highest score
print(vk.sort_values(ascending=False).head(1))        # returns Series
print(vk.sort_values(ascending=False).head(1).values) # returns numpy array
print(vk.sort_values(ascending=False).head(1).values[0]) # returns single value


# ------------------------------------------------
# 3️⃣ sort_index()
# ------------------------------------------------
# Spoken Interview Definition:
# lll "Sorts Series by its index labels. Default is ascending=True. Not permanent unless inplace=True."

print(movies.sort_index())
print(movies.sort_index(ascending=False))

# Method chaining example:
# Get last movie in alphabetical order
print(movies.sort_index(ascending=False).head(1))          # Series
print(movies.sort_index(ascending=False).head(1).values)   # <StringArray>
print(movies.sort_index(ascending=False).head(1).values[0])# Single string


# ------------------------------------------------
# ✅ Quick Tips:
# ------------------------------------------------
# • value_counts() is great for frequency analysis.
# • sort_values() helps in ranking numeric/categorical data.
# • sort_index() helps to restore or reorder original order of labels.
# • Method chaining is useful for quick one-liners.