import numpy as np
import pandas as pd

import os



# ==================================================
# Boolean Indexing on Pandas Series
# ==================================================

# Definition (Interview Friendly)
# Boolean Indexing is a technique used to filter data
# from a Pandas Series using True / False conditions.

# Important Points
# • A condition is applied to each element in the Series
# • It returns a Boolean Series (True / False)
# • Only values with True condition are selected
# • Very useful for filtering data in Data Analysis



path_dir = os.path.dirname(__file__)
file_path1 = os.path.join(path_dir, '../../1_Dataset/kohli_ipl.csv')
file_path2 = os.path.join(path_dir, '../../1_Dataset/subs.csv')
file_path3 = os.path.join(path_dir, '../../1_Dataset/bollywood.csv')


vk = pd.read_csv(file_path1, index_col='match_no').squeeze('columns')
print(vk)

# match_no
# 1       1
# 2      23
# 3      13
# 4      12
# 5       1
#        ..
# 211     0
# 212    20
# 213    73
# 214    25
# 215     7
# Name: runs, Length: 215, dtype: int64




# ==================================================
# Example 1
# Find number of 50's and 100's scored by Kohli
# ==================================================

# Condition: runs >= 50

print(vk[vk >= 50].size) # 50


# Condition: runs == 100

print(vk[vk == 100].size)  # 2


print(vk[vk == 100])

# 120    100
# 164    100
# Name: runs, dtype: int64




# ==================================================
# Example 2
# Find number of Ducks (0 runs)
# ==================================================

# Duck means scoring 0 runs in a match


print(vk[vk == 0].size) # 9


print(vk[vk == 0])

# match_no
# 8      0
# 87     0
# 91     0
# 93     0
# 130    0
# 135    0
# 206    0
# 207    0
# 211    0
# Name: runs, dtype: int64




# ==================================================
# Example 3
# Count number of days when subscribers > 300
# ==================================================

subs = pd.read_csv(file_path2).squeeze('columns')

print(subs)

# 0       48
# 1       57
# 2       40
# 3       43
# 4       44
#       ...
# 360    231
# 361    226
# 362    155
# 363    144
# 364    172
# Name: Subscribers gained, Length: 365, dtype: int64


print(subs[subs >= 300].size) # 4


print(subs[subs >= 300])

# 168    306
# 233    301
# 330    396
# 331    312
# Name: Subscribers gained, dtype: int64




# ==================================================
# Example 4
# Find actors who have done more than 30 movies
# ==================================================

# Step 1: Load dataset

movies = pd.read_csv(file_path3, index_col='movie').squeeze('columns')


# Step 2: Count movies per actor

num_movies = movies.value_counts()

print(num_movies)

# lead
# Akshay Kumar        48
# Amitabh Bachchan    45
# Ajay Devgn          38
# Salman Khan         31
# Sanjay Dutt         26
#                    ..
# Tanishaa Mukerji     1
# Tanuja               1
# Ankit                1
# Rakhee Gulzar        1
# Edwin Fernandes      1
# Name: count, Length: 566, dtype: int64


# Step 3: Apply Boolean filtering

print(num_movies[num_movies > 30])

# lead
# Akshay Kumar        48
# Amitabh Bachchan    45
# Ajay Devgn          38
# Salman Khan         31
# Name: count, dtype: int64




# ==================================================
# Quick Revision
# ==================================================

# Boolean Indexing → filtering data using conditions

# Syntax
# series[condition]

# Example
# series[series > value]

# Common Operators
# >   greater than
# <   less than
# >=  greater than equal
# <=  less than equal
# ==  equal
# !=  not equal