


import numpy as np
import pandas as pd

import os



path_dir = os.path.dirname(__file__)

path_file_deliveries = os.path.join(path_dir, '../1_Dataset/deliveries.csv')



ipl = pd.read_csv(path_file_deliveries)

print(ipl.columns)

# Index(['match_id', 'inning', 'batting_team', 'bowling_team', 'over', 'ball',
#        'batsman', 'non_striker', 'bowler', 'is_super_over', 'wide_runs',
#        'bye_runs', 'legbye_runs', 'noball_runs', 'penalty_runs',
#        'batsman_runs', 'extra_runs', 'total_runs', 'player_dismissed',
#        'dismissal_kind', 'fielder'],
#       dtype='str')




# Ques : Find the top 10 bastman in terms of runs 
#-------------------------------------------------


print(ipl.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10))

# batsman
# V Kohli           5434
# SK Raina          5415
# RG Sharma         4914
# DA Warner         4741
# S Dhawan          4632
# CH Gayle          4560
# MS Dhoni          4477
# RV Uthappa        4446
# AB de Villiers    4428
# G Gambhir         4223
# Name: batsman_runs, dtype: int64


# Ques : Find the batsman with max no of sixes
#----------------------------------------------

print(ipl[ipl['batsman_runs'] == 6].groupby('batsman')['batsman'].count().sort_values(ascending=False).head(1))
# CH Gayle    327
# Name: batsman, dtype: int64





# Ques : Find bastman with most number of 4's and 6's in last 5 overs
#---------------------------------------------------------------------

print(ipl[(15 < ipl['over']) & ((ipl['batsman_runs'] == 4) | (ipl['batsman_runs'] == 6))].groupby('batsman')['batsman'].count().sort_values(ascending=False).head(1))

# batsman
# MS Dhoni    340
# Name: batsman, dtype: int64





# Ques : Find Kohli's record against all teams(in term of vk_runs, vk_min, vk_max, vk_avg, vk_4, vk_6)
#----------------------------------------------------------------



def vk_record_team(group):
    return {
        'vk_runs': group['batsman_runs'].sum(),
        'vk_min': group['batsman_runs'].min(),
        'vk_max': group['batsman_runs'].max(),
        'vk_avg': group['batsman_runs'].mean(),
        'vk_4': (group['batsman_runs'] == 4).sum(),
        'vk_6': (group['batsman_runs'] == 6).sum()
    }
     
 


print(ipl[ipl['batsman'] == 'V Kohli'].groupby('bowling_team').apply(vk_record_team))


# bowling_team
# Chennai Super Kings        {'vk_runs': 749, 'vk_min': 0, 'vk_max': 6, 'vk...
# Deccan Chargers            {'vk_runs': 306, 'vk_min': 0, 'vk_max': 6, 'vk...
# Delhi Capitals             {'vk_runs': 66, 'vk_min': 0, 'vk_max': 6, 'vk_...
# Delhi Daredevils           {'vk_runs': 763, 'vk_min': 0, 'vk_max': 6, 'vk...
# Gujarat Lions              {'vk_runs': 283, 'vk_min': 0, 'vk_max': 6, 'vk...
# Kings XI Punjab            {'vk_runs': 636, 'vk_min': 0, 'vk_max': 6, 'vk...
# Kochi Tuskers Kerala       {'vk_runs': 50, 'vk_min': 0, 'vk_max': 4, 'vk_...
# Kolkata Knight Riders      {'vk_runs': 675, 'vk_min': 0, 'vk_max': 6, 'vk...
# Mumbai Indians             {'vk_runs': 628, 'vk_min': 0, 'vk_max': 6, 'vk...
# Pune Warriors              {'vk_runs': 128, 'vk_min': 0, 'vk_max': 6, 'vk...
# Rajasthan Royals           {'vk_runs': 370, 'vk_min': 0, 'vk_max': 6, 'vk...
# Rising Pune Supergiant     {'vk_runs': 83, 'vk_min': 0, 'vk_max': 6, 'vk_...
# Rising Pune Supergiants    {'vk_runs': 188, 'vk_min': 0, 'vk_max': 6, 'vk...
# Sunrisers Hyderabad        {'vk_runs': 509, 'vk_min': 0, 'vk_max': 6, 'vk...
# dtype: object


vk = ipl[ipl['batsman'] == 'V Kohli']

result = vk.groupby('bowling_team').agg(
    vk_runs=('batsman_runs', 'sum'),
    vk_min=('batsman_runs', 'min'),
    vk_max=('batsman_runs', 'max'),
    vk_avg=('batsman_runs', 'mean'),
    vk_4=('batsman_runs', lambda x: (x == 4).sum()),
    vk_6=('batsman_runs', lambda x: (x == 6).sum())
)

print(result)

#                          vk_runs  vk_min  vk_max    vk_avg  vk_4  vk_6
# bowling_team
# Chennai Super Kings          749       0       6  1.215909    57    30
# Deccan Chargers              306       0       6  1.330435    23    14
# Delhi Capitals                66       0       6  1.320000     3     3
# Delhi Daredevils             763       0       6  1.379747    74    22
# Gujarat Lions                283       0       6  1.521505    24    11
# Kings XI Punjab              636       0       6  1.284848    74    18
# Kochi Tuskers Kerala          50       0       4  0.961538     7     0
# Kolkata Knight Riders        675       0       6  1.310680    58    22
# Mumbai Indians               628       0       6  1.263581    52    24
# Pune Warriors                128       0       6  1.267327     9     5
# Rajasthan Royals             370       0       6  1.054131    29    10
# Rising Pune Supergiant        83       0       6  1.238806     7     2
# Rising Pune Supergiants      188       0       6  1.468750    15     9
# Sunrisers Hyderabad          509       0       6  1.375676    50    21




# Ques : Create a function that can return the highest score of any batsman
#----------------------------------------------------------------------------

def heighest_match_score(batsman_name):
    return ipl[ipl['batsman'] == batsman_name].groupby('match_id')['batsman_runs'].sum().sort_values(ascending=False).head(1).values[0]

print(heighest_match_score('MS Dhoni')) # 89
print(heighest_match_score('V Kohli')) # 113