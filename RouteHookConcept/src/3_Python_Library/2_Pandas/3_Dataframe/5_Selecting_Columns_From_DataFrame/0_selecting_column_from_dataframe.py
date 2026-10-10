
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





# ==================================================
# Selecting Columns From a DataFrame (Pandas)
# ==================================================

# In a DataFrame we can select one column or multiple columns.



# ==================================================
# lll Selecting Single Column
# ==================================================

# Interview Definition
# Selecting a single column from a DataFrame returns
# a Pandas Series object.

# Syntax
# dataframe['column_name']


# Example

print(type(movies['title_x']))
# <class 'pandas.Series'>

print(movies['title_x'])

# 0                   Uri: The Surgical Strike
# 1                              Battalion 609
# 2       The Accidental Prime Minister (film)
# 3                            Why Cheat India
# ...
# 1628                                Humsafar
# Name: title_x, Length: 1629, dtype: object



print(type(ipl_matches['Venue']))
# <class 'pandas.Series'>

print(ipl_matches['Venue'])

# 0                Narendra Modi Stadium, Ahmedabad
# 1                Narendra Modi Stadium, Ahmedabad
# 2                           Eden Gardens, Kolkata
# 3                           Eden Gardens, Kolkata
# ...
# 949                         M Chinnaswamy Stadium
# Name: Venue, Length: 950, dtype: object



# Important Point
# Single column → Series
# Multiple columns → DataFrame



# ==================================================
# lll Selecting Multiple Columns
# ==================================================

# Interview Definition
# Selecting multiple columns from a DataFrame returns
# another DataFrame.

# Syntax
# dataframe[['col1','col2','col3']]

# This technique is called Fancy Indexing.



# Example

print(type(movies[['title_x','year_of_release','actors']]))
# <class 'pandas.DataFrame'>

print(movies[['title_x','year_of_release','actors']])

#                                    title_x  year_of_release  actors
# 0                 Uri: The Surgical Strike             2019  Vicky Kaushal|Paresh Rawal|...
# 1                            Battalion 609             2019  Vicky Ahuja|Shoaib Ibrahim|...
# ...
# 1628                              Humsafar             2011  Fawad Khan|



print(type(ipl_matches[['Team1','Team2','WinningTeam']]))
# <class 'pandas.DataFrame'>

print(ipl_matches[['Team1','Team2','WinningTeam']])
#                            Team1                        Team2                  WinningTeam
# 0               Rajasthan Royals               Gujarat Titans               Gujarat Titans
# 1    Royal Challengers Bangalore             Rajasthan Royals             Rajasthan Royals
# 2    Royal Challengers Bangalore         Lucknow Super Giants  Royal Challengers Bangalore
# ...
# 949  Royal Challengers Bangalore        Kolkata Knight Riders        Kolkata Knight Riders








# ==================================================
# Quick Interview Revision
# ==================================================

# dataframe['column']           → returns Series
# dataframe[['col1','col2']]    → returns DataFrame

# Single []   → Series
# Double [[]] → DataFrame