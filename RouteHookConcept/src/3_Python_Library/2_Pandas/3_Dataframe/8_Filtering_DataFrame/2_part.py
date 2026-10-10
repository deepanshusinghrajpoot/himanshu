
import numpy as np
import pandas as pd



import os





path_dir = os.path.dirname(__file__)
path_file_movies = os.path.join(path_dir, '../../1_Dataset/movies.csv')


movies = pd.read_csv(path_file_movies)


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







# ==================================================
# Boolean Filtering with Multiple Conditions
# (Movies Dataset)
# ==================================================

# Interview Definition
# --------------------
# Boolean Filtering is used to select rows from a DataFrame
# based on one or more conditions.
# It returns only those rows where the condition evaluates to True.



# ==================================================
# Important Boolean Operators in Pandas
# ==================================================

# &  → AND condition
# |  → OR condition
# ~  → NOT condition

# Important Rule
# --------------
# • Every condition must be inside brackets ()
# • Use & instead of 'and'
# • Use | instead of 'or'



# ==================================================
# Q1 : Movies With Rating > 8 And Votes > 10000
# ==================================================

# Explanation
# -----------
# We apply two conditions:
# 1. imdb_rating > 8
# 2. imdb_votes > 10000

print(movies[(movies['imdb_rating'] > 8) & (movies['imdb_votes'] > 10000)])


# Important Points
# ----------------
# • '&' combines multiple conditions
# • Both conditions must be True
# • Returns highly rated popular movies



# Small Example (Understanding Mask)
# ----------------------------------

rating_mask = movies['imdb_rating'] > 8
votes_mask = movies['imdb_votes'] > 10000

print(rating_mask)
print(votes_mask)



# ==================================================
# String Filtering in Pandas
# ==================================================

# Interview Definition
# --------------------
# String filtering is used when we want to filter rows
# based on text patterns inside string columns.

# Important Methods
# -----------------
# str.contains()
# str.split()
# str.startswith()
# str.endswith()



# ==================================================
# Q2 : Action Movies With Rating > 7.5
# ==================================================

# Method 1 : Using split()

mask1 = movies['genres'].str.split('|').apply(lambda x: 'Action' in x)


# Method 2 : Using contains() (Simpler)

mask1 = movies['genres'].str.contains('Action')


# Rating condition

mask2 = movies['imdb_rating'] > 7.5


# Final Filter

print(movies[mask1 & mask2])



# Important Points
# ----------------
# • genres column contains multiple genres separated by '|'
# • str.contains() checks if "Action" exists in the string
# • mask1 → Action movies
# • mask2 → High rating movies



# Example Output Column

print(movies[mask1 & mask2]['genres'])



# ==================================================
# Quick Revision
# ==================================================

# Boolean Filtering → Select rows based on conditions
# '&' → AND condition
# '|' → OR condition
# '~' → NOT condition
# str.contains() → Search text inside column
# str.split() → Split string values

# Example
# -------
# df[(df['rating'] > 8) & (df['votes'] > 10000)]