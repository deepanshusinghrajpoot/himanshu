
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
#         It is also used for Index name or column label context.
# is_unique :- is_unique is a pandas attribute returns True if all the values in the Series are unique; otherwise False."



# DataFrame has attributes
#==========================
# dtypes :- dtypes is a pandas attribute Shows the data type of the values of each column in a DataFrame.
# columns :-  columns is a pandas attribute returns the name of all columns of the DataFrame.



# Common attributes of Series or DataFrame
#==========================================
# shape :- shape is a pandas attribute used to get the dimensions of data.
#          It returns a tuple in the form:(rows, columns)
# index :- Represents the labels of the Series or DataFrame. Acts like row identifiers.
# values :- Returns the underlying data of the Series or DataFrame as a NumPy array.
# size :- size is a pandas attribute used to return the total number of elements in a Series or DataFrame.
#         It is rows multiplied by columns.





# methods of Series or DataFrame.
#================================


#*************************************************************************************************
#  Data Inspection
# *****************

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
#  Sorting & Ranking
# ********************
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
# Missing Values
# ***************
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
#                inplace -> False : returns new object (default)






# ****************************************************************************************************
# Filtering & Conditions
# ***********************
# isin()                           between()
# where()                          query() 


# isin (Series and DataFrame)
# ---------------------------
#      isin() is a pandas method used to check whether each element in a Series or DataFrame 
#      is present in a given list, set, or collection of values.

# between(Series)
# ----------------
#      between() is a pandas Series method used to check whether values lie between a lower and upper limit.
#      It returns True or False for each value."


# where(Series and DataFrame)
# ----------------------------
#      where() is a pandas Series and DataFrame method. It keeps values where condition is True,
#      and replaces values where condition is False.
#   Note : Boolean indexing is better for flltering data.

# query(Series and DataFrame)
# ---------------------------
#      query() is a pandas DataFrame method used to filter rows using a condition written as a string expression.
#      It makes filtering more readable."
#   Note : Both are good — depends on use case.
#          Boolean Indexing → more common, flexible, works on Series + DataFrame
#          query() → cleaner syntax, better readability for DataFrame filtering








# ****************************************************************************************************
# Duplicate Handling
# *******************

# duplicated()       drop_duplicates()  
# unique()           nunique()          


# duplicated (series and dataframe)
# ---------------------------------
#           duplicated() is a pandas method used to Returns a Boolean mask indicating 
#           duplicate values or duplicate rows of a Series or DataFrame.

# drop_duplicates (series and dataframe)
# --------------------------------------
#            drop_duplicates() is a pandas method used remove duplicate values or duplicate rows 
#            from a Series or DataFrame, keeps first by default. 
#     It has parameters
#                  subset : indicate : -> specify columns to check duplicates
#                  keep
#                      keep='first' : mean : -> keep first occurrence (default)
#                      keep='last'  : mean : -> keep last occurrence
#                      keep=False   : mean : -> remove all duplicates
#                  inplace 
#                         is equal to -> True : mean : modifies original data
#                         is equal to  -> False : mean : returns new object (default)

# nunique() (Series and DataFrame)
# --------------------------------
#            nunique() is a pandas method used to count the number of distinct (unique) values
#            in a Series or each column of a DataFrame.
#       It has a dropna parameter.
#          dropna -> True  : ignores NaN(missing) values (default)
#          dropna -> False : counts NaN(missing) as a unique value









# reset_index(series and dataframe)
# ---------------------------------
#            reset_index() is a pandas method used to convert the current index
#            back into a normal column and replace it with a default integer index.


# drop() (Series + DataFrame)
# --------------------------- 
#           drop() is a pandas method used to remove specified
#           labels (rows or columns) from a Series or DataFrame.
#      It has parameters
#         axis -> 0 : drop rows (default)
#         axis -> 1 : drop columns
#         inplace -> True  : modifies original data
#         inplace -> False : returns new object (default)

# astype(series and dataframe)
# ----------------------------
#            is a pandas method used to convert the data type
#            of a Series or DataFrame column into another specified data type.















# ==========================================
