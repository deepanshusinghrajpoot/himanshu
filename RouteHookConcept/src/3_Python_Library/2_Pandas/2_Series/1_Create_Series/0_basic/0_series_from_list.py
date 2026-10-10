# ==========================================
# Pandas Series: Creation & Features
# ==========================================

import pandas as pd

# 1️⃣ Series from Lists
# ---------------------
# A Series is a 1-D labeled array.
# It returns two things:
# 1. Index (labels)
# 2. Corresponding values

# ---------------------
# Example: String Series
country = ['India', 'Pakistan', 'USA', 'Nepal', 'Srilanka']
country_series = pd.Series(country)
print(country_series)
# 0       India
# 1    Pakistan
# 2         USA
# 3       Nepal
# 4    Srilanka
# dtype: object

# ---------------------
# Example: Integer Series
runs = [13, 24, 56, 78, 100]
runs_series = pd.Series(runs)
print(runs_series)
# 0     13
# 1     24
# 2     56
# 3     78
# 4    100
# dtype: int64

# 2️⃣ Series with Custom Index
# ----------------------------
marks = [91, 95, 82, 82, 82]
subjects = ['Maths', 'Hindi', 'Science', 'Social Science', 'Art']

marks_series = pd.Series(marks, index=subjects)
print(marks_series)
# Maths             91
# Hindi             95
# Science           82
# Social Science    82
# Art               82
# dtype: int64

# 3️⃣ Naming a Series
# -------------------
named_series = pd.Series(marks, index=subjects, name='Deepanshu ke marks')
print(named_series)
# Maths             91
# Hindi             95
# Science           82
# Social Science    82
# Art               82
# Name: Deepanshu ke marks, dtype: int64

# ⚡ Quick Tips:
# - Series can store any data type: int, float, string, etc.
# - Use custom indices for meaningful labels.
# - Naming a Series helps during visualization and tabular operations.


'''



lll In Pandas, there are two ways to create a custom index.

lll First is using the index parameter:
    It is used while creating a Series or DataFrame manually.

lll Second is using the index_col parameter:
    It is used while loading data from any sources,
    where a specific column is set as the index.



'''