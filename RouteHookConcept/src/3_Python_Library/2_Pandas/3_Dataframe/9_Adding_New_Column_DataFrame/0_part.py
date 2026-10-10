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
# Adding New Columns in Pandas DataFrame
# ==================================================

# Interview Definition
# --------------------
# In Pandas, we can create new columns in a DataFrame
# either by assigning a constant value or by deriving
# values from existing columns.



# ==================================================
# Method 1 : Adding Column With Constant Value
# ==================================================

# Explanation
# -----------
# A new column can be created by assigning a single value.
# Pandas automatically fills that value for all rows.

# Syntax
# ------
# dataframe['new_column_name'] = value


# Example

movies['Country'] = 'India'

print(movies['Country'])

# Output
# ------
# 0       India
# 1       India
# 2       India
# 3       India
# 4       India
# ...
# 1628    India



# Important Points
# ----------------
# • If column does not exist → Pandas creates a new column
# • Value is automatically broadcast to all rows
# • Very useful when adding labels or categories



# ==================================================
# Method 2 : Creating Column From Existing Column
# ==================================================

# Interview Definition
# --------------------
# A new column can be created by applying operations
# or transformations on existing columns.


# Example Task
# ------------
# Create a new column "lead actors"
# which stores the first actor from the actors column.



# ==================================================
# Handling Missing Values
# ==================================================

# Explanation
# -----------
# Some rows may contain NaN values in the actors column.
# We remove them before processing.

movies.dropna(inplace=True)



# ==================================================
# Extract First Actor
# ==================================================

# Explanation
# -----------
# actors column contains multiple actors separated by '|'
# We split the string and select the first actor.

movies['lead actors'] = movies['actors'].str.split('|').apply(lambda x: x[0])

print(movies['lead actors'])



# Output Example
# --------------
# 11             Ranveer Singh
# 34              Gavie Chahal
# 37        Ayushmann Khurrana
# 87         Sidharth Malhotra
# 96                Ajay Devgn
# ...
# 1623          Karisma Kapoor



# ==================================================
# Important String Methods Used
# ==================================================

# str.split('|')
# Splits the string into a list using '|' separator.

# apply(lambda x: x[0])
# Applies a function to each row and returns the first element.



# ==================================================
# Quick Revision
# ==================================================

# Add column
# ----------
# df['new_column'] = value


# Create column from existing column
# ----------------------------------
# df['new_column'] = df['old_column'].operation()


# String processing
# -----------------
# str.split('|')
# apply(lambda x: x[0])


# Remove missing values
# ---------------------
# df.dropna(inplace=True)