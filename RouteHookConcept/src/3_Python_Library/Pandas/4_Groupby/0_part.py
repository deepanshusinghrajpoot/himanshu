


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



# groupby() in Pandas :- Perfect Interview Notes
#===============================================

# Interview Friendly Definition
#------------------------------
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

# Example
#--------
genres = movies.groupby('Genre')

print(genres)

# Output
#-------
# <pandas.api.typing.DataFrameGroupBy object>


# Important Concept
#------------------
# lll  groupby() doesn't compute anything immediately.
#      first It only creates a grouping object.
#      and Computation happens when we apply mathematical functions.

#      Sir we also know that when we want to apply groupby on multiple 
#      columns then we pass columns name as list inside groupby.


# Aggregation Example
#====================

print(type(genres.sum()))

# Output
#-------
# <class 'pandas.DataFrame'>


print(genres.sum())

# Output
#-------
#                                                 Series_Title                                      Released_Year  ...         Gross  Metascore
# Genre                                                                                                            ...
# Action     The Dark KnightThe Lord of the Rings: The Retu...  2008200320102001200219991980197719621954200019...  ...  3.263226e+10    10499.0
# Adventure  InterstellarBack to the FutureInglourious Bast...  2014198520091981196819621959201319751963194819...  ...  9.496922e+09     5020.0
# Animation  Sen to Chihiro no kamikakushiThe Lion KingHota...  2001199419882016201820172008199719952019200920...  ...  1.463147e+10     6082.0
# Biography  Schindler's ListGoodfellasHamiltonThe Intoucha...  1993199020202011200220171995198420182013201320...  ...  8.276358e+09     6023.0
# Comedy     GisaengchungLa vita è bellaModern TimesCity Li...  2019199719361931200919641940200120001973196019...  ...  1.566387e+10     9840.0
# Crime      The GodfatherThe Godfather: Part II12 Angry Me...  1972197419571994200219991995199120192006199519...  ...  8.452632e+09     6706.0
# Drama      The Shawshank RedemptionFight ClubForrest Gump...  1994199919941975202019981946201420061998198819...  ...  3.540997e+10    19208.0
# Family     E.T. the Extra-TerrestrialWilly Wonka & the Ch...                                           19821971  ...  4.391106e+08      158.0
# Fantasy                Das Cabinet des Dr. CaligariNosferatu                                           19201922  ...  7.827267e+08        0.0
# Film-Noir   The Third ManThe Maltese FalconShadow of a Doubt                                       194919411943  ...  1.259105e+08      287.0
# Horror     PsychoAlienThe ThingThe ExorcistNight of the L...       19601979198219731968196120171978193320042001  ...  1.034649e+09      880.0
# Mystery    MementoRear WindowVertigoShutter IslandKahaani...   200019541958201020121995197219381988201219981997  ...  1.256417e+09      633.0
# Thriller                                     Wait Until Dark                                               1967  ...  1.755074e+07       81.0
# Western    Il buono, il brutto, il cattivoOnce Upon a Tim...                                   1966196819651976  ...  5.822151e+07      313.0
# 
# [14 rows x 9 columns]



# Numeric Aggregation
#====================

print(genres.sum(numeric_only=True))

# Output
#-------
#            Runtime  IMDB_Rating  No_of_Votes         Gross  Metascore
# Genre
# Action       22196       1367.3     72282412  3.263226e+10    10499.0
# Adventure     9656        571.5     22576163  9.496922e+09     5020.0
# Animation     8166        650.3     21978630  1.463147e+10     6082.0
# Biography    11970        698.6     24006844  8.276358e+09     6023.0
# Comedy       17380       1224.7     27620327  1.566387e+10     9840.0
# Crime        13524        857.8     33533615  8.452632e+09     6706.0
# Drama        36049       2299.7     61367304  3.540997e+10    19208.0
# Family         215         15.6       551221  4.391106e+08      158.0
# Fantasy        170         16.0       146222  7.827267e+08        0.0
# Film-Noir      312         23.9       367215  1.259105e+08      287.0
# Horror        1123         87.0      3742556  1.034649e+09      880.0
# Mystery       1429         95.7      4203004  1.256417e+09      633.0
# Thriller       108          7.8        27733  1.755074e+07       81.0
# Western        593         33.4      1289665  5.822151e+07      313.0



# Interview Question
#===================

# Q1 : Find top 3 genres by total earning

print(movies.groupby('Genre').sum(numeric_only=True)['Gross'].sort_values(ascending=False).head(3))

# Output
#-------
# Genre
# Drama     3.540997e+10
# Action    3.263226e+10
# Comedy    1.566387e+10
# Name: Gross, dtype: float64


print(movies.groupby('Genre')['Gross'].sum().sort_values(ascending=False).head(3))

# Output
#-------
# Genre
# Drama     3.540997e+10
# Action    3.263226e+10
# Comedy    1.566387e+10
# Name: Gross, dtype: float64


# Important Note
#---------------
# Second approach is faster because it selects the column before aggregation.



# Q2 : Find genre with highest average IMDB rating

print(movies.groupby('Genre')['IMDB_Rating'].mean().sort_values(ascending=False).head(1))

# Output
#-------
# Genre
# Western    8.35
# Name: IMDB_Rating, dtype: float64



# Q3 : Find director with highest popularity

print(movies.groupby('Director')['No_of_Votes'].sum().sort_values(ascending=False).head(1))

# Output
#-------
# Director
# Christopher Nolan    11578345
# Name: No_of_Votes, dtype: int64



# Q4 : Find number of movies done by each actor

print(movies.groupby('Star1')['Series_Title'].count().sort_values(ascending=False))

# Output
#-------
# Star1
# Tom Hanks            12
# Robert De Niro       11
# Al Pacino            10
# Clint Eastwood       10
# Leonardo DiCaprio     9
# ...
# Name: count, Length: 660, dtype: int64



# Shortcut Method
#----------------

print(movies['Star1'].value_counts())

# Output
#-------
# Same result as groupby count