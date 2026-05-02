import numpy as np
import pandas as pd

import os



# ==================================================
# Pandas Series Indexing Techniques
# ==================================================

# Definition (Interview Friendly)
# Series Indexing Techniques are different ways to access
# multiple elements from a Pandas Series.

# Common techniques include:
# • Slicing
# • Fancy Indexing
# • Label-based Fancy Indexing



path_dir = os.path.dirname(__file__)
file_path1 = os.path.join(path_dir, '../../1_Dataset/kohli_ipl.csv')
file_path2 = os.path.join(path_dir, '../../1_Dataset/bollywood.csv')


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




movies = pd.read_csv(file_path2, index_col='movie').squeeze('columns')
print(movies)

# movie
# Uri: The Surgical Strike                   Vicky Kaushal
# Battalion 609                                Vicky Ahuja
# The Accidental Prime Minister (film)         Anupam Kher
# Why Cheat India                            Emraan Hashmi
# Evening Shadows                         Mona Ambegaonkar
#                                               ...
# Hum Tumhare Hain Sanam                    Shah Rukh Khan
# Aankhen (2002 film)                     Amitabh Bachchan
# Saathiya (film)                             Vivek Oberoi
# Company (film)                                Ajay Devgn
# Awara Paagal Deewana                        Akshay Kumar
# Name: lead, Length: 1500, dtype: str



# ==================================================
# 1. Series Slicing
# ==================================================

# Definition (Interview Friendly)
# Slicing means selecting a range of elements from a Series
# using start, stop, and step values.

# Syntax
# series[start : stop : step]

# Important Points
# • Similar to Python list slicing
# • Start index is inclusive
# • Stop index is exclusive
# • Step controls the interval of selection


print(vk[-5:])

# Output
# match_no
# 211     0
# 212    20
# 213    73
# 214    25
# 215     7
# Name: runs, dtype: int64


print(vk[0::100])

# Output
# match_no
# 1       1
# 101    41
# 201    12
# Name: runs, dtype: int64



# ==================================================
# 2. Fancy Indexing
# ==================================================

# Definition (Interview Friendly)
# Fancy indexing means selecting multiple elements
# using a list of index positions.

# Important Points
# • Uses a list of indexes
# • Returns multiple selected rows
# • Useful when indexes are not continuous


print(vk[[1, 2, 3, 4, 5]])

# Output
# match_no
# 1     1
# 2    23
# 3    13
# 4    12
# 5     1
# Name: runs, dtype: int64



# ==================================================
# 3. Label-based Fancy Indexing
# ==================================================

# Definition (Interview Friendly)
# Label-based fancy indexing selects multiple values
# using index labels instead of integer positions.

# Important Points
# • Works when Series has meaningful labels
# • Very common in real-world datasets


print(movies[['Uri: The Surgical Strike', 'Awara Paagal Deewana']])

# Output
# movie
# Uri: The Surgical Strike    Vicky Kaushal
# Awara Paagal Deewana         Akshay Kumar
# Name: lead, dtype: str



# ==================================================
# Quick Revision
# ==================================================

# Slicing → Select a range of elements
# Example: series[0:10]

# Fancy Indexing → Select multiple rows using index list
# Example: series[[1,2,3]]

# Label Fancy Indexing → Select multiple rows using labels
# Example: series[['label1','label2']]