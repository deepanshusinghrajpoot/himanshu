

import numpy as np
import pandas as pd






# =============================================================================
# Pandas MultiIndexing (Hierarchical Indexing) - Interview Spoken Notes
# =============================================================================

# lll Definition:
#     MultiIndexing in pandas means using multiple index levels
#     in rows or columns instead of a single index.

# In simple words:
# It allows us to represent higher-dimensional data
# inside 1D Series or 2D DataFrame.


# =============================================================================
# Why MultiIndexing?
# =============================================================================

# lll MultiIndex Used when one index is not enough.

# Example:
# Branch + Year
# City + Product
# Department + Employee_ID

# It helps organize grouped data efficiently.


# =============================================================================
# Create MultiIndex
# =============================================================================

# lll There are two way to create multiindex.
#     1. from_tuples()
#     2. from_product()


# -----------------------------------------------------------------------------
# 1. from_tuples()
# -----------------------------------------------------------------------------


index_val = [('cse', 2019), ('cse', 2020), ('cse', 2021), ('cse', 2022), ('ece', 2019), ('ece', 2020), ('ece', 2021), ('ece', 2022)]
multi_index_1 = pd.MultiIndex.from_tuples(index_val)

print(multi_index_1)
'''
MultiIndex([('cse', 2019),
            ('cse', 2020),
            ('cse', 2021),
            ('cse', 2022),
            ('ece', 2019),
            ('ece', 2020),
            ('ece', 2021),
            ('ece', 2022)],
           )
'''

print(multi_index_1.levels[0])
'''
Index(['cse', 'ece'], dtype='str')
'''

print(multi_index_1.levels[1])
'''
Index([2019, 2020, 2021, 2022], dtype='int64')
'''



# -----------------------------------------------------------------------------
# 2. from_product()
# -----------------------------------------------------------------------------


multi_index_2 = pd.MultiIndex.from_product([['cse', 'ece'], [2019, 2020, 2021, 2022]])

print(multi_index_2)
'''
MultiIndex([('cse', 2019),
            ('cse', 2020),
            ('cse', 2021),
            ('cse', 2022),
            ('ece', 2019),
            ('ece', 2020),
            ('ece', 2021),
            ('ece', 2022)],
           )
'''

print(multi_index_1.levels[0])
'''
Index(['cse', 'ece'], dtype='str')
'''

print(multi_index_2.levels[1])
'''
Index([2019, 2020, 2021, 2022], dtype='int64')
'''







# =============================================================================
# MultiIndex Series
# =============================================================================

s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8], index=multi_index_2)

print(s)
'''
cse  2019    1
     2020    2
     2021    3
     2022    4
ece  2019    5
     2020    6
     2021    7
     2022    8
dtype: int64
'''


# =============================================================================
# Access Data from MultiIndex Series
# =============================================================================

print(s[('cse', 2022)]) # 4


print(s['cse'])
'''
2019    1
2020    2
2021    3
2022    4
dtype: int64
'''





# =============================================================================
# unstack()
# =============================================================================

# s.unstack()

# lll Interview Spoken:
#     unstack() converts inner row index level into columns.

# Row -> Column

# Example:
# Series MultiIndex becomes DataFrame.



temp = s.unstack()
print(temp)

'''
     2019  2020  2021  2022
cse     1     2     3     4
ece     5     6     7     8
'''


# =============================================================================
# stack()
# =============================================================================

# df.stack()

# lll Interview Spoken:
#     stack() converts column levels into row index.

#     Column -> Row


print(temp.stack())
'''
cse  2019    1
     2020    2
     2021    3
     2022    4
ece  2019    5
     2020    6
     2021    7
     2022    8
dtype: int64
'''



# =============================================================================
# Key Concept
# =============================================================================

# stack() and unstack() are opposite operations.

















# =============================================================================
# Main Purpose of MultiIndexing
# =============================================================================
# lll MultiIndexing is used to represent higher-dimensional data
#     inside lower-dimensional pandas objects:
#     - 1D Object  -> Series
#     - 2D Object  -> DataFrame
#
# It allows multiple index levels on rows and/or columns.
#
# In simple words:
# MultiIndex helps store 3D, 4D, or more logical data
# inside normal Series/DataFrame structure.
# =============================================================================





# =============================================================================
# Example 1 : MultiIndex Rows + Normal Columns
# Logical View = 3D Data
# Inputs needed to get one value:
#   1. Branch
#   2. Year
#   3. Column Name
# =============================================================================

branch_df1 = pd.DataFrame(
    [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8],
        [9, 10],
        [11, 12],
        [13, 14],
        [15, 16],
    ],
    index=multi_index_2,
    columns=['avg_package', 'students']
)

print(branch_df1)

'''
          avg_package  students
cse 2019            1         2
    2020            3         4
    2021            5         6
    2022            7         8
ece 2019            9        10
    2020           11        12
    2021           13        14
    2022           15        16
'''





# =============================================================================
# Example 2 : Normal Rows + MultiIndex Columns
# Logical View = 3D Data
# Inputs needed:
#   1. Year
#   2. City
#   3. Metric
# =============================================================================

branch_df2 = pd.DataFrame(
    [
        [1, 2, 0, 0],
        [3, 4, 0, 0],
        [5, 6, 0, 0],
        [7, 8, 0, 0],
    ],
    index=[2019, 2020, 2021, 2022],
    columns=pd.MultiIndex.from_product(
        [['delhi', 'mumbia'],
         ['avg_package', 'students']]
    )
)

print(branch_df2)

'''
           delhi               mumbia
     avg_package students avg_package students
2019           1        2           0        0
2020           3        4           0        0
2021           5        6           0        0
2022           7        8           0        0
'''



# =============================================================================
# Example 3 : MultiIndex Rows + MultiIndex Columns
# Logical View = 4D Data
# Inputs needed:
#   1. Branch
#   2. Year
#   3. City
#   4. Metric
# =============================================================================

branch_df3 = pd.DataFrame(
    [
        [1, 2, 0, 0],
        [3, 4, 0, 0],
        [5, 6, 0, 0],
        [7, 8, 0, 0],
        [9, 10, 0, 0],
        [11, 12, 0, 0],
        [13, 14, 0, 0],
        [15, 16, 0, 0],
    ],
    index=multi_index_2,
    columns=pd.MultiIndex.from_product(
        [['delhi', 'mumbia'],
         ['avg_package', 'students']]
    )
)

print(branch_df3)

'''
               delhi               mumbia
         avg_package students avg_package students
cse 2019           1        2           0        0
    2020           3        4           0        0
    2021           5        6           0        0
    2022           7        8           0        0
ece 2019           9       10           0        0
    2020          11       12           0        0
    2021          13       14           0        0
    2022          15       16           0        0
'''



# =============================================================================
# What is Dimension?
# =============================================================================
# Dimension means:
# How many coordinates/inputs are required
# to locate one single value.
#
# Example:
# branch_df3.loc[('cse', 2021), ('delhi', 'students')]
#
# Inputs required:
# 1. branch   -> cse
# 2. year     -> 2021
# 3. city     -> delhi
# 4. metric   -> students
#
# Final Value = 6
# =============================================================================



# =============================================================================
# Interview Line
# =============================================================================
# MultiIndexing is a pandas feature used to represent
# higher-dimensional structured data inside Series or
# DataFrame using multiple row/column index levels.
# =============================================================================





















# Stacking and Unstacking
#=========================

# unstack() :- row -> column
# stack() :- column -> row

print(branch_df1)
'''
          avg_package  students
cse 2019            1         2
    2020            3         4
    2021            5         6
    2022            7         8
ece 2019            9        10
    2020           11        12
    2021           13        14
    2022           15        16
'''

# unstack()
#..........

print(branch_df1.unstack())

'''
    avg_package                students
           2019 2020 2021 2022     2019 2020 2021 2022
cse           1    3    5    7        2    4    6    8
ece           9   11   13   15       10   12   14   16
'''


print(branch_df1.unstack().unstack())

'''
avg_package  2019  cse     1
                   ece     9
             2020  cse     3
                   ece    11
             2021  cse     5
                   ece    13
             2022  cse     7
                   ece    15
students     2019  cse     2
                   ece    10
             2020  cse     4
                   ece    12
             2021  cse     6
                   ece    14
             2022  cse     8
                   ece    16
dtype: int64
'''


print(branch_df1.unstack().stack())

'''
          avg_package  students
cse 2019            1         2
    2020            3         4
    2021            5         6
    2022            7         8
ece 2019            9        10
    2020           11        12
    2021           13        14
    2022           15        16
'''


print(branch_df1.unstack().stack().stack())

'''
cse  2019  avg_package     1
           students        2
     2020  avg_package     3
           students        4
     2021  avg_package     5
           students        6
     2022  avg_package     7
           students        8
ece  2019  avg_package     9
           students       10
     2020  avg_package    11
           students       12
     2021  avg_package    13
           students       14
     2022  avg_package    15
           students       16
dtype: int64
'''





print(branch_df2)
'''
           delhi               mumbia
     avg_package students avg_package students
2019           1        2           0        0
2020           3        4           0        0
2021           5        6           0        0
2022           7        8           0        0
'''


print(branch_df2.unstack())
'''
delhi   avg_package  2019    1
                     2020    3
                     2021    5
                     2022    7
        students     2019    2
                     2020    4
                     2021    6
                     2022    8
mumbia  avg_package  2019    0
                     2020    0
                     2021    0
                     2022    0
        students     2019    0
                     2020    0
                     2021    0
                     2022    0
dtype: int64
'''

print(branch_df2.stack())
'''
                  delhi  mumbia
2019 avg_package      1       0
     students         2       0
2020 avg_package      3       0
     students         4       0
2021 avg_package      5       0
     students         6       0
2022 avg_package      7       0
     students         8       0
'''


print(branch_df3)
'''
               delhi               mumbia
         avg_package students avg_package students
cse 2019           1        2           0        0
    2020           3        4           0        0
    2021           5        6           0        0
    2022           7        8           0        0
ece 2019           9       10           0        0
    2020          11       12           0        0
    2021          13       14           0        0
    2022          15       16           0        0
'''


print(branch_df3.unstack())
'''
          delhi                                             mumbia
    avg_package                students                avg_package                students
           2019 2020 2021 2022     2019 2020 2021 2022        2019 2020 2021 2022     2019 2020 2021 2022
cse           1    3    5    7        2    4    6    8           0    0    0    0        0    0    0    0
ece           9   11   13   15       10   12   14   16           0    0    0    0        0    0    0    0
'''

print(branch_df3.unstack().unstack())
'''
delhi   avg_package  2019  cse     1
                           ece     9
                     2020  cse     3
                           ece    11
                     2021  cse     5
                           ece    13
                     2022  cse     7
                           ece    15
        students     2019  cse     2
                           ece    10
                     2020  cse     4
                           ece    12
                     2021  cse     6
                           ece    14
                     2022  cse     8
                           ece    16
mumbia  avg_package  2019  cse     0
                           ece     0
                     2020  cse     0
                           ece     0
                     2021  cse     0
                           ece     0
                     2022  cse     0
                           ece     0
        students     2019  cse     0
                           ece     0
                     2020  cse     0
                           ece     0
                     2021  cse     0
                           ece     0
                     2022  cse     0
                           ece     0
dtype: int64
'''



# head and tail
#---------------

print(branch_df3.head())
'''
               delhi               mumbia
         avg_package students avg_package students
cse 2019           1        2           0        0
    2020           3        4           0        0
    2021           5        6           0        0
    2022           7        8           0        0
ece 2019           9       10           0        0
'''

print(branch_df3.tail())
'''
               delhi               mumbia
         avg_package students avg_package students
cse 2022           7        8           0        0
ece 2019           9       10           0        0
    2020          11       12           0        0
    2021          13       14           0        0
    2022          15       16           0        0
'''


# shape
#-------

print(branch_df3.shape)
'''
(8, 4)
'''


# info
#------

print(branch_df3.info())
'''
<class 'pandas.DataFrame'>
MultiIndex: 8 entries, ('cse', np.int64(2019)) to ('ece', np.int64(2022))
Data columns (total 4 columns):
 #   Column                 Non-Null Count  Dtype
---  ------                 --------------  -----
 0   (delhi, avg_package)   8 non-null      int64
 1   (delhi, students)      8 non-null      int64
 2   (mumbia, avg_package)  8 non-null      int64
 3   (mumbia, students)     8 non-null      int64
dtypes: int64(4)
memory usage: 820.0+ bytes
None
'''


# Extract sinle row
#-------------------

print(branch_df3.loc[('cse', 2022)])
'''
delhi   avg_package    7
        students       8
mumbia  avg_package    0
        students       0
Name: (cse, 2022), dtype: int64
'''


# Extract multiple rows
#-----------------------

print(branch_df3.loc[[('cse', 2019), ('cse', 2020), ('ece', 2019)]])
'''
               delhi               mumbia
         avg_package students avg_package students
cse 2019           1        2           0        0
    2020           3        4           0        0
ece 2019           9       10           0        0
'''


print(branch_df3.loc[('cse', 2019):('ece', 2019):2])
'''
               delhi               mumbia
         avg_package students avg_package students
cse 2019           1        2           0        0
    2021           5        6           0        0
ece 2019           9       10           0        0
'''


print(branch_df3.iloc[0:5:2])
'''
         avg_package students avg_package students
cse 2019           1        2           0        0
    2021           5        6           0        0
ece 2019           9       10           0        0
'''



# Extract single col
#--------------------

print(branch_df3['delhi'])
'''
          avg_package  students
cse 2019            1         2
    2020            3         4
    2021            5         6
    2022            7         8
ece 2019            9        10
    2020           11        12
    2021           13        14
    2022           15        16
'''

print(branch_df3['delhi']['avg_package'])
'''
cse  2019     1
     2020     3
     2021     5
     2022     7
ece  2019     9
     2020    11
     2021    13
     2022    15
Name: avg_package, dtype: int64
'''


# Extract multiple cols
#-----------------------

print(branch_df3.iloc[:, 1:3])
'''
            delhi      mumbia
         students avg_package
cse 2019        2           0
    2020        4           0
    2021        6           0
    2022        8           0
ece 2019       10           0
    2020       12           0
    2021       14           0
    2022       16           0
'''



print(branch_df3.iloc[[0, 4], [1, 2]])
'''
            delhi      mumbia
         students avg_package
cse 2019        2           0
ece 2019       10           0
'''



# sort index
#------------

print(branch_df3.sort_index(ascending=False))
'''
               delhi               mumbia
         avg_package students avg_package students
ece 2022          15       16           0        0
    2021          13       14           0        0
    2020          11       12           0        0
    2019           9       10           0        0
cse 2022           7        8           0        0
    2021           5        6           0        0
    2020           3        4           0        0
    2019           1        2           0        0
'''


# both -> descending -> diff order
#---------------------------------

print(branch_df3.sort_index(ascending=[False, True]))
'''
               delhi               mumbia
         avg_package students avg_package students
ece 2019           9       10           0        0
    2020          11       12           0        0
    2021          13       14           0        0
    2022          15       16           0        0
cse 2019           1        2           0        0
    2020           3        4           0        0
    2021           5        6           0        0
    2022           7        8           0        0
'''


# based on one level
#---------------------

print(branch_df3.sort_index(level=1, ascending=[False]))
'''
               delhi               mumbia
         avg_package students avg_package students
cse 2022           7        8           0        0
ece 2022          15       16           0        0
cse 2021           5        6           0        0
ece 2021          13       14           0        0
cse 2020           3        4           0        0
ece 2020          11       12           0        0
cse 2019           1        2           0        0
ece 2019           9       10           0        0
'''











# =============================================================================
# lll transpose() : Pandas method used to convert rows into columns
#                   and columns into rows.
#
# Key Point:
# - Row index becomes column index
# - Column labels become row index
# - Useful for changing data orientation
# =============================================================================

print(branch_df3.transpose())

'''
                    cse                 ece
                   2019 2020 2021 2022 2019 2020 2021 2022
delhi  avg_package    1    3    5    7    9   11   13   15
       students       2    4    6    8   10   12   14   16
mumbia avg_package    0    0    0    0    0    0    0    0
       students       0    0    0    0    0    0    0    0
'''



# =============================================================================
# lll swaplevel() : Pandas method used to swap MultiIndex levels.
#
# It has parameter
#            axis
#            - axis=0 : Mean swaps row index levels (default)
#            - axis=1 : Mean swaps column MultiIndex levels
#
# Useful when working with hierarchical indexing.
# =============================================================================



print(branch_df3.swaplevel())

'''
               delhi               mumbia
         avg_package students avg_package students
2019 cse           1        2           0        0
2020 cse           3        4           0        0
2021 cse           5        6           0        0
2022 cse           7        8           0        0
2019 ece           9       10           0        0
2020 ece          11       12           0        0
2021 ece          13       14           0        0
2022 ece          15       16           0        0
'''


print(branch_df3.swaplevel(axis=1))

'''
         avg_package students avg_package students
               delhi    delhi      mumbia   mumbia
cse 2019           1        2           0        0
    2020           3        4           0        0
    2021           5        6           0        0
    2022           7        8           0        0
ece 2019           9       10           0        0
    2020          11       12           0        0
    2021          13       14           0        0
    2022          15       16           0        0
'''




