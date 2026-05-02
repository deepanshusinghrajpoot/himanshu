import numpy as np
import pandas as pd
import os



# ==================================================
# Pandas Series Indexing
# ==================================================

# Definition (Interview Friendly)
#     We know. We are accessing elements from a Pandas Series
#     using either integer index or custom index.
#     We can create our won custum index using index_col parameter


# Important Points
# • Series supports both integer indexing and label indexing
# • Integer indexing starts from 0
# • Label indexing uses the index name
# • Series behaves similar to a Python dictionary when labels exist



path_dir = os.path.dirname(__file__)
file_path1 = os.path.join(path_dir, '../../1_Dataset/bollywood.csv')

movies = pd.read_csv(file_path1, index_col='movie').squeeze('columns')
print(movies)

# movie
# Uri: The Surgical Strike                   Vicky Kaushal
# Battalion 609                                Vicky Ahuja
# The Accidental Prime Minister (film)         Anupam Kher
# Why Cheat India                            Emraan Hashmi
# Evening Shadows                         Mona Ambegaonkar
#                                               ...
# Hum Tumhare Hain Sanam                    Shah Rukh Khan
# Aankhen (2002 film)                     Amitabh Bachchan
# Saathiya (film)                             Vivek Oberoi
# Company (film)                                Ajay Devgn
# Awara Paagal Deewana                        Akshay Kumar
# Name: lead, Length: 1500, dtype: str



# ==================================================
# 1. Integer Indexing
# ==================================================

# Definition (Interview Friendly)
# Integer indexing means accessing elements using their position.
# Index starts from 0 just like Python lists.

# Important Points
# • Works using integer positions
# • Starts from index 0
# • Mostly used when Series has default numeric index


x = pd.Series(np.arange(12, 24))

print(x[0])
print(x[5])
print(x[9])

# Output
# 12
# 17
# 21



# ==================================================
# 2. Label Indexing
# ==================================================

# Definition (Interview Friendly)
# Label indexing means accessing data using the index label instead
# of the numeric position.

# Important Points
# • Works when Series has meaningful index labels
# • Very useful in real datasets
# • Similar to dictionary key access


print(movies['Uri: The Surgical Strike'])

# Output
# Vicky Kaushal



# ==================================================
# Quick Revision
# ==================================================

# Integer Indexing → Access by position
# Example: series[0]

# Label Indexing → Access by index name
# Example: series['movie name']

# Pandas Series supports both indexing styles