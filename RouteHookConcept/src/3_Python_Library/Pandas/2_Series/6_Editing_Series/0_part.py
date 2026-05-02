import numpy as np
import pandas as pd

import os



# ==================================================
# Pandas Series Editing
# ==================================================

# Definition (Interview Friendly)
# Editing a Pandas Series means modifying existing values
# or adding new values using index labels or index positions.

# Important Points
# • Series values can be updated directly using indexing
# • If the index exists → value gets updated
# • If the index does NOT exist → a new element is created
# • Editing works with slicing and fancy indexing as well



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



# ==================================================
# 1. Editing an Existing Value
# ==================================================

# Definition (Interview Friendly)
# If the index label already exists in the Series,
# assigning a new value updates the existing element.


marks_series['math'] = 95

print(marks_series)

# math              95
# english           85
# science           86
# hindi             91
# social science    82
# Name: Deepanshu Singh, dtype: int64



# ==================================================
# 2. Adding a New Element
# ==================================================

# Definition (Interview Friendly)
# If the index label does not exist, Pandas automatically
# creates a new element in the Series.


marks_series['language'] = 90

print(marks_series)

# math              95
# english           85
# science           86
# hindi             91
# social science    82
# language          90
# Name: Deepanshu Singh, dtype: int64



# ==================================================
# 3. Editing Using Slicing
# ==================================================

# Definition (Interview Friendly)
# Multiple values can be modified at once using slicing.

# Syntax
# series[start : stop] = [new values]


runs = pd.Series([45, 67, 13, 34, 99], name='rohit runs')

print(runs)

# 0    45
# 1    67
# 2    13
# 3    34
# 4    99
# Name: rohit runs, dtype: int64


runs[2:4] = [100, 264]

print(runs)

# 0     45
# 1     67
# 2    100
# 3    264
# 4     99
# Name: rohit runs, dtype: int64



# ==================================================
# 4. Editing Using Fancy Indexing
# ==================================================

# Definition (Interview Friendly)
# Fancy indexing allows modifying multiple specific
# positions using a list of indexes.


runs[[0, 2, 4]] = [0, 0, 0]

print(runs)

# 0      0
# 1     67
# 2      0
# 3    264
# 4      0
# Name: rohit runs, dtype: int64



# ==================================================
# 5. Editing Using Index Labels
# ==================================================

# Definition (Interview Friendly)
# You can update multiple values using index labels
# instead of numeric positions.


marks_series[['math', 'english']] = [98, 88]

print(marks_series)

# math              98
# english           88
# science           86
# hindi             91
# social science    82
# language          90
# Name: Deepanshu Singh, dtype: int64



# ==================================================
# Quick Revision
# ==================================================

# Update value → series['index'] = new_value

# Add new element → series['new_index'] = value

# Slice update → series[start:stop] = values

# Fancy update → series[[i1,i2,i3]] = values

# Label update → series[['label1','label2']] = values