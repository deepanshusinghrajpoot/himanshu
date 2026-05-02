


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




# apply() in Pandas GroupBy :- Perfect Interview Notes
#=====================================================

# Interview Friendly Definition
#------------------------------
# apply() method is used to apply a custom function to each group
# of a grouped DataFrame and then combine the results.

# Simple Words
#-------------
# apply() allows us to run our own function on each group
# when built-in aggregation functions (mean, sum, etc.) are not enough.

# It follows the GroupBy principle:
# Split → Apply → Combine

# Syntax
#-------
# dataframe.groupby(column).apply(function)



# Example 1 : Understanding apply()
#==================================

def foo(group):
    print(type(group))
    return group

movies.groupby('Genre').apply(foo)

# Output
#-------
# <class 'pandas.DataFrame'>
# <class 'pandas.DataFrame'>
# <class 'pandas.DataFrame'>
# <class 'pandas.DataFrame'>
# <class 'pandas.DataFrame'>
# <class 'pandas.DataFrame'>
# <class 'pandas.DataFrame'>
# <class 'pandas.DataFrame'>
# <class 'pandas.DataFrame'>
# <class 'pandas.DataFrame'>
# <class 'pandas.DataFrame'>
# <class 'pandas.DataFrame'>
# <class 'pandas.DataFrame'>



# Interview Concept
#------------------
# Each group passed into apply() is a DataFrame.



# Q1 : Find number of movies starting with A for each genre
#==========================================================

def start_A(group):
    return group['Series_Title'].str.startswith('A').sum()

print(movies.groupby('Genre').apply(start_A))

# Output
#-------
# Genre
# Action       10
# Adventure     2
# Animation     2
# Biography     9
# Comedy       14
# Crime         4
# Drama        21
# Family        0
# Fantasy       0
# Film-Noir     0
# Horror        1
# Mystery       0
# Thriller      0
# Western       0
# dtype: int64



# Q2 : Find ranking of each movie within its genre according to IMDB rating
#==========================================================================

def rank_movie(group):
    group['genre_rank'] = group['IMDB_Rating'].rank(ascending=False)
    return group

print(movies.groupby('Genre').apply(rank_movie))

# Output
#-------
#                                                    Series_Title Released_Year  Runtime  IMDB_Rating  ... No_of_Votes        Gross  Metascore  genre_rank
# Genre                                                                                                ...
# Action   2                                      The Dark Knight          2008      152          9.0  ...     2303232  534858444.0       84.0         1.0
#          5        The Lord of the Rings: The Return of the King          2003      201          8.9  ...     1642758  377845905.0       94.0         2.0
#          8                                            Inception          2010      148          8.8  ...     2067042  292576195.0       74.0         3.5
#          10   The Lord of the Rings: The Fellowship of the Ring          2001      178          8.8  ...     1661481  315544750.0       92.0         3.5
#          13               The Lord of the Rings: The Two Towers          2002      179          8.7  ...     1485555  342551365.0       87.0         6.0
# ...
# Thriller 700                                    Wait Until Dark          1967      108          7.8  ...       27733   17550741.0       81.0         1.0
# Western  12                     Il buono, il brutto, il cattivo          1966      161          8.8  ...      688390    6100000.0       90.0         1.0
# ...
# [1000 rows x 10 columns]



# Q3 : Find normalized IMDB rating genre-wise
#============================================

# Normalization Formula
#----------------------
# (value - min) / (max - min)


def normalize(group):
    group['norm_rating'] = (
        (group['IMDB_Rating'] - group['IMDB_Rating'].min()) /
        (group['IMDB_Rating'].max() - group['IMDB_Rating'].min())
    )
    return group

print(movies.groupby('Genre').apply(normalize))

# Output
#-------
#                                                    Series_Title Released_Year  Runtime  IMDB_Rating  ... No_of_Votes        Gross  Metascore  norm_rating
# Genre                                                                                                ...
# Action   2                                      The Dark Knight          2008      152          9.0  ...     2303232  534858444.0       84.0     1.000000
#          5        The Lord of the Rings: The Return of the King          2003      201          8.9  ...     1642758  377845905.0       94.0     0.928571
#          8                                            Inception          2010      148          8.8  ...     2067042  292576195.0       74.0     0.857143
#          10   The Lord of the Rings: The Fellowship of the Ring          2001      178          8.8  ...     1661481  315544750.0       92.0     0.857143
# ...
# Thriller 700                                    Wait Until Dark          1967      108          7.8  ...       27733   17550741.0       81.0          NaN
# Western  12                     Il buono, il brutto, il cattivo          1966      161          8.8  ...      688390    6100000.0       90.0     1.000000
# ...
# [1000 rows x 10 columns]



# Important Interview Notes
#==========================

# agg()  → Used for aggregation (mean, sum, min, max)
# apply() → Used for custom complex operations
# transform() → Used when output shape must remain same as original
#
# apply() is flexible but slower than agg() and transform().