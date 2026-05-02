


import numpy as np
import pandas as pd



import os





path_dir = os.path.dirname(__file__)
path_file_ipl_matches = os.path.join(path_dir, '../../1_Dataset/ipl-matches.csv')


ipl_matches = pd.read_csv(path_file_ipl_matches)



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
# Boolean Filtering in Pandas
# ==================================================

# Interview Definition
# --------------------
# Boolean Filtering is a Pandas technique used to select
# rows from a DataFrame based on conditions.
# It creates a boolean mask (True / False values) and
# returns only the rows where the condition is True.



# ==================================================
# Boolean Mask
# ==================================================

# Interview Definition
# --------------------
# A Boolean Mask is a Series of True and False values
# created by applying a condition on a DataFrame column.
# Pandas uses this mask to filter rows.

# Example
mask = ipl_matches['MatchNumber'] == 'Final'



# ==================================================
# Q1 : Find All Final Winners With Season
# ==================================================

# Explanation
# -----------
# We filter rows where MatchNumber = 'Final'
# and then select Season and WinningTeam columns.

mask = ipl_matches['MatchNumber'] == 'Final'
new_df = ipl_matches[mask]

print(new_df[['Season','WinningTeam']])


# Short Method
final_winners = ipl_matches[ipl_matches['MatchNumber'] == 'Final'][['Season','WinningTeam']]
print(final_winners)


# Important Points
# ----------------
# • Boolean condition creates a mask
# • Mask filters the DataFrame
# • Double brackets select specific columns


# Output
# ------
#       Season            WinningTeam
# 0       2022         Gujarat Titans
# 74      2021    Chennai Super Kings
# 134  2020/21         Mumbai Indians
# 194     2019         Mumbai Indians
# 254     2018    Chennai Super Kings
# 314     2017         Mumbai Indians
# 373     2016    Sunrisers Hyderabad
# 433     2015         Mumbai Indians
# 492     2014  Kolkata Knight Riders
# 552     2013         Mumbai Indians
# 628     2012  Kolkata Knight Riders
# 702     2011    Chennai Super Kings
# 775  2009/10    Chennai Super Kings
# 835     2009        Deccan Chargers
# 892  2007/08       Rajasthan Royals



# ==================================================
# Q2 : How Many Super Over Finishes Occurred
# ==================================================

# Explanation
# -----------
# SuperOver column contains 'Y' if super over occurred.
# We filter rows where SuperOver == 'Y'.

print(ipl_matches[ipl_matches['SuperOver'] == 'Y'])


# Count Super Over Matches
print(ipl_matches[ipl_matches['SuperOver'] == 'Y'].shape[0])  # 14


# Important Points
# ----------------
# • 'Y' represents Super Over match
# • shape[0] returns number of rows



# ==================================================
# Q3 : How Many Matches CSK Won In Kolkata
# ==================================================

# Explanation
# -----------
# Two conditions are applied:
# City = Kolkata
# WinningTeam = Chennai Super Kings

print(
    ipl_matches[
        (ipl_matches['City'] == 'Kolkata') &
        (ipl_matches['WinningTeam'] == 'Chennai Super Kings')
    ][['Venue','WinningTeam']]
)

# Count Matches
print(
    ipl_matches[
        (ipl_matches['City'] == 'Kolkata') &
        (ipl_matches['WinningTeam'] == 'Chennai Super Kings')
    ].shape[0]
)  # 5


# Important Points
# ----------------
# • '&' is used for AND condition
# • Each condition must be inside brackets
# • shape[0] gives number of rows



# ==================================================
# Q4 : Toss Winner Is Match Winner (Percentage)
# ==================================================

# Explanation
# -----------
# We filter matches where TossWinner and WinningTeam
# are the same.

toss_match_winning_df = ipl_matches[
    ipl_matches['TossWinner'] == ipl_matches['WinningTeam']
]

print(toss_match_winning_df)


# Calculate Percentage
print((toss_match_winning_df.shape[0] * 100) / ipl_matches.shape[0])

# Result
# ------
# 51.47 %



# ==================================================
# Important Boolean Operators in Pandas
# ==================================================

# AND operator
# df[(condition1) & (condition2)]

# OR operator
# df[(condition1) | (condition2)]

# NOT operator
# df[~(condition)]



# ==================================================
# Quick Revision
# ==================================================

# Boolean Filtering → Selecting rows using conditions
# Boolean Mask → True/False Series used for filtering
# '&' → AND condition
# '|' → OR condition
# '~' → NOT condition
# shape[0] → Number of rows