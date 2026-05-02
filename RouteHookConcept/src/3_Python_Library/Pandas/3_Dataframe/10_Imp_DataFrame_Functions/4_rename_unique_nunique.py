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





path_dir = os.path.dirname(__file__)
movies_file_path = os.path.join(path_dir, '../../1_Dataset/movies.csv')


movies = pd.read_csv(movies_file_path)
print(movies.columns)

# Index(['title_x', 'imdb_id', 'poster_path', 'wiki_link', 'title_y',
#        'original_title', 'is_adult', 'year_of_release', 'runtime', 'genres',
#        'imdb_rating', 'imdb_votes', 'story', 'summary', 'tagline', 'actors',
#        'wins_nominations', 'release_date'],
#        dtype='str')


movies.set_index('title_x', inplace=True)

print(movies)

#                                          imdb_id                                        poster_path  ...        wins_nominations              release_date
# title_x                                                                                              ...
# Uri: The Surgical Strike               tt8291224  https://upload.wikimedia.org/wikipedia/en/thum...  ...                  4 wins     11 January 2019 (USA)   
# Battalion 609                          tt9472208                                                NaN  ...                     NaN   11 January 2019 (India)   
# The Accidental Prime Minister (film)   tt6986710  https://upload.wikimedia.org/wikipedia/en/thum...  ...                     NaN     11 January 2019 (USA)   
# Why Cheat India                        tt8108208  https://upload.wikimedia.org/wikipedia/en/thum...  ...                     NaN     18 January 2019 (USA)   
# Evening Shadows                        tt6028796                                                NaN  ...  17 wins & 1 nomination   11 January 2019 (India)   
# ...                                          ...                                                ...  ...                     ...                       ...   
# Tera Mera Saath Rahen                  tt0301250  https://upload.wikimedia.org/wikipedia/en/2/2b...  ...                     NaN   7 November 2001 (India)   
# Yeh Zindagi Ka Safar                   tt0298607  https://upload.wikimedia.org/wikipedia/en/thum...  ...                     NaN  16 November 2001 (India)   
# Sabse Bada Sukh                        tt0069204                                                NaN  ...                     NaN                       NaN   
# Daaka                                 tt10833860  https://upload.wikimedia.org/wikipedia/en/thum...  ...                     NaN     1 November 2019 (USA)   
# Humsafar                               tt2403201  https://upload.wikimedia.org/wikipedia/en/thum...  ...                     NaN     TV Series (2011–2012)   
#
# [1629 rows x 17 columns]



# 6. rename(dataframe) :- Perfect Interview Spoken Definition
#=============================================================
# rename() is a pandas DataFrame method used to change the names of
# columns or index labels without modifying the original data.

# Important Parameters
#---------------------
# columns -> dictionary used to rename column names
# index   -> dictionary used to rename index labels
# inplace -> True makes the change permanent



movies.rename(columns={'imdb_id':'imdb', 'poster_path':'link'}, inplace=True)

print(movies)

#                                             imdb                                               link  ...        wins_nominations              release_date
# title_x                                                                                              ...
# Uri: The Surgical Strike               tt8291224  https://upload.wikimedia.org/wikipedia/en/thum...  ...                  4 wins     11 January 2019 (USA)
# Battalion 609                          tt9472208                                                NaN  ...                     NaN   11 January 2019 (India)
# The Accidental Prime Minister (film)   tt6986710  https://upload.wikimedia.org/wikipedia/en/thum...  ...                     NaN     11 January 2019 (USA)
# Why Cheat India                        tt8108208  https://upload.wikimedia.org/wikipedia/en/thum...  ...                     NaN     18 January 2019 (USA)
# Evening Shadows                        tt6028796                                                NaN  ...  17 wins & 1 nomination   11 January 2019 (India)
# ...
# [1629 rows x 17 columns]



# We can also change index names
#-------------------------------

movies.rename(index={'Uri: The Surgical Strike':'Uri', 'Battalion 609':'Battalion'}, inplace=True)

print(movies)

#                                             imdb                                               link  ...        wins_nominations              release_date
# title_x                                                                                              ...
# Uri                                    tt8291224  https://upload.wikimedia.org/wikipedia/en/thum...  ...                  4 wins     11 January 2019 (USA)
# Battalion                              tt9472208                                                NaN  ...                     NaN   11 January 2019 (India)
# ...
# [1629 rows x 17 columns]



# 7. unique(series) :- Perfect Interview Spoken Definition
#=========================================================
# unique() is a pandas Series method used to return all distinct
# or unique values present in a Series. It returns the result as a NumPy array.

temp = pd.Series([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, np.nan, np.nan])

print(temp)

# 0     1.0
# 1     1.0
# 2     2.0
# 3     2.0
# 4     3.0
# 5     3.0
# 6     4.0
# 7     4.0
# 8     5.0
# 9     5.0
# 10    NaN
# 11    NaN
# dtype: float64


print(temp.unique())  
# [ 1.  2.  3.  4.  5. nan]



# 8. nunique(series + dataframe) :- Perfect Interview Spoken Definition
#=======================================================================
# nunique() is a pandas method used to count the number of distinct
# or unique values in a Series or DataFrame.

# Important Parameter
#--------------------
# dropna -> True (default)  : NaN values are not counted
# dropna -> False           : NaN values are counted



print(temp.unique().shape[0]) 
# 6


print(temp.nunique()) 
# 5