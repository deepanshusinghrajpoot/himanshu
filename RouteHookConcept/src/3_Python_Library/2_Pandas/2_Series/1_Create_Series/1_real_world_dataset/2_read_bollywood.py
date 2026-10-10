# ==========================================
# Pandas Series: From bollywood.csv Dataset
# ==========================================

import pandas as pd
import os

# ✅ Definition:
# A Pandas Series can be created from a single column of a CSV.
# - read_csv() reads the CSV into a DataFrame.
# - squeeze('columns') converts a single-column DataFrame into a Series.
# - index_col parameter allows setting a column as the Series index.

# ------------------------------------------------
# Step 1: Get the CSV file path
# ------------------------------------------------
path_dir = os.path.dirname(__file__)
file_path = os.path.join(path_dir, '../../../1_Dataset/bollywood.csv')
print(file_path)
# Example Output:
# c:\path\to\your\project\1_Dataset\bollywood.csv

# ------------------------------------------------
# Step 2: Read CSV and convert to Series
# ------------------------------------------------
# Set 'movie' as the index
movies = pd.read_csv(file_path, index_col='movie').squeeze('columns')
print(type(movies))
# Output: <class 'pandas.Series'>

# ------------------------------------------------
# Step 3: Inspect the Series
# ------------------------------------------------
print(movies)
# Example Output:
# movie
# Uri: The Surgical Strike                   Vicky Kaushal
# Battalion 609                                Vicky Ahuja
# The Accidental Prime Minister (film)         Anupam Kher
# Why Cheat India                            Emraan Hashmi
# Evening Shadows                         Mona Ambegaonkar
# ...
# Hum Tumhare Hain Sanam                    Shah Rukh Khan
# Aankhen (2002 film)                     Amitabh Bachchan
# Saathiya (film)                             Vivek Oberoi
# Company (film)                                Ajay Devgn
# Awara Paagal Deewana                        Akshay Kumar
# Name: lead, Length: 1500, dtype: str

# ✅ Quick Notes:
# - Column name ('lead') becomes the Series name.
# - Index column ('movie') becomes the Series index.
# - Useful for mapping movie names to lead actors.
# - squeeze() ensures the object is a Series when CSV has a single column.

# ⚡ Tip:
# Always use index_col when you want meaningful indices for quick access.