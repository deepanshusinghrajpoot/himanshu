
import pandas as pd
import numpy as np





# ==========================================
# Pandas: Introduction & Series
# ==========================================

# What is Pandas
# ------------------
# lll Pandas is a fast, powerful, flexible, and easy-to-use
#     open-source Python library for data analysis and manipulation.
#     Built on top of Python, it is widely used for working with tabular data.

# lll We know pandas has object like.
#     Series and DataFrame

#  Pandas Series
#=================
# lll A Pandas Series is a 1-dimensional labeled array capable of holding data of any type (integer, float, string, etc.)

# There are two way to create pandas series.
# 1. Using Python list.
# 2. Using Python dictionary.


# lll We also know that a Pandas Series can be created directly from a CSV file.

# - lll read_csv() reads the CSV file as a DataFrame by default.
# - lll squeeze() converts a single-column DataFrame into a Series.


# Pandas DataFrame
#==================
# lll A DataFrame is a 2-dimensional labeled data structure.


# lll In Pandas, there are two ways to create a custom index.

# lll First is using the index parameter:
#     It is used while creating a Series or DataFrame manually.

# lll Second is using the index_col parameter:
#     It is used while loading data from any sources,
#     where a specific column is set as the index.






# Series has attributes.
#========================
# dtype :- dtype is a pandas attribute shows the data type of the values stored in the Series.
# name :- name is a pandas attribute used to get or set the name of a Series.
# is_unique :- is_unique is a pandas attribute returns True if all the values in the Series are unique; otherwise False."



# DataFrame has attributes
#==========================
# dtypes :- dtypes is a pandas attribute Shows the data type of the values of each column in a DataFrame.
# columns :-  columns is a pandas attribute returns the name of all columns of the DataFrame.



# Series and DataFrame have common attribute
#============================================
# shape :- shape is a pandas attribute used to get the dimensions of data.
#          It returns a tuple in the form:(rows, columns)
# index :- is pandas attribute represents the labels of the Series or DataFrame. 
#          Acts like row identifiers.
# values :- is pandas attribute returns the underlying data of the Series or DataFrame as a NumPy array.
# size :- size is a pandas attribute used to return the total number of elements in a Series or DataFrame.
#         It is rows multiplied by columns.





# methods of Series or DataFrame
#================================



#*****************************************************************************************************
#  Index Operations of Series and Dataframe
#*******************************************
# set_index(dataframe)
# reset_index(series and dataframe)

# set_index(dataframe)
#----------------------
# lll “Sir, set_index() is a pandas dataframe methode used to convert an existing column into the index of a DataFrame.”
#     It has parameter
#            inplace 

# reset_index(series and dataframe)
# ---------------------------------
#            reset_index() is a pandas method used to convert the current index
#            back into a normal column and replace it with a default integer index.




#*******************************************************************************************************
# for Data Type Conversion of Series and DataFrame
#*************************************************
# astype()
# to_numeric()
# to_datetime()


# astype(series and dataframe)
# ----------------------------
#            is a pandas method used to convert the data type
#            of a Series or DataFrame column into another specified data type.







#*******************************************************************************************************
# for Row & Column Operations
#*****************************
# drop()
# rename()
# insert()
# assign()


# drop() (Series + DataFrame)
# --------------------------- 
#           drop() is a pandas method used to remove specified
#           labels (rows or columns) from a Series or DataFrame.
#      It has parameters
#         axis -> 0 : drop rows (default)
#         axis -> 1 : drop columns
#         inplace -> True  : modifies original data
#         inplace -> False : returns new object (default)


#  rename(dataframe) 
#---------------------
# rename() is a pandas DataFrame method used to change the names of
# columns or index labels without modifying the original data.

# Important Parameters
#         columns -> dictionary used to rename column names
#         index   -> dictionary used to rename index labels
#         inplace -> True makes the change permanent







#*******************************************************************************************************
#  Data Inspection of Series and Dataframe
# ****************************************

# methods
#.........
# head(series and dataframe)       tail(series and dataframe)       sample(series and dataframe)
# info(series and dataframe)       describe(series and dataframe)

# attributes
#............
# shape        columns      index
# dtypes



# head() :- "Returns the first n elements of the Series or DataFrame. Default is 5 if n not provided."
# tail() :- "Returns the last n elements of the Series or DataFrame. Default is 5 if n not provided."
# sample() :- "Returns random n elements of the Series or DataFrame. Default is 1 if n not provided."


# info(series and dataframe)
# --------------------------
#                 is a pandas method used to display a concise summary
#                 of a Series or DataFrame.
#        It gives information such as:
#           - Index details
#           - Number of entries
#           - Column names
#           - Non-null counts  
#           - Data types (dtype)
#           - Memory usage



# describe(series and dataframe)
# ------------------------------
#            describe() is a pandas method used to generate
#            statistics summary of a Series or DataFrame.
#            It quickly gives information like count, mean,
#            standard deviation, minimum, maximum, and quartiles.

#      It has Parameters
#           include='all'      -> include all columns (numeric + object + category)
#           exclude=...        -> exclude specific data types
#           percentiles=[...]  -> custom percentile values
#           datetime_is_numeric=True -> treat datetime as numeric






#************************************************************************************************************
# For Sorting & Ranking of Series and Dataframe
# **********************************************
# value_counts(series and dataframe)   sort_values(series and dataframe)    sort_index(series and dataframe)
# rank(series)           nlargest(series and dataframe)
# nsmallest(series and dataframe)



# value_counts (series and dataframe)
# -----------------------------------
#            value_counts is a pandas method used to "Returns frequency 
#            of each unique value or unique row in descending order by default."
#    It has parameters
#            subset : indicate : -> specify columns to find frequency
#            normalize  
#                      is equal to -> True : mean : returns proportions / percentages
#                      is equal to  -> False : mean : returns counts (default)
#            ascending
#                      is equal to -> True : mean : lowest count first
#                      is equal to  -> False : mean : highest count first (default)
#            dropna
#                    is equal to -> True : mean : excludes NaN(missing) values (default)
#                    is equal to  -> False : mean : includes NaN(missing) values
#            bins -> Used for numeric data to group values into intervals


# sort_values() (Series + DataFrame)
# ----------------------------------
#           sort_values() is a pandas method used to sort the data
#           based on values in a Series or one or more columns in a DataFrame.
#     It has parameters 
#                by : indicate : -> specify columns to sort DataFrame
#                ascending
#                         is equal to -> True : mean : ascending order (default)
#                         is equal to  -> False : mean : descending order
#                inplace 
#                         is equal to -> True : mean : modifies original data
#                         is equal to  -> False : mean : returns new object (default)
#                na_position -> 'first' or 'last' (specify the position of missing value(NaN))


# sort_index (series and dataframe) 
# ---------------------------------
#            sort_index is a pandas method used to "Sorts Series or DataFrame by its index labels. 
#     It has parameters 
#            Default is ascending=True. 
#            Not permanent unless inplace=True."


# rank(Series)
# ------------
#            rank() is a pandas Series method used to assign ranks
#            to values based on their order.
#     It has parameters
#            ascending 
#                  is equal to -> True : mean : smallest value gets rank 1 (default)
#                  is equal to  -> False : mean : largest value gets rank 1
#            method has values
#                  'average' : by default it assign average rank
#                  'min'     : lowest rank
#                  'max'     : highest rank
#                  'first'   : order of appearance
#                  'dense'   : consecutive ranks
#            na_option has values
#                  'keep'   : keep NaN
#                  'top'    : rank NaN first
#                  'bottom' : rank NaN last
#            pct
#                  True : percentage rank


# nlargest() (Series + DataFrame) 
# -------------------------------
#            nlargest() is a pandas method used to return the top 'n'
#            largest values from a Series or rows from a DataFrame
#            based on a specified column.


# nsmallest() (Series + DataFrame)
# --------------------------------
#            nsmallest() is a pandas method used to return the
#            top 'n' smallest (lowest) values from a Series or
#            rows from a DataFrame based on a specified column.





# **************************************************************************************************
# for Missing Values of Series and Dataframe
# *******************************************
# isna(series and dataframe)       notna(series and dataframe)
# dropna(series and dataframe)     fillna(series and dataframe)

# isnull(series and dataframe) or isna(series and dataframe)
# ----------------------------------------------------------
#           is a pandas method used to Returns a Boolean mask indicating missing (NaN) values of a Series or DataFrame.

# notnull(series and dataframe) or notna(series and dataframe)
# ------------------------------------------------------------
#           is a pandas method used to Returns a Boolean mask indicating non-missing (NaN) values of a Series or DataFrame.

# dropna (series and dataframe) 
# -----------------------------
#           dropna() is a pandas method used to remove missing values (NaN) from a
#           Series or DataFrame. It deletes rows or columns that contain null(missing) values.
#     It has parameters
#            subset : indicate : -> specify columns to check missing
#            axis
#               axis = 0 mean : drop rows (default)
#               axis = 1 mean : drop columns
#            how : has values
#               how ='any' mean : drop rows/columns if at least one NaN(missing) value present
#               how ='all' mean : drop rows/columns only if all values are NaN(missing)
#            inplace
#               inplace = True  mean : modifies original data
#               inplace = False : returns new object (default)

# fillna (series and dataframe)
# ------------------------------
#           fillna() is a pandas method used to replace missing values (NaN)
#           in a Series or DataFrame with a specified value.
#     It has parameters
#                value   -> value used to replace NaN (scalar, dict, Series)
#                method  -> 'ffill' : forward fill (previous value)
#                           'bfill' : backward fill (next value)
#                axis    -> 0 : fill column-wise (default)
#                           1 : fill row-wise
#                inplace -> True  : modifies original data
#                           False : returns new object (default)





# ****************************************************************************************************
# for Handling Duplicate of Series and Dataframe
# **********************************************

# duplicated()        drop_duplicates()  
# nunique()            


# duplicated (series and dataframe)
# ---------------------------------
#           duplicated() is a pandas method used to Returns a Boolean mask indicating 
#           duplicate values or duplicate rows of a Series or DataFrame.


# It has parameters
#         subset → columns to consider when checking duplicates
#         keep='first' → keep first occurrence as False
#         keep='last' → keep last occurrence as False
#         keep=False → mark all duplicates as True


# drop_duplicates (series and dataframe)
# --------------------------------------
#            drop_duplicates() is a pandas method used remove duplicate values or duplicate rows 
#            from a Series or DataFrame, keeps first by default. 
#     It has parameters
#                  subset : indicate : -> specify columns to check duplicates
#                  keep
#                      keep='first' : mean : -> keep first occurre nce (default)
#                      keep='last'  : mean : -> keep last occurrence
#                      keep=False   : mean : -> remove all duplicates
#                  inplace 
#                         is equal to -> True : mean : modifies original data
#                         is equal to  -> False : mean : returns new object (default)
#                  ignore_index    ->        Reset the index after removing duplicates



# nunique() (Series and DataFrame)
# --------------------------------
#            nunique() is a pandas method used to count the number of distinct (unique) values
#            in a Series or each column of a DataFrame.
#       It has a dropna parameter.
#          dropna -> True  : ignores NaN(missing) values (default)
#                 -> False : counts NaN(missing) as a unique value






#**********************************************************************************************************************
# for Selection of row or col of Series and Dataframe
#****************************************************
# loc[]        iloc[]


# loc (Label Location)
#----------------------
# Interview Definition
# lll loc is used to select rows and columns from a DataFrame using
#     labels index instead of integer index positions.

#     Syntax
#        dataframe.loc[row_label, column_label]

#     Slicing
#        dataframe.loc[start_row:end_row, start_col:end_col]

#     Important Rule
#        start → included
#        end   → included



# iloc (Index Location)
#------------------------
# Interview Definition
# lll iloc is used to select rows and columns from a
#     DataFrame using integer index positions.

# Syntax
# dataframe.iloc[row_index, column_index]

# Slice Syntax
# dataframe.iloc[start_row:end_row:step , start_col:end_col:step]

# Important Rule
# start → included
# end   → excluded




# Fancy Indexing in loc[] and iloc[]
# ----------------------------------

# Interview Definition
# lll Fancy Indexing is used to select multiple specific
#     rows and/or columns at once by passing a list.

# loc[] → uses labels
# iloc[] → uses integer index positions

# Syntax
# dataframe.loc[[row_label1, row_label2], [col_label1, col_label2]]

# Example
# df.loc[['A', 'C', 'E'], ['Name', 'Salary']]




# Selecting Columns From a DataFrame (Pandas)
# ...........................................

# dataframe['column']           → returns Series
# dataframe[['col1','col2']]    → returns DataFrame

# Single []   → Series
# Double [[]] → DataFrame



# Boolean Indexing of Series and DataFrame
# ........................................

'''

🔷 Logical Operators in Pandas
===============================

| Operator | Symbol | Meaning                             | Example                                  |
| -------- | ------ | ----------------------------------- | ---------------------------------------- |
| AND      | `&`    | Both conditions must be True        | `(df['marks'] > 50) & (df['iq'] > 100)`  |
| OR       | `|`   | At least one condition must be True | `(df['marks'] > 50) | (df['iq'] > 100)` |
| NOT      | `~`    | Reverse the condition               | `~(df['marks'] > 50)`                    |


🔷 Comparison Operators in Pandas
===================================

| Operator              | Symbol | Meaning           | Example             |
| --------------------- | ------ | ----------------- | ------------------- |
| Equal to              | `==`   | Checks equality   | `df['marks'] == 50` |
| Not equal to          | `!=`   | Checks inequality | `df['marks'] != 50` |
| Greater than          | `>`    | Greater value     | `df['marks'] > 50`  |
| Less than             | `<`    | Smaller value     | `df['marks'] < 50`  |
| Greater than or equal | `>=`   | ≥ condition       | `df['marks'] >= 50` |
| Less than or equal    | `<=`   | ≤ condition       | `df['marks'] <= 50` |


🔷 Arithmetic Operators in Pandas
==================================

| Operator       | Symbol | Meaning           | Example              |
| -------------- | ------ | ----------------- | -------------------- |
| Addition       | `+`    | Adds values       | `df['A'] + df['B']`  |
| Subtraction    | `-`    | Subtracts values  | `df['A'] - df['B']`  |
| Multiplication | `*`    | Multiplies values | `df['A'] * df['B']`  |
| Division       | `/`    | Divides values    | `df['A'] / df['B']`  |
| Floor Division | `//`   | Integer division  | `df['A'] // df['B']` |
| Modulus        | `%`    | Remainder         | `df['A'] % df['B']`  |
| Power          | `**`   | Exponentiation    | `df['A'] ** 2`       |


'''



# ****************************************************************************************************
# for Filtering & Conditions of Series and Dataframe
# ***************************************************
# isin()                           between()
# where()                          query() 


# isin (Series and DataFrame)
# ---------------------------
#      isin() is a pandas method used to check whether each element in a Series or DataFrame 
#      is present in a given list, set, or collection of values.


# between(Series)
# ---------------
#      between() is a pandas Series method used to check whether values lie between a lower and upper limit.
#      It returns True or False for each value."


# where(Series and DataFrame)
# ----------------------------
#      where() is a pandas Series and DataFrame method. It keeps values where condition is True,
#      and replaces values where condition is False.
#   Note : Boolean indexing is better for flltering data.


# query(DataFrame)
# -----------------
#      query() is a pandas DataFrame method used to filter rows using a condition written as a string expression.
#
#      It makes filtering more readable."

#   Note : Both are good — depends on use case.
#          Boolean Indexing → more common, flexible, works on Series + DataFrame
#          query() → cleaner syntax, better readability for DataFrame filtering






#**************************************************************************************************
# For Grouping & Aggregation of Series and Dataframe
#***************************************************

# groupby()    agg()
# filter()     transform()


# groupby() in Pandas
#***********************
# lll  groupby() is used to split data into groups based on one or more columns
#      and then apply aggregation, transformation, or analysis on each group.

# Simple Words
#-------------
# groupby() = Split → Apply → Combine
# 1. Split data into groups 
# 2. Apply operation on each group
# 3. Combine the results

# Syntax
#-------
# dataframe.groupby(column_name)

# Output : <pandas.api.typing.DataFrameGroupBy object>


# Important Concept
#------------------
# lll  groupby() doesn't compute anything immediately.
#      first It only creates a grouping object.
#      and Computation happens when we apply mathematical functions.

#   Sir we also know that when we want to apply groupby on multiple 
#   columns then we pass columns name as list inside groupby.







# agg() in Pandas
#*****************
# lll agg() (aggregation) is a pandas groupby method used to apply one or multiple aggregation
#     functions on grouped data and return a summarized result.


#     There are various way to apply aggregation function inside agg() method in Pandas

# 1. By using Dictionary
# -----------------------
# Column name as key, function as value
'''
movies.groupby('Genre').agg({
    'Runtime': 'mean',
    'IMDB_Rating': 'mean',
    'No_of_Votes': 'sum',
    'Gross': 'sum',
    'Metascore': 'min'
})

'''


# 2. By using List
# ----------------
# Select columns first, then apply list of functions
'''
movies.groupby('Genre')[['Gross', 'Metascore', 'IMDB_Rating']].agg(
    ['min', 'max', 'mean', 'sum']
)
'''



# 3. By using Tuple / Named Aggregation
# -------------------------------------
# New column name = (old_column, function)
'''
vk.groupby('bowling_team').agg(
    vk_runs=('batsman_runs', 'sum'),
    vk_min=('batsman_runs', 'min'),
    vk_max=('batsman_runs', 'max'),
    vk_avg=('batsman_runs', 'mean')
)
'''



# filter()
# ********
#lll  filter() is a pandas GroupBy method used to keep or remove
#     entire groups based on a condition.

# Syntax
# dataframe.groupby(column).filter(function)

# result = df.groupby("Dept").filter(
#    lambda x: x["Salary"].mean() > 40000
# )




# transform()
# -----------
# lll transform() is a pandas GroupBy method used to perform
#     calculations on each group and return an output having
#     the same size as the original DataFrame.

# Syntax
# dataframe.groupby(column)[target_column].transform(function)

# df["Dept_Avg"] = df.groupby("Dept")["Salary"].transform("mean")





#******************************************************************************************************************************
# for Combining Data of Series and DataFrame
#********************************************

# concat()     merge()
# join()


# pd.concat()
#*************
# lll pd.concat() is a Pandas method used to combine two or more DataFrames
#     or Series either vertically (row-wise) or horizontally (column-wise).

# In simple words:
# It is used to stack multiple datasets into one dataset.

# pd.concat(objs, axis=0, ignore_index=False, keys=None)

# lll It has parameter 
#                (Indicate)
#     objs           ->       List of DataFrames / Series
#     axis=0         ->       Vertical stacking (default) |   Way of stacking
#     axis=1         ->       Horizontal stacking         |
#     ignore_index   ->       Reset index after stacking
#     keys           ->       MultiIndex labels


# For pd.concat(), stacking happens in two ways:

# lll Vertical Stacking (axis=0):
#     ----------------------------
#     Best condition: 
#              Columns should be same.
#              If columns are different, pandas adds new columns and fills missing values with NaN.

# lll Horizontal Stacking (axis=1):
#     -------------------------------
#     Best condition: 
#               Index should be same.
#               If indexes are different, pandas fills unmatched rows with NaN.

# Easy Rule:
#       axis=0 → Match Columns
#       axis=1 → Match Index





# Pandas merge() / join()
# ***********************   
# lll merge() is a pandas method used to combine two DataFrames
#     based on one or more common columns, similar to SQL JOIN.

# In simple words:
# It is used to connect related tables using key columns.


# pd.merge(left_df, right_df, how='inner', on='column_name')

# OR

# left_df.merge(right_df, how='inner', on='column_name')


# It has Parameters:
#          (Indicate)
# how         ->         type of join
# on          ->         common column name
# left_on     ->         left table join column
# right_on    ->         right table join column
# suffixes (handle duplicate column names)


# left_on and right_on
# ---------------------
# df1.merge(df2, left_on='emp_id', right_on='id')

# lll Used when column names are different
#     in both DataFrames.


# suffixes Parameter
# -------------------
# df1.merge(df2, on='id', suffixes=('_left', '_right'))

# lll Used when same column names exist
#     in both DataFrames.

# result = df1.merge(
#     df2,
#     on="id",
#     suffixes=("_old", "_new")
# )

#    id   name  salary_old  salary_new  bonus
# 0   1   Aman       50000       55000   5000
# 1   2  Rahul       60000       65000   6000
# 2   3  Priya       70000       75000   7000








#*****************************************************************************************************************************
# for Reshaping Data of Series and DataFrame
#********************************************
# pivot()      pivot_table()
# melt()       stack()
# unstack()



# pivot() in Pandas
# ******************
# lll pivot() is a pandas reshaping method used to
#     convert unique values from one column into
#     separate columns.


# lll And pivot() reshape data only when there are
#     no duplicate values.


# lll we also know that it convert
#     long-format data into wide-format data by transforming
#     row values into columns."
 


# Syntax
# -------
# dataframe.pivot(index, columns, values)

# It has parameters
# ------------------
#          index   → Row labels in the new DataFrame
#          columns → Unique values that become new columns
#          values  → Values to fill inside the table

# Best Condition
# --------------
# Each (index, column) combination must have
# only one value.

# If Duplicate Values Exist
# -------------------------
# pivot() raises an error.
#
# Use pivot_table() when duplicates are present.


# Example
# -------
# Original DataFrame

# Student  Year  Subject   Exam    Marks
# A        2024  Math      Mid      90
# A        2024  Math      Final    95
# A        2024  Science   Mid      85
# B        2024  Math      Mid      88


# df.pivot(
#     index=['Student', 'Year'],
#     columns=['Subject', 'Exam'],
#     values='Marks'
# )


# Output

# Subject         Math          Science
# Exam            Mid  Final       Mid
# Student Year
# A       2024     90    95         85
# B       2024     88    NaN       NaN





# pivot_table() 
# **************
# lll pivot_table() is a pandas method used to reshape
#     and summarize data by converting unique values
#     into rows and columns while applying an aggregation
#     function.

# lll We also know that pivot_table() handle duplicate values by applying an
#     aggregation function (mean by default).


# Syntax
# -------
# dataframe.pivot_table(
#     index=None,
#     columns=None,
#     values=None,
#     aggfunc='mean'
# )

# Parameters
# ----------
# index    → Row labels in the new table
# columns  → Unique values that become columns
# values   → Column to aggregate
# aggfunc  → Aggregation function
#            (mean, sum, count, min, max, etc.)


# Best Condition
# --------------
# Used when duplicate (index, column) combinations
# exist and aggregation is required.

# Example
# -------
# Original DataFrame

# Student   Subject   Marks
# A         Math      90
# A         Math      85
# B         Math      88
# B         Science   92

# df.pivot_table(
#     index='Student',
#     columns='Subject',
#     values='Marks',
#     aggfunc='mean'
# )

# Output

# Subject   Math   Science
# Student
# A         87.5      NaN
# B         88.0      92


# Important Points
# ----------------
#     Handles duplicate values.
#     Performs aggregation automatically.
#     Default aggregation function is 'mean'.
#     Can use multiple aggregation functions.


# pivot() Vs pivot_table()
# ------------------------

# pivot()
# -------
# Only reshapes data.
# it Does not perform aggregation.
# if Duplicate values exist then it cause an error.


# pivot_table()
# -------------
# Reshapes and aggregates data.
# Handles duplicate values.
# Uses aggfunc (mean by default).

# Easy Interview Rule
# -------------------
# pivot()       → Reshape Data
# pivot_table() → Reshape + Aggregate Data





# lll melt()
# ***********

# lll "Sir, melt() is a pandas reshaping method used to convert
#     wide-format data into long-format data by transforming
#     columns into rows."

# It has parameters:
#             (Indicate)
# id_vars         ->        Columns to keep fixed
# value_vars      ->        Columns to unpivot
# var_name        ->        Name of variable column
# value_name      ->        Name of value column
# ignore_index    ->        Reset index or not


import pandas as pd

df = pd.DataFrame({
    'Name':['John', 'Chris'],
    'Height':[160, 182],
    'Weight':[67, 78]
})

print(df)

'''
    Name  Height  Weight
0   John     160      67
1  Chris     182      78
'''


print(
    df.melt(
        id_vars='Name',
        value_vars=['Height', 'Weight'],
        var_name='Attribute',
        value_name='Value'
    )
)

'''
    Name Attribute  Value
0   John    Height    160
1  Chris    Height    182
2   John    Weight     67
3  Chris    Weight     78
'''



# unstack()
# *********
#  lll  unstack() is pandas reshaping method used to converts inner row index level into columns.

# Row -> Column

# Example:
# Series MultiIndex becomes DataFrame.

multi_index_2 = pd.MultiIndex.from_product([['cse', 'ece'], [2019, 2020, 2021, 2022]])

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

temp = s.unstack()
print(temp)

'''
     2019  2020  2021  2022
cse     1     2     3     4
ece     5     6     7     8
'''



# stack()
# ********
#     stack() is pandas reshaping method used to converts column levels into row index.
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





#***************************************************************************************************************************
# For Aggregation Functions of Series and DataFrame
#***************************************************
# sum()        count()      mean() 
# min()        max()        median()
# std()        var()

# It has parameters
#                   axis ->  0 : column-wise sum (default)
#                            1 : row-wise sum

#                   skipna -> True  : ignores NaN values (default)
#                             False : includes NaN effect

#                   numeric_only -> True  : only numeric columns
#                                   False : all possible columns


# sum()      → total of values
# count()    → number of non-null values
# product()  → multiplication of values
# mean()     → average value
# median()   → middle value
# mode()     → most frequent value
# std()      → standard deviation
# var()      → variance
# min()      → smallest value
# max()      → largest value
#
# axis=0 → column wise
# axis=1 → row wise











#   for File Handling in Pandas
# *******************************

#     "Sir, Pandas provides functions and methods to read
#     data from files into a DataFrame and write DataFrame
#     data into different file formats."


# It has functions/methods:
#             (Indicate)
# read_csv()       ->        Read CSV file into DataFrame
# read_excel()     ->        Read Excel file into DataFrame
# to_csv()         ->        Write DataFrame to CSV file
# to_excel()       ->        Write DataFrame to Excel file


# ============================================================
# 1. read_csv()
# ============================================================

# Parameters:
# filepath_or_buffer  ->     Path or name of CSV file
# sep                 ->     Separator/delimiter
# header              ->     Row used as column names
# usecols             ->     Select specific columns
# dtype               ->     Specify data types
# na_values           ->     Values treated as missing


import pandas as pd


# Example:
df = pd.read_csv(
    'employees.csv',
    sep=',',
    header=0,
    usecols=['Name', 'Salary']
)

print(df)


# ============================================================
# 2. read_excel()
# ============================================================

# Parameters:
# io                  ->     Path or name of Excel file
# sheet_name          ->     Name or index of sheet
# header              ->     Row used as column names
# usecols             ->     Select specific columns
# dtype               ->     Specify data types


# Example:
df = pd.read_excel(
    'employees.xlsx',
    sheet_name='Employees',
    header=0,
    usecols=['Name', 'Salary']
)

print(df)


# ============================================================
# 3. to_csv()
# ============================================================

# Parameters:
# path_or_buf         ->     Path or name of output file
# index               ->     Write index or not
# columns             ->     Columns to write
# header              ->     Write column names or not
# sep                 ->     Separator/delimiter


# Example:
df.to_csv(
    'output.csv',
    index=False,
    columns=['Name', 'Salary'],
    header=True,
    sep=','
)


# ============================================================
# 4. to_excel()
# ============================================================

# Parameters:
# excel_writer        ->     Path or name of output file
# sheet_name          ->     Name of Excel sheet
# index               ->     Write index or not
# columns             ->     Columns to write
# header              ->     Write column names or not


# Example:
df.to_excel(
    'output.xlsx',
    sheet_name='Employees',
    index=False,
    columns=['Name', 'Salary'],
    header=True
)
  
# ==========================================
