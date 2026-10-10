


#######################################################################################################

# 1. astype(series and dataframe)   
#------------------------------------
# lll is a pandas method used to convert the data type
#     of a Series or DataFrame column into another specified data type.





#=====================================================================================================================================================

# 2. value_counts (series and dataframe) 
# ---------------------------------------
# lll  value_counts is a pandas method used to "Returns frequency of each unique value or unique row in descending order by default."
#      it aplicable on both Series and DataFrame.

# --------------------------------------------------------
# Important Parameters
# --------------------------------------------------------


# subset ->
# specify columns to find frequency

# normalize ->
# True  : returns proportions / percentages
# False : returns counts (default)

# ascending ->
# True  : lowest count first
# False : highest count first (default)

# dropna ->
# True  : excludes NaN values (default)
# False : includes NaN values

# bins ->
# Used for numeric data to group values into intervals
# (mainly for Series)



# --------------------------------------------------------
# Syntax
# --------------------------------------------------------

# Series
# s.value_counts()

# DataFrame
# df.value_counts()

# --------------------------------------------------------
# Example
# --------------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    'city':['Delhi','Mumbai','Delhi','Chennai',None],
    'department':['IT','HR','IT','Sales','HR']
})

# Series
# df['city'].value_counts()

# Output
# Delhi      2
# Mumbai     1
# Chennai    1

# --------------------------------------------------------

# Percentage
# df['city'].value_counts(normalize=True)

# Output
# Delhi      0.50
# Mumbai     0.25
# Chennai    0.25

# --------------------------------------------------------

# Include NaN
# df['city'].value_counts(dropna=False)

# Output
# Delhi      2
# Mumbai     1
# Chennai    1
# NaN        1

# --------------------------------------------------------

# DataFrame row combinations
# df.value_counts(subset=['city', 'department'])

# Output
# city      department
# Delhi     IT            2
# Mumbai    HR            1
# Chennai   Sales         1





#====================================================================================================================================




# sort_values() (Series + DataFrame)
# -----------------------------------
# lll sort_values() is a pandas method used to sort the data
#     based on values in a Series or one or more columns in a DataFrame.

#     Important Parameters
#             it has 
#                by       -> column name(s) to sort (DataFrame only)
#                ascending -> True  : ascending order (default)
#                             False : descending order
#                inplace  -> True  : modifies original data
#                            False : returns new object (default)
#                na_position -> 'first' or 'last' (position of NaN)


# Example
#.........

# Series
# df['marks'].sort_values()

# DataFrame (single column)
# df.sort_values(by='marks')

# DataFrame (multiple columns)
# df.sort_values(by=['marks', 'iq'], ascending=[False, True])





# 3. sort_index (series and dataframe) 
#---------------------------------------
# lll sort_index is a pandas method used to "Sorts Series or DataFrame by its index labels. Default is ascending=True. 
#     Not permanent unless inplace=True."




# 4. reset_index(series and dataframe)
#---------------------------------------
# lll reset_index() is a pandas method used to convert the current index
#     back into a normal column and replace it with a default integer index.




# 5. drop_duplicates (series and dataframe)
#--------------------------------------------
# lll drop_duplicates() is a pandas method used remove duplicate values or duplicate rows 
#     from a Series or DataFrame, keeps first by default. 
#
#     Important Parameters
#         It has parameter
#                  subset       -> specify columns to check duplicates
#                  keep='first' -> keep first occurrence (default)
#                  keep='last'  -> keep last occurrence
#                  keep=False   -> remove all duplicates
#                  inplace      -> If we want to perform permanent changes




# 6. duplicated (series and dataframe)
#---------------------------------------
# lll duplicated() is a pandas method used to Returns a Boolean mask indicating 
#     duplicate values or duplicate rows of a Series or DataFrame.






# 7. isnull / notnull (series and dataframe)
#--------------------------------------------
# lll isnull() : is a pandas method used to Returns a Boolean mask indicating missing (NaN) values of a Series or DataFrame.
# lll notnull() : is a pandas method used to Returns a Boolean mask indicating non-missing (NaN) values of a Series or DataFrame.




# 8. dropna (series and dataframe) 
#-----------------------------------
# lll dropna() is a pandas method used to remove missing values (NaN) from a
#     Series or DataFrame. It deletes rows or columns that contain null(missing) values.
#
#     Important Parameters
#            axis -> 0 : drop rows (default)
#            axis -> 1 : drop columns

#            It also has how, subset, inplace parameter
#            how -> 'any' : drop rows/columns if at least one NaN(missing) value present
#                   'all' : drop rows/columns only if all values are NaN(missing)

#            subset -> specify columns to find missing

#            inplace -> True  : modifies original data
#            inplace -> False : returns new object (default)






# 9. fillna (series and dataframe)
#-----------------------------------
# lll fillna() is a pandas method used to replace missing values (NaN)
#     in a Series or DataFrame with a specified value.

#     Important Parameters
#       It has parameter
#                value   -> value used to replace NaN (scalar, dict, Series)
#                method  -> 'ffill' : forward fill (previous value)
#                           'bfill' : backward fill (next value)
#                axis    -> 0 : fill column-wise (default)
#                           1 : fill row-wise
#                inplace -> True  : modifies original data
#                inplace -> False : returns new object (default)





# 10. drop() (Series + DataFrame) 
#_________________________________
# lll drop() is a pandas method used to remove specified
#     labels (rows or columns) from a Series or DataFrame.
# 
#     Important Parameter
#       It has parameter
#         axis -> 0 : drop rows (default)
#         axis -> 1 : drop columns
#         inplace -> True  : modifies original data
#         inplace -> False : returns new object (default)

# --------------------------------------------------------
# How it Works
# --------------------------------------------------------

# Series    -> removes elements using index labels
# DataFrame -> removes rows or columns based on axis

# --------------------------------------------------------
# Important Parameter
# --------------------------------------------------------

# axis -> 0 : drop rows (default)
# axis -> 1 : drop columns

# inplace -> True  : modifies original data
# inplace -> False : returns new object (default)

# --------------------------------------------------------
# Syntax
# --------------------------------------------------------

# Series
# s.drop(label)

# DataFrame
# df.drop(labels, axis=0/1)

# --------------------------------------------------------
# Example
# --------------------------------------------------------

# Series
# s.drop(2)

# DataFrame (drop row)
# df.drop(2, axis=0)

# DataFrame (drop column)
# df.drop('marks', axis=1)

# --------------------------------------------------------
# Key Point
# --------------------------------------------------------

# Uses labels (not index positions) for removal.

# --------------------------------------------------------
# One-Line Answer
# --------------------------------------------------------

# drop() removes specified rows or columns using labels
# from a Series or DataFrame.






# 11. apply (Series + DataFrame) 
#________________________________
# lll  apply() is a pandas method used to apply a function
#      to each element of a Series or along rows/columns
#      of a DataFrame.

#      Important Parameter
#          axis -> 0 : apply function on columns (default)
#          axis -> 1 : apply function on rows

# --------------------------------------------------------
# How it Works
# --------------------------------------------------------

# Series   -> applies function to each value
# DataFrame -> applies function row-wise or column-wise

# --------------------------------------------------------
# Important Parameter
# --------------------------------------------------------

# axis -> 0 : apply function on columns (default)
# axis -> 1 : apply function on rows

# --------------------------------------------------------
# Example
# --------------------------------------------------------

# Series
# df['marks'].apply(lambda x: x + 5)

# DataFrame
# df.apply(lambda x: x.max(), axis=0)

# --------------------------------------------------------
# One-Line Answer
# --------------------------------------------------------

# apply() is used to apply a custom function on Series
# or DataFrame (row-wise or column-wise).






# 12. isin (Series + DataFrame)
#________________________________
#  lll isin() is a pandas method used to check whether each
#      element in a Series or DataFrame is present in a given
#      list, set, or collection of values.

# It returns a Boolean result (True/False) for each element.

# --------------------------------------------------------
# How it Works
# --------------------------------------------------------

# Series    -> checks each value in the Series
# DataFrame -> checks each value in the entire DataFrame

# --------------------------------------------------------
# Example
# --------------------------------------------------------

# Series
# df['city'].isin(['Delhi', 'Mumbai'])

# DataFrame
# df.isin([10, 20, 30])

# --------------------------------------------------------
# Use Case
# --------------------------------------------------------

# Filtering data based on multiple values

# df[df['city'].isin(['Delhi', 'Mumbai'])]

# --------------------------------------------------------
# One-Line Answer
# --------------------------------------------------------

# isin() checks membership of values and returns
# True/False for each element.





# 13. nlargest() (Series + DataFrame) 
#_____________________________________
# lll nlargest() is a pandas method used to return the top 'n'
#     largest values from a Series or rows from a DataFrame
#     based on a specified column.



# It is more efficient than sorting the entire dataset.

# --------------------------------------------------------
# How it Works
# --------------------------------------------------------

# Series    -> returns top n largest values
# DataFrame -> returns rows with highest values in a column

# --------------------------------------------------------
# Syntax
# --------------------------------------------------------

# Series
# s.nlargest(n)

# DataFrame
# df.nlargest(n, 'column_name')

# --------------------------------------------------------
# Example
# --------------------------------------------------------

# Series
# df['marks'].nlargest(3)

# DataFrame
# df.nlargest(3, 'marks')

# --------------------------------------------------------
# Key Point
# --------------------------------------------------------

# Faster than sort_values(ascending=False).head(n)
# because it avoids full sorting.

# --------------------------------------------------------
# One-Line Answer
# --------------------------------------------------------

# nlargest() returns the top n highest values efficiently
# from a Series or DataFrame.









# 14. nsmallest() (Series + DataFrame)
#______________________________________

# lll nsmallest() is a pandas method used to return the
#     top 'n' smallest (lowest) values from a Series or
#     rows from a DataFrame based on a specified column.

# It is more efficient than sorting the entire dataset.

# --------------------------------------------------------
# How it Works
# --------------------------------------------------------

# Series    -> returns n smallest values
# DataFrame -> returns rows with lowest values in a column

# --------------------------------------------------------
# Syntax
# --------------------------------------------------------

# Series
# s.nsmallest(n)

# DataFrame
# df.nsmallest(n, 'column_name')

# --------------------------------------------------------
# Example
# --------------------------------------------------------

# Series
# df['marks'].nsmallest(3)

# DataFrame
# df.nsmallest(3, 'marks')

# --------------------------------------------------------
# Key Point
# --------------------------------------------------------

# Faster than sort_values().head(n)
# because it avoids full sorting.

# --------------------------------------------------------
# One-Line Answer
# --------------------------------------------------------

# nsmallest() returns the lowest n values efficiently
# from a Series or DataFrame.




# =============================================================================
# where()
# =============================================================================

# lll where():
#     "Sir, where() is a pandas Series and DataFrame method.
#      It keeps values where condition is True,
#      and replaces values where condition is False.

import pandas as pd

s = pd.Series([10, 20, 30])

# Boolean Indexing
print(s[s > 15])

# where()
print(s.where(s > 15))

'''
1    20
2    30
dtype: int64

0     NaN
1    20.0
2    30.0
dtype: float64
'''

# =============================================================================
# query()
# =============================================================================

# lll query():
#     "Sir, query() is a pandas DataFrame method used to filter
#      rows using a condition written as a string expression.
#      It makes filtering more readable."

import pandas as pd

df = pd.DataFrame({
    "Name": ["Aman", "Riya", "Karan"],
    "Age": [22, 25, 30],
    "Salary": [25000, 40000, 50000]
})

print(df.query("Age > 23"))




# 15. copy() (Series + DataFrame)
#__________________________________

# lll copy() is a pandas method used to create a new independent
#     copy of a Series or DataFrame.

#     Changes made to the copied object do not affect the original
#     data, ensuring safe modifications.


# --------------------------------------------------------
# How it Works
# --------------------------------------------------------

# Series    -> creates a separate copy of the Series
# DataFrame -> creates a separate copy of the DataFrame

# --------------------------------------------------------
# Important Parameter
# --------------------------------------------------------

# deep -> True  : creates a full independent copy (default)
# deep -> False : creates a shallow copy (references data)

# --------------------------------------------------------
# Example
# --------------------------------------------------------

# df_copy = df.copy()

# df_copy['marks'] = df_copy['marks'] + 10
# (Original df remains unchanged)

# --------------------------------------------------------
# Key Point
# --------------------------------------------------------

# Prevents unintended changes to original data.

# --------------------------------------------------------
# One-Line Answer
# --------------------------------------------------------

# copy() creates an independent duplicate of data to avoid
# modifying the original object.







# 16. nunique() (Series + DataFrame)
#____________________________________

# lll nunique() is a pandas method used to count the number
#     of distinct (unique) values in a Series or each column
#     of a DataFrame.

#     Important Parameter
#        It has a dropna parameter.
#          dropna -> True  : ignores NaN(missing) values (default)
#          dropna -> False : counts NaN(missing) as a unique value



# --------------------------------------------------------
# How it Works
# --------------------------------------------------------

# Series    -> returns a single count of unique values
# DataFrame -> returns unique count for each column


# --------------------------------------------------------
# Syntax
# --------------------------------------------------------

# Series
# s.nunique()

# DataFrame
# df.nunique()

# --------------------------------------------------------
# Example
# --------------------------------------------------------

# Series
# df['marks'].nunique()

# DataFrame
# df.nunique()

# Including NaN
# df['marks'].nunique(dropna=False)

# --------------------------------------------------------
# Key Point
# --------------------------------------------------------

# Helps identify distinct values quickly for analysis.

# --------------------------------------------------------
# One-Line Answer
# --------------------------------------------------------

# nunique() returns the count of unique values in a
# Series or per column in a DataFrame.





# =============================================================================
# Interview Spoken Definition
# =============================================================================

# lll describe():
#            "Sir, describe() is a pandas method used to generate
#            summary statistics of a Series or DataFrame.
#            It quickly gives measures like count, mean,
#            standard deviation, minimum, maximum, and quartiles."

# =============================================================================
# Important Parameters
# =============================================================================

# include='all'      -> include all columns (numeric + object + category)
# exclude=...        -> exclude specific data types
# percentiles=[...]  -> custom percentile values
# datetime_is_numeric=True -> treat datetime as numeric


df = pd.DataFrame({
    "Age": [22, 25, 28, 30, 35],
    "Salary": [25000, 30000, 40000, 50000, 60000],
    "Name": ["Aman", "Riya", "Karan", "Neha", "Pooja"],
    "Join_Date": pd.to_datetime([
        "2022-01-10",
        "2021-06-15",
        "2023-03-20",
        "2020-09-01",
        "2024-02-05"
    ])
})

df.describe(percentiles=[0.10, 0.50, 0.90])

'''
             Age       Salary
count   5.000000      5.000000
mean   28.000000  41000.000000
std     4.949747  13601.470508
min    22.000000  25000.000000
10%    23.2      27000.0
50%    28.0      40000.0
90%    33.0      56000.0
max    35.0      60000.0
'''


df.describe(datetime_is_numeric=True)
'''
                       Join_Date
count                         5
mean      2022-04-18 04:48:00
min       2020-09-01
25%       2021-06-15
50%       2022-01-10
75%       2023-03-20
max       2024-02-05
'''





#================================================================================================


#  17. set_index(dataframe)
#--------------------------
# lll “Sir, set_index() is a pandas dataframe methode used to convert an existing column into the index of a DataFrame.”
#     It has parameter
#            inplace 




# 18. rename(dataframe)
#----------------------
# rename() is a pandas DataFrame method used to change the names of
# columns or index labels without modifying the original data.

# Important Parameters
#           columns -> dictionary used to rename column names
#           index   -> dictionary used to rename index labels
#           inplace -> True makes the change permanent




#================================================================================================



# =============================================================================
# 19. rank() (Series)
# =============================================================================

# lll rank() is a pandas Series method used to assign ranks
# to values based on their order.

# By default:
# Smallest value gets Rank 1

# If duplicate values exist:
# rank() gives average rank by default..

# Important Parameters
# ---------------------

# ascending ->
# True  : smallest gets rank 1 (default)
# False : largest gets rank 1

# method ->
# 'average' : average rank (default)
# 'min'     : lowest rank
# 'max'     : highest rank
# 'first'   : order of appearance
# 'dense'   : consecutive ranks

# na_option ->
# 'keep'   : keep NaN
# 'top'    : rank NaN first
# 'bottom' : rank NaN last

# pct ->
# True : percentage rank

# eg:

# [10, 20, 20, 30, 40]

# | Value | Position |
# | ----- | -------- |
# | 10    | 1        |
# | 20    | 2        |
# | 20    | 3        |
# | 30    | 4        |
# | 40    | 5        |

# | Value | Rank |
# | ----- | ---- |
# | 10    | 1    |
# | 20    | 2    |
# | 20    | 2    |
# | 30    | 3    |
# | 40    | 4    |


# Final Output for Each Method

# | Method  | Result                |
# | ------- | --------------------- |
# | average | `[1, 2.5, 2.5, 4, 5]` |
# | min     | `[1, 2, 2, 4, 5]`     |
# | max     | `[1, 3, 3, 4, 5]`     |
# | first   | `[1, 2, 3, 4, 5]`     |
# | dense   | `[1, 2, 2, 3, 4]`     |





# hasnans : Series
#------------------
# hasnans is a pandas Series attribute used to quickly check
# whether a Series contains any missing values (NaN) or not.
# It returns:
# True  -> if at least one NaN exists
# False -> if no NaN exists





# 21. unique() (Series)
#______________________

# unique() is a pandas Series method used to return
# all distinct (unique) values present in the Series.

# It does not return the count, only the unique values.

# --------------------------------------------------------
# How it Works
# --------------------------------------------------------

# Series -> returns array of unique values

# --------------------------------------------------------
# Syntax
# --------------------------------------------------------

# s.unique()

# --------------------------------------------------------
# Example
# --------------------------------------------------------

# df['city'].unique()

# Output -> ['Delhi', 'Mumbai', 'Chennai']

# --------------------------------------------------------
# Key Point
# --------------------------------------------------------

# - Returns values, not count
# - Output is in array format
# - Order is preserved (no sorting)

# --------------------------------------------------------
# One-Line Answer
# --------------------------------------------------------

# unique() returns all distinct values from a Series
# without counting them.

















# 16. corr (series and dataframe) :- gpt give perfect interview spoken diffinition

# 18. insert (series and dataframe) :- gpt give perfect interview spoken diffinition

################################################################


















import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os





path_dir = os.path.dirname(__file__)

path_file_movies = os.path.join(path_dir, '../../1_Dataset/movies.csv')
path_file_ipl_matches = os.path.join(path_dir, '../../1_Dataset/ipl-matches.csv')


movies = pd.read_csv(path_file_movies)
ipl_matches = pd.read_csv(path_file_ipl_matches)



print(movies)
#                                    title_x  ...              release_date
# 0                 Uri: The Surgical Strike  ...     11 January 2019 (USA)
# 1                            Battalion 609  ...   11 January 2019 (India)
# 2     The Accidental Prime Minister (film)  ...     11 January 2019 (USA)
# 3                          Why Cheat India  ...     18 January 2019 (USA)
# r  ...  16 November 2001 (India)
# 1626                       Sabse Bada Sukh  ...                       NaN   
# 1627                                 Daaka  ...     1 November 2019 (USA)   
# 1628                              Humsafar  ...     TV Series (2011–2012)   

# [1629 rows x 18 columns]


print(movies.columns)
# Index(['title_x', 'imdb_id', 'poster_path', 'wiki_link', 'title_y',
#        'original_title', 'is_adult', 'year_of_release', 'runtime', 'genres',
#        'imdb_rating', 'imdb_votes', 'story', 'summary', 'tagline', 'actors',
#        'wins_nominations', 'release_date'],
#       dtype='str')



print(ipl_matches)
#           ID        City  ...        Umpire1         Umpire2
# 0    1312200   Ahmedabad  ...    CB Gaffaney     Nitin Menon
# 1    1312199   Ahmedabad  ...    CB Gaffaney     Nitin Menon
# 2    1312198     Kolkata  ...  J Madanagopal        MA Gough
# 3    1312197     Kolkata  ...   BNJ Oxenford       VK Sharma
# 4    1304116      Mumbai  ...   AK Chaudhary   NA Patwardhan
# ..       ...         ...  ...            ...             ...
# 945   335986     Kolkata  ...      BF Bowden     K Hariharan
# 946   335985      Mumbai  ...       SJ Davis       DJ Harper
# 947   335984       Delhi  ...      Aleem Dar  GA Pratapkumar
# 948   335983  Chandigarh  ...      MR Benson      SL Shastri
# 949   335982   Bangalore  ...      Asad Rauf     RE Koertzen

# [950 rows x 20 columns]



print(ipl_matches.columns)
# Index(['ID', 'City', 'Date', 'Season', 'MatchNumber', 'Team1', 'Team2',     
#        'Venue', 'TossWinner', 'TossDecision', 'SuperOver', 'WinningTeam',   
#        'WonBy', 'Margin', 'method', 'Player_of_Match', 'Team1Players',      
#        'Team2Players', 'Umpire1', 'Umpire2'],
#       dtype='str')







print(ipl_matches.info())
# <class 'pandas.DataFrame'>
# RangeIndex: 950 entries, 0 to 949
# Data columns (total 20 columns):
#      Column           Non-Null Count  Dtype
# ---  ------           --------------  -----
#  0   ID               950 non-null    int64
#  1   City             899 non-null    str
#  2   Date             950 non-null    str
#  3   Season           950 non-null    str
#  4   MatchNumber      950 non-null    str
#  5   Team1            950 non-null    str
#  6   Team2            950 non-null    str
#  7   Venue            950 non-null    str
#  8   TossWinner       950 non-null    str
#  9   TossDecision     950 non-null    str
#  10  SuperOver        946 non-null    str
#  11  WinningTeam      946 non-null    str
#  12  WonBy            950 non-null    str
#  13  Margin           932 non-null    float64
#  14  method           19 non-null     str
#  15  Player_of_Match  946 non-null    str
#  16  Team1Players     950 non-null    str
#  17  Team2Players     950 non-null    str
#  18  Umpire1          950 non-null    str
#  19  Umpire2          950 non-null    str
# dtypes: float64(1), int32(1), str(18)
# memory usage: 144.9 KB
# None








# ==================================
# Important DataFrame Functions
# ==================================


# -------------------------------------------------
# 1. astype()
# -------------------------------------------------

# Interview Spoken Definition:
# astype() is a pandas method used to convert the data type
# of a Series or DataFrame column into another specified data type.


ipl_matches['ID'] = ipl_matches['ID'].astype('int32')

print(ipl_matches.info())

# <class 'pandas.DataFrame'>
# RangeIndex: 950 entries, 0 to 949
# Data columns (total 20 columns):
#      Column           Non-Null Count  Dtype
# ---  ------           --------------  -----
#  0   ID               950 non-null    int32
#  1   City             899 non-null    str
#  2   Date             950 non-null    str
#  3   Season           950 non-null    str
#  4   MatchNumber      950 non-null    str
#  5   Team1            950 non-null    str
#  6   Team2            950 non-null    str
#  7   Venue            950 non-null    str
#  8   TossWinner       950 non-null    str
#  9   TossDecision     950 non-null    str
#  10  SuperOver        946 non-null    str
#  11  WinningTeam      946 non-null    str
#  12  WonBy            950 non-null    str
#  13  Margin           932 non-null    float64
#  14  method           19 non-null     str
#  15  Player_of_Match  946 non-null    str
#  16  Team1Players     950 non-null    str
#  17  Team2Players     950 non-null    str
#  18  Umpire1          950 non-null    str
#  19  Umpire2          950 non-null    str
# dtypes: float64(1), int32(1), str(18)



# ==================================
# Example DataFrame
# ==================================

marks = pd.DataFrame(
    [
        [100, 80, 10],
        [90, 70, 7],
        [120, 100, 14],
        [80, 70, 14],
        [80, 70, 14]
    ],
    columns=['iq', 'marks', 'package']
)

print(marks)

#     iq  marks  package
# 0  100     80       10
# 1   90     70        7
# 2  120    100       14
# 3   80     70       14
# 4   80     70       14



# -------------------------------------------------
# 2. value_counts()
# -------------------------------------------------

# Interview Spoken Definition:
# value_counts() is a pandas method used to count the frequency
# of unique values in a Series or rows in a DataFrame,
# and it returns the result in descending order.


# Series Example
print(marks.iloc[4].value_counts())

# 80    1
# 70    1
# 14    1
# Name: count, dtype: int64


# DataFrame Example
print(marks.value_counts())

# iq   marks  package
# 80   70     14         2
# 100  80     10         1
# 90   70     7          1
# 120  100    14         1
# Name: count, dtype: int64



# ==================================
# Interview Questions Practice
# ==================================


# -------------------------------------------------
# Question:
# Find which player has won most "Player of the Match"
# awards in Final and Qualifier matches
# -------------------------------------------------

print(
    ipl_matches[~ipl_matches['MatchNumber'].str.isdigit()]
    ['Player_of_Match']
    .value_counts()
)

# Output Example:
# F du Plessis     3
# KA Pollard       3
# SK Raina         3
# JJ Bumrah        2
# SR Watson        2
# ...


# Explanation:
# ~ipl_matches['MatchNumber'].str.isdigit()
# selects matches that are NOT regular league matches
# (i.e., Final, Qualifier, Eliminator)



# -------------------------------------------------
# Question:
# After winning toss what percentage of teams
# choose bat or field
# -------------------------------------------------

ipl_matches['TossDecision'].value_counts().plot(kind='pie')

plt.show()

print(ipl_matches['TossDecision'].value_counts())

# TossDecision
# field    599
# bat      351
# Name: count, dtype: int64



# -------------------------------------------------
# Question:
# How many matches each team has played
# -------------------------------------------------

print(ipl_matches['Team1'].value_counts())


(
    ipl_matches['Team1'].value_counts() +
    ipl_matches['Team2'].value_counts()
).plot(kind='bar')

plt.show()