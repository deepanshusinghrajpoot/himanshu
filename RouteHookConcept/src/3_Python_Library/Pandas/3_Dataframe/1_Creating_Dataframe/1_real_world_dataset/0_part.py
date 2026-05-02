import numpy as np
import pandas as pd

import os



# ==================================================
# Creating DataFrame from Real-World Dataset
# ==================================================

# Definition (Interview Friendly)
# In real-world data analysis, DataFrames are usually created
# by reading external data files such as CSV, Excel, JSON, etc.

# The most common method is read_csv() which loads
# comma-separated values (CSV) files into a Pandas DataFrame.



# ==================================================
# What is a CSV File?
# ==================================================

# CSV (Comma Separated Values) is a file format where
# data values are separated using commas.

# Example CSV structure

# name,age,city
# Rahul,23,Delhi
# Aman,25,Mumbai



# ==================================================
# Creating DataFrame using read_csv()
# ==================================================

# Syntax
# pd.read_csv("file_path")

# Important Points
# • read_csv() reads the file and converts it into a DataFrame
# • Each row in the CSV becomes a row in the DataFrame
# • Each column in the CSV becomes a column in the DataFrame
# • Widely used for real-world datasets



path_dir = os.path.dirname(__file__)
file_path_movies = os.path.join(path_dir, '../../../1_Dataset/movies.csv')



movies = pd.read_csv(file_path_movies)
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



# Explanation
# movies.csv file is loaded into a DataFrame
# It contains 1629 rows and 18 columns
# Each row represents a movie record



# ==================================================
# Another Example Dataset
# IPL Matches Dataset
# ==================================================

# DataFrame can also be created from any CSV dataset
# such as sports data, sales data, etc.



file_path_ipl_matches = os.path.join(path_dir, '../../../1_Dataset/ipl-matches.csv')

ipl_matches = pd.read_csv(file_path_ipl_matches)
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



# Explanation
# ipl-matches.csv dataset is loaded into a DataFrame
# It contains IPL match details like:
# • City
# • Teams
# • Umpires
# • Match ID



# ==================================================
# Quick Revision
# ==================================================

# read_csv() → used to load CSV file into DataFrame

# Syntax
# pd.read_csv("file_path")

# CSV file → comma separated values

# Real-world datasets are usually loaded using read_csv()