import numpy as np
import pandas as pd

import os




# ==================================================
# DataFrame Attributes
# ==================================================

# Definition (Interview Friendly)
# DataFrame attributes are properties that give
# information about the structure and metadata
# of a DataFrame such as rows, columns, data types,
# indexes, and underlying values.



path_dir = os.path.dirname(__file__)

path_file_movies = os.path.join(path_dir, '../../1_Dataset/movies.csv')
path_file_ipl_matches = os.path.join(path_dir, '../../1_Dataset/ipl-matches.csv')


movies = pd.read_csv(path_file_movies)
ipl_matches = pd.read_csv(path_file_ipl_matches)



# ==================================================
# 1. shape
# ==================================================

# Interview Definition
# shape is a DataFrame attribute that returns the
# number of rows and columns in a DataFrame
# in the form of a tuple → (rows, columns)

print(movies.shape) # (1629, 18)

print(ipl_matches.shape)



# Important Points
# • First value → number of rows
# • Second value → number of columns
# • Useful for quickly understanding dataset size



# ==================================================
# 2. dtypes
# ==================================================

# Interview Definition
# dtypes attribute returns the data type of each
# column in the DataFrame.

# It helps understand whether a column contains
# integers, floats, strings, etc.


print(movies.dtypes)

# title_x                 str
# imdb_id                 str
# poster_path             str
# wiki_link               str
# title_y                 str
# original_title          str
# is_adult              int64
# year_of_release       int64
# runtime                 str
# genres                  str
# imdb_rating         float64
# imdb_votes            int64
# story                   str
# summary                 str
# tagline                 str
# actors                  str
# wins_nominations        str
# release_date            str
# dtype: object


print(ipl_matches.dtypes)

# ID                   int64
# City                   str
# Date                   str
# Season                 str
# MatchNumber            str
# Team1                  str
# Team2                  str
# Venue                  str
# TossWinner             str
# TossDecision           str
# SuperOver              str
# WinningTeam            str
# WonBy                  str
# Margin             float64
# method                 str
# Player_of_Match        str
# Team1Players           str
# Team2Players           str
# Umpire1                str
# Umpire2                str
# dtype: object



# Important Points
# • Helps in data cleaning and preprocessing
# • Shows numerical and categorical columns



# ==================================================
# 3. index
# ==================================================

# Interview Definition
# index attribute returns the row labels
# of the DataFrame.

# It represents the unique identifier
# for each row.


print(movies.index)
print(ipl_matches.index)

# RangeIndex(start=0, stop=1629, step=1)
# RangeIndex(start=0, stop=950, step=1)



# Important Points
# • Default index starts from 0
# • Index can also be custom labels



# ==================================================
# 4. columns
# ==================================================

# Interview Definition
# columns attribute returns the names
# of all columns in the DataFrame.


print(movies.columns)

# Index(['title_x', 'imdb_id', 'poster_path', 'wiki_link', 'title_y',
#        'original_title', 'is_adult', 'year_of_release', 'runtime', 'genres',
#        'imdb_rating', 'imdb_votes', 'story', 'summary', 'tagline', 'actors',
#        'wins_nominations', 'release_date'],
#         dtype='str')


print(ipl_matches.columns)

# Index(['ID', 'City', 'Date', 'Season', 'MatchNumber', 'Team1', 'Team2',     
#        'Venue', 'TossWinner', 'TossDecision', 'SuperOver', 'WinningTeam',   
#        'WonBy', 'Margin', 'method', 'Player_of_Match', 'Team1Players',      
#        'Team2Players', 'Umpire1', 'Umpire2'],
#        dtype='str')



# Important Points
# • Used to see column names quickly
# • Helps while selecting specific columns



# ==================================================
# 5. values
# ==================================================

# Interview Definition
# values attribute returns the underlying
# NumPy array of the DataFrame.

# It converts the DataFrame into a
# 2D NumPy array.


print(movies.values)


# [
#  ['Uri: The Surgical Strike' 'tt8291224'
#   'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/URI_-_New_poster.jpg/220px-URI_-_New_poster.jpg'
#   ...
#   'Vicky Kaushal|Paresh Rawal|Mohit Raina|Yami Gautam|Kirti Kulhari|Rajit Kapoor|Ivan Rodrigues|Manasi Parekh|Swaroop Sampat|Riva Arora|Yogesh Soman|Fareed Ahmed|Akashdeep Arora|Kallol Banerjee|'
#   '4 wins' '11 January 2019 (USA)']
#  ['Battalion 609' 'tt9472208' nan ...
#   'Vicky Ahuja|Shoaib Ibrahim|Shrikant Kamat|Elena Kazan|Vishwas Kini|Major Kishore|Jashn Kohli|Rammy C. Pandey|Manish Sharma|Sparsh Sharma|Farnaz Shetty|Vikas Shrivastav|Chandraprakash Thakur|Brajesh Tiwari|'
#   nan '11 January 2019 (India)']
#  ['The Accidental Prime Minister (film)' 'tt6986710'
#   'https://upload.wikimedia.org/wikipedia/en/thumb/a/a1/The_Accidental_Prime_Minister_film.jpg/220px-The_Accidental_Prime_Minister_film.jpg'
#   ...
#   'Anupam Kher|Akshaye Khanna|Aahana Kumra|Atul Sharma|Manoj Anand|Arjun Mathur|Suzanne Bernert|Abdul Quadir Amin|Bharat Mistri|Divya Seth|Anil Rastogi|Ramesh Bhatkar|Parrgash Kaur|Jess Kaur|'
#   nan '11 January 2019 (USA)']
#   ...
#  ['Sabse Bada Sukh' 'tt0069204' nan ...
#   'Vijay Arora|Asrani|Rajni Bala|Kumud Damle|Utpal Dutt|Meeta Faiyyaz|Rabi Ghosh|Tarun Ghosh|Sanjeev Kumar|Keshto Mukherjee|Meena Rai|'
#   nan nan]
#  ['Daaka' 'tt10833860'
#   'https://upload.wikimedia.org/wikipedia/en/thumb/4/45/Daaka.jpg/220px-Daaka.jpg'
#   ... 'Gippy Grewal|Zareen Khan|' nan '1 November 2019 (USA)']
#  ['Humsafar' 'tt2403201'
#   'https://upload.wikimedia.org/wikipedia/en/thumb/4/41/Flag_of_India.svg/23px-Flag_of_India.svg.png'
#   ... 'Fawad Khan|' nan 'TV Series (2011–2012)']
# ]



# Important Points
# • Returns NumPy representation of DataFrame
# • Mostly used for numerical computations



# ==================================================
# Quick Revision
# ==================================================

# shape    → lll shape returns the number of rows and columns of a DataFrame in the form of a tuple → (rows, columns)
# dtypes   → lll "Shows the data type of the values of each column in a DataFrame."
# index    → lll "Represents the labels of the DataFrame. Acts like row identifiers."
# columns  → lll columns returns the name of all columns of the DataFrame.
# values   → lll "Returns the underlying data of the DataFrame as a NumPy array."