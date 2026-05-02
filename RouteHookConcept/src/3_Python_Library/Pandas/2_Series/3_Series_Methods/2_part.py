import pandas as pd
import numpy as np
import os
import sys

# Load datasets
path_dir = os.path.dirname(__file__)
file_path1 = os.path.join(path_dir, '../../1_Dataset/bollywood.csv')
file_path2 = os.path.join(path_dir, '../../1_Dataset/kohli_ipl.csv')
file_path3 = os.path.join(path_dir, '../../1_Dataset/subs.csv')

movies = pd.read_csv(file_path1, index_col='movie').squeeze('columns')
vk = pd.read_csv(file_path2, index_col='match_no').squeeze('columns')
subs = pd.read_csv(file_path3).squeeze('columns')

# ==========================================
# 1️⃣ Memory Usage
# ==========================================
# sys.getsizeof(series) returns memory used by a Series object in bytes.
print(sys.getsizeof(vk))                  # Original memory
# Output: 1884
print(sys.getsizeof(vk.astype('int16')))  # Memory optimized
# Output: 594

# ==========================================
# 2️⃣ between()
# ==========================================
# Returns a boolean Series showing which values lie between two given bounds.

print(vk.between(51, 99))

# Output:
# match_no
# 1      False
# 2      False
# 3      False
# 4      False
# 5      False
#       ...
# 215    False
# Name: runs, Length: 215, dtype: bool

print(vk[vk.between(51, 99)])
# Output:
# 34     58
# 41     71
# 44     56
# 45     67
# ...
# 213    73
# Name: runs, dtype: int64

# ==========================================
# 3️⃣ clip()
# ==========================================
# Limits values: <min → min, >max → max
print(subs.clip(100, 200))
# Output:
# 0      100
# 1      100
# 2      100
# 3      100
# 4      100
# ...
# 360    200
# 361    200
# 362    155
# 363    144
# 364    172
# Name: Subscribers gained, Length: 365, dtype: int64

# ==========================================
# 4️⃣ drop_duplicates() & duplicated()
# ==========================================
# drop_duplicates(): removes repeated values, keeps first by default
temp = pd.Series([1,1,2,2,3,3,4,4])
print(temp.drop_duplicates())
# Output:
# 0    1
# 2    2
# 4    3
# 6    4
# dtype: int64

print(temp.drop_duplicates(keep='last'))
# Output:
# 1    1
# 3    2
# 5    3
# 7    4
# dtype: int64

# duplicated(): returns a boolean Series where True indicates a duplicate
print(temp.duplicated())
# Output:
# 0    False
# 1     True
# 2    False
# 3     True
# 4    False
# 5     True
# 6    False
# 7     True
# dtype: bool
print(temp.duplicated().sum())
# Output: 4

# ==========================================
# 5️⃣ isnull(), dropna(), fillna()
# ==========================================
# isnull(): True for missing (NaN) values
temp1 = pd.Series([1,2,3,np.nan,5,6,np.nan,8,np.nan,10])
print(temp1.isnull())
# Output:
# 0    False
# 1    False
# 2    False
# 3     True
# 4    False
# 5    False
# 6     True
# 7    False
# 8     True
# 9    False
# dtype: bool

print(temp1.isnull().sum())
# Output: 3

# dropna(): returns Series without NaNs
print(temp1.dropna())
# Output:
# 0     1.0
# 1     2.0
# 2     3.0
# 4     5.0
# 5     6.0
# 7     8.0
# 9    10.0
# dtype: float64

# fillna(): replaces NaNs with a specific value
print(temp1.fillna(0))
# Output:
# 0     1.0
# 1     2.0
# 2     3.0
# 3     0.0
# 4     5.0
# 5     6.0
# 6     0.0
# 7     8.0
# 8     0.0
# 9    10.0
# dtype: float64

print(temp1.fillna(temp1.mean()))
# Output:
# 0     1.0
# 1     2.0
# 2     3.0
# 3     5.0
# 4     5.0
# 5     6.0
# 6     5.0
# 7     8.0
# 8     5.0
# 9    10.0
# dtype: float64

# ==========================================
# 6️⃣ isin()
# ==========================================
# Checks whether each element exists in a given list, returns boolean Series
print(vk.isin([49, 99]))
# Output: Boolean series
print(vk[vk.isin([49, 99])])
# Output:
# match_no
# 82    99
# 86    49
# Name: runs, dtype: int64

# ==========================================
# 7️⃣ apply()
# ==========================================
# apply(): applies a function to each element in the Series
print(movies.apply(lambda x: x.split()))
# Output:
# movie
# Uri: The Surgical Strike                   [Vicky, Kaushal]
# Battalion 609                                 [Vicky, Ahuja]
# ...

print(movies.apply(lambda x: x.split()[0]))
# Output:
# movie
# Uri: The Surgical Strike                  Vicky
# Battalion 609                             Vicky
# ...

print(subs.apply(lambda x: 'good day' if x > subs.mean() else 'bad day'))
# Output:
# 0       bad day
# 1       bad day
# ...
# 360    good day
# 361    good day
# ...

# ==========================================
# 8️⃣ copy()
# ==========================================
# copy(): creates an independent copy of a Series
new = vk.head().copy()
new[1] = 100
print(vk)
# Output (original unchanged):
# match_no
# 1       1
# 2      23
# 3      13
# 4      12
# 5       1
# ...
# 215     7
# Name: runs, Length: 215, dtype: int64



'''

lll ✅ Key Definitions (Interview Spoken Version)

| Method / Attribute              | Spoken Definition                                               |
| ------------------------------- | --------------------------------------------------------------- |
| `sys.getsizeof()`               | Returns memory used by the Series in bytes.                     |
| `between(a,b)`                  | Returns a Boolean mask indicating element lies between a and b. |
| `clip(min,max)`                 | Replaces values <min with min, >max with max.                   |
| `drop_duplicates(keep='first')` | Removes repeated values, keeps first by default.                |
| `duplicated()`                  | Returns a Boolean mask indicating duplicate rows                |
| `isnull()`                      | Returns a Boolean mask indicating missing (NaN) values          |
| `dropna()`                      | Removes all missing (NaN) values from series.                   |
| `fillna(value)`                 | Replace missing (NaN) with specified value (or mean) in a series.          |
| `isin(list)`                    | Checks whether each element exists in a given list, returns boolean Series |
| `apply(func)`                   | Applies a function to every element in the Series.              |
| `copy()`                        | creates an independent copy of a Series                         |



'''