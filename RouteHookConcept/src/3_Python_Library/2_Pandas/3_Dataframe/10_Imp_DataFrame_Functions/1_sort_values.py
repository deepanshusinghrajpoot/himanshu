#####################################################################

# 1. astype
# 2. value_counts (series and dataframe) :- gpt give perfect interview spoken diffinition

# 3. rank (series) :- gpt give perfect interview spoken diffinition

# 4. sort index (series and dataframe) :- gpt give perfect interview spoken diffinition

# 5. set index (series and dataframe) :- gpt give perfect interview spoken diffinition

# 6. rename index -> rename (series and dataframe) :- gpt give perfect interview spoken diffinition

# 7. reset index (series and dataframe) :- gpt give perfect interview spoken diffinition

# 8. unique & nunique (series and dataframe) :- gpt give perfect interview spoken diffinition

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





 
# Important DataFrame Functions
#===============================


# ========================================================
# sort_values() (Series + DataFrame) :- Perfect Interview Definition
# ========================================================

# sort_values() is a pandas method used to sort the data
# based on values in a Series or one or more columns in a DataFrame.

# It returns a sorted object without modifying the original
# data unless inplace=True is used.

# --------------------------------------------------------
# How it Works
# --------------------------------------------------------

# Series    -> sorts values in ascending or descending order
# DataFrame -> sorts rows based on one or more column values

# --------------------------------------------------------
# Important Parameters
# --------------------------------------------------------

# by       -> column name(s) to sort (DataFrame only)
# ascending -> True  : ascending order (default)
#             False : descending order
# inplace  -> True  : modifies original data
#             False : returns new object (default)
# na_position -> 'first' or 'last' (position of NaN)

# --------------------------------------------------------
# Syntax
# --------------------------------------------------------

# Series
# s.sort_values()

# DataFrame
# df.sort_values(by='marks')

# --------------------------------------------------------
# Example
# --------------------------------------------------------

# Series
# df['marks'].sort_values()

# DataFrame (single column)
# df.sort_values(by='marks')

# DataFrame (multiple columns)
# df.sort_values(by=['marks', 'iq'], ascending=[False, True])

# --------------------------------------------------------
# Key Point
# --------------------------------------------------------

# Sorting is based on values, not index (use sort_index() for index).

# --------------------------------------------------------
# One-Line Answer
# --------------------------------------------------------

# sort_values() sorts data based on values in a Series
# or columns in a DataFrame.


print(marks.iloc[4].sort_values())

# package    14
# marks      70
# iq         80
# Name: 4, dtype: int64



print(marks.sort_values('iq'))

#     iq  marks  package
# 3   80     70       14
# 4   80     70       14
# 1   90     70        7
# 0  100     80       10
# 2  120    100       14



students = pd.DataFrame(
    {
        'name':['nitish', 'ankit', 'rupesh', np.nan, 'mrityunjay', np.nan, 'rishabh', np.nan, 'aditya', np.nan],
        'college':['bit', 'iit', 'vit', np.nan, np.nan, 'vlsi', 'ssit', np.nan, np.nan, 'git'],
        'cgpa':[6.66, 8.25, 6.41, np.nan, 5.6, 9.0, 7.4, np.nan, np.nan, np.nan],
        'package':[4, 5, 6, np.nan, 6, 7, 8, 9, np.nan, np.nan]
    }
)

print(students)

#          name college  cgpa  package
# 0      nitish     bit  6.66      4.0
# 1       ankit     iit  8.25      5.0
# 2      rupesh     vit  6.41      6.0
# 3         NaN     NaN   NaN      NaN
# 4  mrityunjay     NaN  5.60      6.0
# 5         NaN    vlsi  9.00      7.0
# 6     rishabh    ssit  7.40      8.0
# 7         NaN     NaN   NaN      9.0
# 8      aditya     NaN   NaN      NaN
# 9         NaN     git   NaN      NaN



# Note : sort_values() method by default places NaN values at the end
#--------------------------------------------------------------------

print(students.sort_values('name'))

#          name college  cgpa  package
# 8      aditya     NaN   NaN      NaN
# 1       ankit     iit  8.25      5.0
# 4  mrityunjay     NaN  5.60      6.0
# 0      nitish     bit  6.66      4.0
# 6     rishabh    ssit  7.40      8.0
# 2      rupesh     vit  6.41      6.0
# 3         NaN     NaN   NaN      NaN
# 5         NaN    vlsi  9.00      7.0
# 7         NaN     NaN   NaN      9.0
# 9         NaN     git   NaN      NaN



# Note : sort_values() method by default places NaN values at the end
# but we can move them to the top using na_position='first'
#------------------------------------------------------------

print(students.sort_values('name', na_position='first'))

#          name college  cgpa  package
# 3         NaN     NaN   NaN      NaN
# 5         NaN    vlsi  9.00      7.0
# 7         NaN     NaN   NaN      9.0
# 9         NaN     git   NaN      NaN
# 8      aditya     NaN   NaN      NaN
# 1       ankit     iit  8.25      5.0
# 4  mrityunjay     NaN  5.60      6.0
# 0      nitish     bit  6.66      4.0
# 6     rishabh    ssit  7.40      8.0
# 2      rupesh     vit  6.41      6.0



# Note :- inplace=True
#---------------------
# Used when we want to apply changes permanently to the original DataFrame.



# Sort using multiple columns
#----------------------------

print(
    movies.sort_values(
        ['year_of_release', 'title_x'],
        ascending=[True, False]
    )[['year_of_release', 'title_x']]
)

# 'year_of_release' sorted in ascending order
# 'title_x' sorted in descending order

#       year_of_release                               title_x
# 1623             2001                              Zubeidaa
# 1625             2001                  Yeh Zindagi Ka Safar
# 1622             2001         Yeh Teraa Ghar Yeh Meraa Ghar
# 1620             2001              Yeh Raaste Hain Pyaar Ke
# 1573             2001                   Yaadein (2001 film)
# ...               ...                                   ...
# 37               2019                     Article 15 (film)
# 46               2019                         Arjun Patiala
# 10               2019                                Amavas
# 26               2019  Albert Pinto Ko Gussa Kyun Aata Hai?
# 21               2019                              22 Yards

# [1629 rows x 2 columns]