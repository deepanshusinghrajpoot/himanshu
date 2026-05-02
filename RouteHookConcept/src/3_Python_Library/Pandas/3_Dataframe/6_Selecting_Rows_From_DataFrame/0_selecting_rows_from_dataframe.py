

import numpy as np
import pandas as pd



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






student_dict = {
    'name':['nitish', 'ankit', 'rupesh', 'rishabh', 'amit', 'ankita'],
    'iq':[100, 90, 120, 80, 0, 0],
    'marks':[80, 70, 100, 50, 0, 0],
    'package':[10, 7, 14, 2, 0, 0]
}



students = pd.DataFrame(student_dict)

print(students)
#       name   iq  marks  package
# 0   nitish  100     80       10
# 1    ankit   90     70        7
# 2   rupesh  120    100       14
# 3  rishabh   80     50        2
# 4     amit    0      0        0
# 5   ankita    0      0        0



# ==================================================
# set_index()
# ==================================================

# Interview Definition
# set_index() is a Pandas DataFrame method used to
# convert an existing column into the index of the DataFrame.

# Syntax
# dataframe.set_index(column_name, inplace=True/False)

# lll “Sir, set_index() is used to convert an existing column into the index of a DataFrame.”
#     “By default, it does not modify the original DataFrame, it returns a new one.”
#     “If we use inplace = True, then it will permanently update the original DataFrame.”



# Example

students.set_index('name', inplace=True)

print(students)

# name      iq  marks  package
# nitish   100     80       10
# ankit     90     70        7
# rupesh   120    100       14
# rishabh   80     50        2
# amit       0      0        0
# ankita     0      0        0



# ==================================================
# Selecting Rows From DataFrame
# ==================================================

# In Pandas we mainly use two methods:

# iloc → Index Location (position based)
# loc  → Label Location (label based)



# ==================================================
# iloc (Index Location)
# ==================================================

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



# --------------------------------------------------
# Selecting Single Row
# --------------------------------------------------

print(movies.iloc[2])

# title_x          The Accidental Prime Minister (film)
# imdb_id                               tt6986710
# year_of_release                          2019
# ...
# Name: 2, dtype: object



# --------------------------------------------------
# Selecting Multiple Rows (Slicing)
# --------------------------------------------------

print(movies.iloc[0:5])

# rows from index 0 to 4



print(movies.iloc[0:10:3])

# rows from 0 to 9 with step 3
# 0,3,6,9



# --------------------------------------------------
# Fancy Indexing with iloc
# --------------------------------------------------

print(movies.iloc[[0,3,5]])

# Selects specific rows using list of positions



# ==================================================
# loc (Label Location)
# ==================================================

# Interview Definition
# lll loc is used to select rows and columns from a DataFrame using
#     labels index instead of integer index positions.

#     Syntax
#        dataframe.loc[row_label, column_label]

#     Slicing
#        dataframe.iloc[start_row:end_row:step , start_col:end_col:step]

#     Important Rule
#        start → included
#        end   → included



# --------------------------------------------------
# Selecting Single Row
# --------------------------------------------------

print(students.loc['nitish'])

# iq         100
# marks       80
# package     10
# Name: nitish



# --------------------------------------------------
# Selecting Multiple Rows (Slicing)
# --------------------------------------------------

print(students.loc['nitish':'rishabh'])

# nitish
# ankit
# rupesh
# rishabh



# --------------------------------------------------
# Fancy Indexing with loc
# --------------------------------------------------

print(students.loc[['nitish','rupesh','rishabh']])

# name      iq  marks  package
# nitish   100     80       10
# rupesh   120    100       14
# rishabh   80     50        2



# ==================================================
# iloc on Students DataFrame
# ==================================================

# Even if we set name as index,
# iloc still works with integer positions.



# Single Row

print(students.iloc[0])

# iq         100
# marks       80
# package     10
# Name: nitish



# Multiple Rows

print(students.iloc[0:4])



# Fancy Indexing

print(students.iloc[[0,2,3]])



# ==================================================
# Quick Interview Revision
# ==================================================

# iloc → index position based selection
# loc  → label based selection

# iloc slicing → end excluded
# loc slicing  → end included

# iloc example → df.iloc[0]
# loc example  → df.loc['nitish']