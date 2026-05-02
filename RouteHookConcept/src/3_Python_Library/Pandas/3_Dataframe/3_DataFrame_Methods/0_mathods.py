import numpy as np
import pandas as pd
import os



# ==================================================
# DataFrame Methods
# ==================================================

# Definition (Interview Friendly)
# DataFrame methods are built-in functions used to
# explore, analyze, and manipulate tabular data.



path_dir = os.path.dirname(__file__)

path_file_movies = os.path.join(path_dir, '../../1_Dataset/movies.csv')
path_file_ipl_matches = os.path.join(path_dir, '../../1_Dataset/ipl-matches.csv')


movies = pd.read_csv(path_file_movies)
ipl_matches = pd.read_csv(path_file_ipl_matches)



# ==================================================
# 1. head() and tail()
# ==================================================

# Interview Definition
# head() returns the first N rows of a DataFrame.
# tail() returns the last N rows of a DataFrame.

# Default value of N = 5

print(movies.head(2))

#                     title_x  ...             release_date
# 0  Uri: The Surgical Strike  ...    11 January 2019 (USA)
# 1             Battalion 609  ...  11 January 2019 (India)
#
# [2 rows x 18 columns]


print(ipl_matches.tail(2))

#          ID        City  ...    Umpire1      Umpire2
# 948  335983  Chandigarh  ...  MR Benson   SL Shastri
# 949  335982   Bangalore  ...  Asad Rauf  RE Koertzen
#
# [2 rows x 20 columns]


# Important Points
# • Useful for quick dataset inspection
# • Helps verify data loading



# ==================================================
# 2. sample()
# ==================================================

# Interview Definition
# sample() returns random rows from the DataFrame.

print(movies.sample(1))

#                 title_x  ...               release_date
# 1461  Market (2003 film)  ...  12 September 2003 (India)
#
# [1 rows x 18 columns]


print(ipl_matches.sample(1))

#          ID       City  ...    Umpire1    Umpire2
# 885  392188  Cape Town  ...  M Erasmus  AM Saheba
#
# [1 rows x 20 columns]


# Important Points
# • Used for random sampling
# • Useful in data exploration and ML



# ==================================================
# 3. info()
# ==================================================

# Interview Definition
# info() provides a concise summary of the DataFrame
# including column names, non-null values, data types,
# and memory usage.

print(movies.info())

# <class 'pandas.DataFrame'>
# RangeIndex: 1629 entries, 0 to 1628
# Data columns (total 18 columns):
#      Column            Non-Null Count  Dtype
# ---  ------            --------------  -----
# 0   title_x           1629 non-null   str
# 1   imdb_id           1629 non-null   str
# 2   poster_path       1526 non-null   str
# 3   wiki_link         1629 non-null   str
# ...
# memory usage: 229.2 KB


print(ipl_matches.info())


# Important Points
# • Shows missing values
# • Shows memory usage
# • Helpful for data cleaning



# ==================================================
# 4. describe()
# ==================================================

# Interview Definition
# describe() generates statistical summary
# of numerical columns in the DataFrame.

# It returns:
# count, mean, std, min, 25%, 50%, 75%, max


print(movies.describe())

#        is_adult  year_of_release  imdb_rating     imdb_votes
# count    1629.0      1629.000000  1629.000000    1629.000000
# mean        0.0      2010.263966     5.557459    5384.263352
# std         0.0         5.381542     1.567609   14552.103231
# min         0.0      2001.000000     0.000000       0.000000
# 25%         0.0      2005.000000     4.400000     233.000000
# 50%         0.0      2011.000000     5.600000    1000.000000
# 75%         0.0      2015.000000     6.800000    4287.000000
# max         0.0      2019.000000     9.400000  310481.000000


print(ipl_matches.describe())

#                  ID      Margin
# count  9.500000e+02  932.000000
# mean   8.304852e+05   17.056867
# std    3.375678e+05   21.633109
# min    3.359820e+05    1.000000
# 25%    5.012612e+05    6.000000
# 50%    8.297380e+05    8.000000
# 75%    1.175372e+06   19.000000
# max    1.312200e+06  146.000000


# Important Points
# • Works only on numerical columns
# • Helps understand data distribution



# ==================================================
# 5. isnull()
# ==================================================

# Interview Definition
# isnull() checks for missing (NaN) values
# in the DataFrame and returns a boolean table.

print(movies.isnull())


print(movies.isnull().sum())

# title_x                0
# imdb_id                0
# poster_path          103
# wiki_link              0
# title_y                0
# original_title         0
# is_adult               0
# year_of_release        0
# runtime                0
# genres                 0
# imdb_rating            0
# imdb_votes             0
# story                 20
# summary                0
# tagline             1072
# actors                 5
# wins_nominations     922
# release_date         107


# Important Points
# • Used for missing value detection
# • Often combined with sum()



# ==================================================
# 6. duplicated()
# ==================================================

# Interview Definition
# duplicated() checks duplicate rows
# and returns True for duplicates.

print(movies.duplicated())


print(movies.duplicated().sum())

# 0


print(ipl_matches.duplicated().sum())

# 0



student_dict = {
    'iq':[100, 90, 120, 80, 0, 0],
    'marks':[80, 70, 100, 50, 0, 0],
    'package':[10, 7, 14, 2, 0, 0]
}

students = pd.DataFrame(student_dict)

print(students)

#     iq  marks  package
# 0  100     80       10
# 1   90     70        7
# 2  120    100       14
# 3   80     50        2
# 4    0      0        0
# 5    0      0        0


print(students.duplicated().sum())

# 1



# ==================================================
# 7. rename()
# ==================================================

# Interview Definition
# rename() is used to change column names
# or index labels in a DataFrame.

# By default changes are temporary.

print(students.rename(columns={'marks':'percent', 'package':'8lpa'}))

#     iq  percent  8lpa
# 0  100       80    10
# 1   90       70     7
# 2  120      100    14
# 3   80       50     2
# 4    0        0     0
# 5    0        0     0


print(students)

#     iq  marks  package
# 0  100     80       10
# 1   90     70        7
# 2  120    100       14
# 3   80     50        2
# 4    0      0        0
# 5    0      0        0


students.rename(columns={'marks':'percent', 'package':'8lpa'}, inplace=True)

print(students)

#     iq  percent  8lpa
# 0  100       80    10
# 1   90       70     7
# 2  120      100    14
# 3   80       50     2
# 4    0        0     0
# 5    0        0     0



# ==================================================
# Quick Revision
# ==================================================

# head()        → lll "Returns the first n elements of the DataFrame. Default is 5 if n not provided."
# tail()        → lll "Returns the last n elements of the DataFrame. Default is 5 if n not provided."
# sample()      → lll "Returns the random n elements of the DataFrame. Default is 5 if n not provided."
# describe()    > lll "Returns a statistical summary of the Series or DataFrame:
#                      count, mean, std, min, max, 25%, 50%, 75% percentiles
#                      For categorical data, it returns count, unique, top, freq"
# duplicated()  → lll  Returns a Boolean mask indicating duplicate rows 
# isnull()      → lll  Returns a Boolean mask indicating missing (NaN) values
# rename()      → lll  is used to change column names in a DataFrame
# info()        → lll  provides a concise summary of the DataFrame
#                      including column names, non-null values, data types,
#                      and memory usage.