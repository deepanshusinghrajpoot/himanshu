import numpy as np
import pandas as pd

import os




# ==================================================
# Pandas Series with Python Functionalities
# ==================================================

# Definition (Interview Friendly)
# A Pandas Series behaves very similar to Python data structures.
# Many built-in Python functions and operators can work directly
# with a Series object.

# Important Points
# • Python built-in functions work with Series
# • Series supports loops and membership operators
# • Arithmetic and relational operators support broadcasting
# • Series can be converted to Python data types



path_dir = os.path.dirname(__file__)
file_path1 = os.path.join(path_dir, '../../1_Dataset/subs.csv')
file_path2 = os.path.join(path_dir, '../../1_Dataset/bollywood.csv')
file_path3 = os.path.join(path_dir, '../../1_Dataset/kohli_ipl.csv')

subs = pd.read_csv(file_path1).squeeze('columns').head(10)
print(subs)

# 0    48
# 1    57
# 2    40
# 3    43
# 4    44
# 5    46
# 6    33
# 7    40
# 8    44
# 9    74
# Name: Subscribers gained, dtype: int64




# ==================================================
# 1. lll Python Built-in Functions
# ==================================================

# Definition (Interview Friendly)
# Many Python built-in functions can directly operate
# on a Pandas Series.


# len/min/max/sum/sorted
#------------------------

print(len(subs)) # 10
print(min(subs)) # 33
print(max(subs)) # 74
print(sum(subs)) # 469
print(sorted(subs)) # [33, 40, 40, 43, 44, 44, 46, 48, 57, 74]



# lll Important Points
# • len() → returns number of elements in a series.
# • min() → returns smalest element in a series.
# • max() → returns largest element in a series.
# • sum() → returns sum of all elements in a series.
# • sorted() → returns sorted list (not a Series).




# ==================================================
# 2. type() and dir()
# ==================================================

# Definition (Interview Friendly)
# lll type() returns the object type
# lll dir() returns all attributes and methods of the object


print(type(subs)) # <class 'pandas.Series'>
print(dir(subs)) # return all method and attribute




# ==================================================
# 3. lll Type Conversion
# ==================================================

# Definition (Interview Friendly)
# A Pandas Series can be converted into Python
# data structures like list, dictionary, etc.


print(type(list(subs))) # <class 'list'>




# ==================================================
# 4. Membership Operator
# ==================================================

# Definition (Interview Friendly)
# The membership operator checks whether a value exists
# inside a Series.

# Important Rule
# By default, membership operator works on the INDEX
# not on the VALUES.



movies = pd.read_csv(file_path2, index_col='movie').squeeze('columns').head(10)
print(movies)

# movie
# Uri: The Surgical Strike                       Vicky Kaushal
# Battalion 609                                    Vicky Ahuja
# The Accidental Prime Minister (film)             Anupam Kher
# Why Cheat India                                Emraan Hashmi
# Evening Shadows                             Mona Ambegaonkar
# Soni (film)                             Geetika Vidya Ohlyan
# Fraud Saiyaan                                   Arshad Warsi
# Bombairiya                                      Radhika Apte
# Manikarnika: The Queen of Jhansi              Kangana Ranaut
# Thackeray (film)                         Nawazuddin Siddiqui
# Name: lead, dtype: str


print('Uri: The Surgical Strike' in movies) # True
print('Vicky Kaushal' in movies)            # False
print('Vicky Kaushal' in movies.values)     # True




# ==================================================
# 5. Looping through Series
# ==================================================

# Definition (Interview Friendly)
# Iterating over a Series returns the VALUES by default.


for i in movies:
    print(i)

# Vicky Kaushal
# Vicky Ahuja
# Anupam Kher
# Emraan Hashmi
# Mona Ambegaonkar
# Geetika Vidya Ohlyan
# Arshad Warsi
# Radhika Apte
# Kangana Ranaut
# Nawazuddin Siddiqui




# ==================================================
# 6. Arithmetic Operations (Broadcasting)
# ==================================================

# Definition (Interview Friendly)
# Arithmetic operations apply the operation to
# every element of the Series automatically.
# This concept is called Broadcasting.


dict = {
    'math':91,
    'english':85,
    'science':86,
    'hindi':91,
    'social science':82
}

marks_series = pd.Series(dict, name='Deepanshu Singh')
print(marks_series)

# math              91
# english           85
# science           86
# hindi             91
# social science    82
# Name: Deepanshu Singh, dtype: int64


print(100 - marks_series)

# math               9
# english           15
# science           14
# hindi              9
# social science    18
# Name: Deepanshu Singh, dtype: int64


print(100 + marks_series)

# math              191
# english           185
# science           186
# hindi             191
# social science    182
# Name: Deepanshu Singh, dtype: int64


# Note
# Similar operations work with
# *, /, **, %




# ==================================================
# 7. Relational Operators
# ==================================================

# Definition (Interview Friendly)
# Relational operators compare each element in a Series
# and return a Boolean Series (True / False).


vk = pd.read_csv(file_path3, index_col='match_no').squeeze('columns').head(10)
print(vk)

# match_no
# 1      1
# 2     23
# 3     13
# 4     12
# 5      1
# 6      9
# 7     34
# 8      0
# 9     21
# 10     3
# Name: runs, dtype: int64


print(vk >= 15)

# match_no
# 1     False
# 2      True
# 3     False
# 4     False
# 5     False
# 6     False
# 7      True
# 8     False
# 9      True
# 10    False
# Name: runs, dtype: bool


print(vk[ vk >= 15 ])

# match_no
# 2    23
# 7    34
# 9    21
# Name: runs, dtype: int64




# ==================================================
# Quick Revision
# ==================================================

# Built-in Functions → len(), min(), max(), sum(), sorted()

# Membership Operator → works on index by default

# Looping → iterates over Series values

# Broadcasting → arithmetic operation applied to all elements

# Relational Operators → return Boolean Series