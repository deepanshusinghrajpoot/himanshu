


import numpy as np
import pandas as pd


import os



path_dir = os.path.dirname(__file__)

path_file_imdb_top_1000 = os.path.join(path_dir, '../1_Dataset/imdb-top-1000.csv')




movies = pd.read_csv(path_file_imdb_top_1000)

print(movies.columns)
# Index(['Series_Title', 'Released_Year', 'Runtime', 'Genre', 'IMDB_Rating',
#        'Director', 'Star1', 'No_of_Votes', 'Gross', 'Metascore'],
#       dtype='str')




# agg() in Pandas :- Perfect Interview Notes
#===========================================

# Interview Friendly Definition
#------------------------------
# lll agg() (aggregation) method is used to apply one or multiple aggregation
#     functions on grouped data and return a summarized result.

# =====================================================================
# There are many ways to perform aggregation inside agg() method in Pandas
# =====================================================================


# 1. By using Dictionary
# ---------------------------------------------------------------------
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
# ---------------------------------------------------------------------
# Select columns first, then apply list of functions
'''
movies.groupby('Genre')[['Gross', 'Metascore', 'IMDB_Rating']].agg(
    ['min', 'max', 'mean', 'sum']
)
'''



# 3. By using Tuple / Named Aggregation
# ---------------------------------------------------------------------
# New column name = (old_column, function)
'''
vk.groupby('bowling_team').agg(
    vk_runs=('batsman_runs', 'sum'),
    vk_min=('batsman_runs', 'min'),
    vk_max=('batsman_runs', 'max'),
    vk_avg=('batsman_runs', 'mean')
)
'''



# 1.1. By using Custom Function
# ---------------------------------------------------------------------

def range_value(x):
    return x.max() - x.min()

movies.groupby('Genre').agg({
    'Gross': range_value
})


# 1.2. By using Dictionary with Multiple Functions
# ---------------------------------------------------------------------
# One column with many functions
'''
movies.groupby('Genre').agg({
    'Gross': ['min', 'max', 'mean', 'sum'],
    'Metascore': ['min', 'max'],
    'IMDB_Rating': ['mean']
})
'''




# Simple Words
#-------------
# agg() allows us to perform multiple calculations (like mean, sum, min, max)
# on one or more columns at the same time.

# Syntax
#-------
# dataframe.groupby(column).agg(function)
# dataframe.groupby(column).agg({column:function})



# passing dict
#==============

# Here each column is mapped with the aggregation function
# we want to apply.

print(movies.groupby('Genre').agg(
    {
        'Runtime':'mean',
        'IMDB_Rating':'mean',
        'No_of_Votes':'sum',
        'Gross':'sum',
        'Metascore':'min'
    }
))

# Output
#-------
#               Runtime  IMDB_Rating  No_of_Votes         Gross  Metascore
# Genre
# Action     129.046512     7.949419     72282412  3.263226e+10       33.0
# Adventure  134.111111     7.937500     22576163  9.496922e+09       41.0
# Animation   99.585366     7.930488     21978630  1.463147e+10       61.0
# Biography  136.022727     7.938636     24006844  8.276358e+09       48.0
# Comedy     112.129032     7.901290     27620327  1.566387e+10       45.0
# Crime      126.392523     8.016822     33533615  8.452632e+09       47.0
# Drama      124.737024     7.957439     61367304  3.540997e+10       28.0
# Family     107.500000     7.800000       551221  4.391106e+08       67.0
# Fantasy     85.000000     8.000000       146222  7.827267e+08        NaN
# Film-Noir  104.000000     7.966667       367215  1.259105e+08       94.0
# Horror     102.090909     7.909091      3742556  1.034649e+09       46.0
# Mystery    119.083333     7.975000      4203004  1.256417e+09       52.0
# Thriller   108.000000     7.800000        27733  1.755074e+07       81.0
# Western    148.250000     8.350000      1289665  5.822151e+07       69.0



# passing list
#==============

# Here multiple aggregation functions are applied
# to selected columns.

print(movies.groupby('Genre')[['Gross', 'Metascore', 'IMDB_Rating']].agg(['min', 'max', 'mean', 'sum']))

# Output
#-------
#                  Gross                                          Metascore                            IMDB_Rating
#                    min          max          mean           sum       min    max       mean      sum         min  max      mean     sum
# Genre
# Action          3296.0  936662225.0  1.897224e+08  3.263226e+10      33.0   98.0  73.419580  10499.0         7.6  9.0  7.949419  1367.3
# Adventure      61001.0  874211619.0  1.319017e+08  9.496922e+09      41.0  100.0  78.437500   5020.0         7.6  8.6  7.937500   571.5
# Animation     128985.0  873839108.0  1.784326e+08  1.463147e+10      61.0   96.0  81.093333   6082.0         7.6  8.6  7.930488   650.3
# Biography      21877.0  753585104.0  9.404952e+07  8.276358e+09      48.0   97.0  76.240506   6023.0         7.6  8.9  7.938636   698.6
# Comedy          1305.0  886752933.0  1.010572e+08  1.566387e+10      45.0   99.0  78.720000   9840.0         7.6  8.6  7.901290  1224.7
# Crime           6013.0  790482117.0  7.899656e+07  8.452632e+09      47.0  100.0  77.080460   6706.0         7.6  9.2  8.016822   857.8
# Drama           3600.0  924558264.0  1.225259e+08  3.540997e+10      28.0  100.0  79.701245  19208.0         7.6  9.3  7.957439  2299.7
# Family       4000000.0  435110554.0  2.195553e+08  4.391106e+08      67.0   91.0  79.000000    158.0         7.8  7.8  7.800000    15.6
# Fantasy    337574718.0  445151978.0  3.913633e+08  7.827267e+08       NaN    NaN        NaN      0.0         7.9  8.1  8.000000    16.0
# Film-Noir     449191.0  123353292.0  4.197018e+07  1.259105e+08      94.0   97.0  95.666667    287.0         7.8  8.1  7.966667    23.9
# Horror         89029.0  298791505.0  9.405902e+07  1.034649e+09      46.0   97.0  80.000000    880.0         7.6  8.5  7.909091    87.0
# Mystery      1035953.0  474203697.0  1.047014e+08  1.256417e+09      52.0  100.0  79.125000    633.0         7.6  8.4  7.975000    95.7
# Thriller    17550741.0   17550741.0  1.755074e+07  1.755074e+07      81.0   81.0  81.000000     81.0         7.8  7.8  7.800000     7.8
# Western      5321508.0   31800000.0  1.455538e+07  5.822151e+07      69.0   90.0  78.250000    313.0         7.8  8.8  8.350000    33.4



# Adding both the syntax
#=======================

# We can combine dictionary + list style aggregations
# to perform different operations on different columns.

print(movies.groupby('Genre').agg(
    {
        'Runtime':['mean', 'sum'],
        'IMDB_Rating':'mean',
        'No_of_Votes':['sum', 'min', 'max'],
        'Gross':'sum',
        'Metascore':['min', 'mean', 'sum']
    }
))

# Output
#-------
#               Runtime        IMDB_Rating No_of_Votes                          Gross Metascore
#                  mean    sum        mean         sum     min      max           sum       min       mean      sum
# Genre
# Action     129.046512  22196    7.949419    72282412   25312  2303232  3.263226e+10      33.0  73.419580  10499.0
# Adventure  134.111111   9656    7.937500    22576163   29999  1512360  9.496922e+09      41.0  78.437500   5020.0
# Animation   99.585366   8166    7.930488    21978630   25229   999790  1.463147e+10      61.0  81.093333   6082.0
# Biography  136.022727  11970    7.938636    24006844   27254  1213505  8.276358e+09      48.0  76.240506   6023.0
# Comedy     112.129032  17380    7.901290    27620327   26337   939631  1.566387e+10      45.0  78.720000   9840.0
# Crime      126.392523  13524    8.016822    33533615   27712  1826188  8.452632e+09      47.0  77.080460   6706.0
# Drama      124.737024  36049    7.957439    61367304   25088  2343110  3.540997e+10      28.0  79.701245  19208.0
# Family     107.500000    215    7.800000      551221  178731   372490  4.391106e+08      67.0  79.000000    158.0
# Fantasy     85.000000    170    8.000000      146222   57428    88794  7.827267e+08       NaN        NaN      0.0
# Film-Noir  104.000000    312    7.966667      367215   59556   158731  1.259105e+08      94.0  95.666667    287.0
# Horror     102.090909   1123    7.909091     3742556   27007   787806  1.034649e+09      46.0  80.000000    880.0
# Mystery    119.083333   1429    7.975000     4203004   33982  1129894  1.256417e+09      52.0  79.125000    633.0
# Thriller   108.000000    108    7.800000       27733   27733    27733  1.755074e+07      81.0  81.000000     81.0
# Western    148.250000    593    8.350000     1289665   65659   688390  5.822151e+07      69.0  78.250000    313.0



# looping on groups
#==================

# Interview Friendly Definition
#------------------------------
# When we iterate over groupby(), each iteration returns:
# 1. group name (key)
# 2. dataframe containing rows belonging to that group.

# group -> value of the grouped column
# data  -> subset dataframe for that group

for group, data in movies.groupby('Genre'):
    print(type(group), type(data))

# Output
#-------
# <class 'str'> <class 'pandas.DataFrame'>
# <class 'str'> <class 'pandas.DataFrame'>
# <class 'str'> <class 'pandas.DataFrame'>
# <class 'str'> <class 'pandas.DataFrame'>
# <class 'str'> <class 'pandas.DataFrame'>
# <class 'str'> <class 'pandas.DataFrame'>
# <class 'str'> <class 'pandas.DataFrame'>
# <class 'str'> <class 'pandas.DataFrame'>
# <class 'str'> <class 'pandas.DataFrame'>
# <class 'str'> <class 'pandas.DataFrame'>
# <class 'str'> <class 'pandas.DataFrame'>
# <class 'str'> <class 'pandas.DataFrame'>
# <class 'str'> <class 'pandas.DataFrame'>



# Example Problem
#================

# Q : Find the highest rated movies of each genre



# Efficient Method
#=================

# Append results in a list and concatenate at the end.

rows = []

for group, data in movies.groupby('Genre'):
    rows.append(data[data['IMDB_Rating'] == data['IMDB_Rating'].max()])

df = pd.concat(rows)

print(type(df))

# Output
#-------
# <class 'pandas.DataFrame'>


print(df)

# Output
#-------
#                             Series_Title Released_Year  Runtime      Genre  ...                Star1 No_of_Votes        Gross  Metascore
# 2                        The Dark Knight          2008      152     Action  ...       Christian Bale     2303232  534858444.0       84.0
# 21                          Interstellar          2014      169  Adventure  ...  Matthew McConaughey     1512360  188020017.0       74.0
# 23         Sen to Chihiro no kamikakushi          2001      125  Animation  ...        Daveigh Chase      651376   10055859.0       96.0
# 7                       Schindler's List          1993      195  Biography  ...          Liam Neeson     1213505   96898818.0       94.0
# 19                          Gisaengchung          2019      132     Comedy  ...         Kang-ho Song      552778   53367844.0       96.0
# 26                       La vita è bella          1997      116     Comedy  ...      Roberto Benigni      623629   57598247.0       59.0
# 1                          The Godfather          1972      175      Crime  ...        Marlon Brando     1620367  134966411.0      100.0
# 0               The Shawshank Redemption          1994      142      Drama  ...          Tim Robbins     2343110   28341469.0       80.0
# 688           E.T. the Extra-Terrestrial          1982      115     Family  ...         Henry Thomas      372490  435110554.0       91.0
# 698  Willy Wonka & the Chocolate Factory          1971      100     Family  ...          Gene Wilder      178731    4000000.0       67.0
# 321         Das Cabinet des Dr. Caligari          1920       76    Fantasy  ...        Werner Krauss       57428  337574718.0        NaN
# 309                        The Third Man          1949      104  Film-Noir  ...         Orson Welles      158731     449191.0       97.0
# 49                                Psycho          1960      109     Horror  ...      Anthony Perkins      604211   32000000.0       97.0
# 69                               Memento          2000      113    Mystery  ...           Guy Pearce     1125712   25544867.0       80.0
# 81                           Rear Window          1954      112    Mystery  ...        James Stewart      444074   36764313.0      100.0
# 700                      Wait Until Dark          1967      108   Thriller  ...       Audrey Hepburn       27733   17550741.0       81.0
# 12       Il buono, il brutto, il cattivo          1966      161    Western  ...       Clint Eastwood      688390    6100000.0       90.0
#
# [17 rows x 10 columns]