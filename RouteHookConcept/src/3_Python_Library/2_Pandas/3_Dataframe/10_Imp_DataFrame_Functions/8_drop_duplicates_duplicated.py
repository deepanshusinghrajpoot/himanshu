

#####################################################################

# 1. astype

# 2. value_counts (series and dataframe) :- gpt give perfect interview spoken diffinition

# 3. rank (series) :- gpt give perfect interview spoken diffinition

# 4. sort index (series and dataframe) :- gpt give perfect interview spoken diffinition

# 5. set index (dataframe) :- gpt give perfect interview spoken diffinition

# 6. rename index -> rename (dataframe) :- gpt give perfect interview spoken diffinition

# 7. reset index (series and dataframe) :- gpt give perfect interview spoken diffinition

# 8. unique (series) :- gpt give perfect interview spoken diffinition
# 8. nunique (series + dataframe) :- gpt give perfect interview spoken diffinition

# 9. isnull/notnull/hasnans (series and dataframe) :- gpt give perfect interview spoken diffinition

# 10. dropna (series and dataframe) :- gpt give perfect interview spoken diffinition

# 11. fillna (series and dataframe) :- gpt give perfect interview spoken diffinition

# 12. drop_duplicates (series and dataframe) :- gpt give perfect interview spoken diffinition

# 13. drop (series and dataframe) :- gpt give perfect interview spoken diffinition

# 14. apply (series and dataframe) :- gpt give perfect interview spoken diffinition

# 15. isin (series and dataframe) :- gpt give perfect interview spoken diffinition

# 16. corr (series and dataframe) :- gpt give perfect interview spoken diffinition

# 17. nlargest -> nsmallest (series and dataframe) :- gpt give perfect interview spoken diffinition

# 18. insert (series and dataframe) :- gpt give perfect interview spoken diffinition

# 19. copy (series and dataframe) :- gpt give perfect interview spoken diffinition


################################################################


import numpy as np
import pandas as pd

import os

marks = pd.DataFrame([
    [100, 80, 10],
    [90, 70, 7],
    [120, 100, 14],
    [80, 70, 14],
    [80, 70, 14]
], columns=['iq', 'marks', 'package'])


print(marks)

#     iq  marks  package
# 0  100     80       10
# 1   90     70        7
# 2  120    100       14
# 3   80     70       14
# 4   80     70       14


# 12. duplicated (series and dataframe) :- Perfect Interview Spoken Definition
#==============================================================================
# duplicated() is a pandas method used to identify duplicate values or duplicate
# rows in a Series or DataFrame.

# It returns a Boolean Series:
# False -> first occurrence (not duplicate)
# True  -> repeated/duplicate occurrence

# Important Points
#-----------------
# • Helps detect repeated data
# • Often used before removing duplicates
# • Works on both Series and DataFrame


print(marks.duplicated())

# 0    False
# 1    False
# 2    False
# 3    False
# 4     True
# dtype: bool


# Count total duplicate values
#-----------------------------

print(marks.duplicated().sum())   # 1




# 13. drop_duplicates (series and dataframe) :- Perfect Interview Spoken Definition
#===================================================================================
# drop_duplicates() is a pandas method used to remove duplicate values
# or duplicate rows from a Series or DataFrame.

# Important Parameters
#---------------------
# keep='first' -> keep first occurrence (default)
# keep='last'  -> keep last occurrence
# keep=False   -> remove all duplicates
# subset       -> specify columns to check duplicates



# Example on Series
#------------------

temp = pd.Series([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])

print(temp.drop_duplicates())

# 0    1
# 2    2
# 4    3
# 6    4
# 8    5
# dtype: int64




# Example on DataFrame
#---------------------

print(marks.drop_duplicates())

#     iq  marks  package
# 0  100     80       10
# 1   90     70        7
# 2  120    100       14
# 3   80     70       14



# Keep first duplicate (default)
#-------------------------------

print(marks.drop_duplicates(keep='first'))

#     iq  marks  package
# 0  100     80       10
# 1   90     70        7
# 2  120    100       14
# 3   80     70       14



# Keep last duplicate
#--------------------

print(marks.drop_duplicates(keep='last'))

#     iq  marks  package
# 0  100     80       10
# 1   90     70        7
# 2  120    100       14
# 4   80     70       14




# Real Interview-Type Example
#============================


# Ques: Find the last match played by Virat Kohli in Delhi
#--------------------------------------------------------


path_dir = os.path.dirname(__file__)
ipl_matches_file = os.path.join(path_dir, '../../1_Dataset/ipl-matches.csv')

ipl_matches = pd.read_csv(ipl_matches_file)


print(ipl_matches.columns)

# Index(['ID', 'City', 'Date', 'Season', 'MatchNumber', 'Team1', 'Team2',
#        'Venue', 'TossWinner', 'TossDecision', 'SuperOver', 'WinningTeam',
#        'WonBy', 'Margin', 'method', 'Player_of_Match', 'Team1Players',
#        'Team2Players', 'Umpire1', 'Umpire2'],
#       dtype='str')



# Filter matches where Virat Kohli played and City is Delhi
#----------------------------------------------------------

match_play_virat_kohali_Delhi = ipl_matches[
    (ipl_matches['Team1Players'] + ipl_matches['Team2Players']).apply(lambda x: 'V Kohli' in x)
    &
    (ipl_matches['City'] == 'Delhi')
]


print(match_play_virat_kohali_Delhi.drop_duplicates(subset=['City'], keep='first'))

#           ID   City        Date  ...                                       Team2Players       Umpire1                Umpire2
# 208  1178421  Delhi  2019-04-28  ...  ['PA Patel', 'V Kohli', 'AB de Villiers', 'S D...  BNJ Oxenford  KN Ananthapadmanabhan




# Syntax Summary (Important for Interview)
#-----------------------------------------

# drop_duplicates(subset=[column1, column2, ...], keep='first or last')

# subset=[column1, column2, ...]
# means duplicates will be checked based on these columns.