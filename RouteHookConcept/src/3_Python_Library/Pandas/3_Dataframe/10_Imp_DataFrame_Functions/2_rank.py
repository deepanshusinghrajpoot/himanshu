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


import os




path_dir = os.path.dirname(__file__)
bastman_run_ipl = os.path.join(path_dir, '../../1_Dataset/batsman_runs_ipl.csv')


bastman_run = pd.read_csv(bastman_run_ipl)

print(bastman_run)

#              batter  batsman_run
# 0    A Ashish Reddy          280
# 1          A Badoni          161
# 2        A Chandila            4
# 3          A Chopra           53
# 4       A Choudhary           25
# ..              ...          ...
# 600      Yash Dayal            0
# 601   Yashpal Singh           47
# 602     Younis Khan            3
# 603    Yuvraj Singh         2754
# 604          Z Khan          117
#
# [605 rows x 2 columns]



# =============================================================================
# 19. rank() (Series)
# =============================================================================

# lll rank() is a pandas Series method used to assign ranks
# to values based on their order.

# By default:
# Smallest value gets Rank 1

# If duplicate values exist:
# rank() gives average rank by default.




# Important Parameters
# ---------------------

# ascending ->
# True  : smallest gets rank 1 (default)
# False : largest gets rank 1

# method ->
# 'average' : average rank (default)
# 'min'     : lowest rank
# 'max'     : highest rank
# 'first'   : order of appearance
# 'dense'   : consecutive ranks

# na_option ->
# 'keep'   : keep NaN
# 'top'    : rank NaN first
# 'bottom' : rank NaN last

# pct ->
# True : percentage rank


# eg:

# [10, 20, 20, 30, 40]

# | Value | Position |
# | ----- | -------- |
# | 10    | 1        |
# | 20    | 2        |
# | 20    | 3        |
# | 30    | 4        |
# | 40    | 5        |

# | Value | Rank |
# | ----- | ---- |
# | 10    | 1    |
# | 20    | 2    |
# | 20    | 2    |
# | 30    | 3    |
# | 40    | 4    |


# Final Output for Each Method

# | Method  | Result                |
# | ------- | --------------------- |
# | average | `[1, 2.5, 2.5, 4, 5]` |
# | min     | `[1, 2, 2, 4, 5]`     |
# | max     | `[1, 3, 3, 4, 5]`     |
# | first   | `[1, 2, 3, 4, 5]`     |
# | dense   | `[1, 2, 2, 3, 4]`     |




print(bastman_run['batsman_run'].rank())

# 0      439.5
# 1      380.0
# 2       71.0
# 3      277.0
# 4      203.5
#        ...
# 600     12.0
# 601    263.0
# 602     58.5
# 603    579.0
# 604    350.0
# Name: batsman_run, Length: 605, dtype: float64



# Ranking in descending order (Highest runs gets Rank 1)
#-------------------------------------------------------

print(bastman_run['batsman_run'].rank(ascending=False))

# 0      166.5
# 1      226.0
# 2      535.0
# 3      329.0
# 4      402.5
#        ...
# 600    594.0
# 601    343.0
# 602    547.5
# 603     27.0
# 604    256.0
# Name: batsman_run, Length: 605, dtype: float64



# Creating a new column for ranking
#----------------------------------

bastman_run['rank'] = bastman_run['batsman_run'].rank(ascending=False)

print(bastman_run)

#              batter  batsman_run   rank
# 0    A Ashish Reddy          280  166.5
# 1          A Badoni          161  226.0
# 2        A Chandila            4  535.0
# 3          A Chopra           53  329.0
# 4       A Choudhary           25  402.5
# ..              ...          ...    ...
# 600      Yash Dayal            0  594.0
# 601   Yashpal Singh           47  343.0
# 602     Younis Khan            3  547.5
# 603    Yuvraj Singh         2754   27.0
# 604          Z Khan          117  256.0
#
# [605 rows x 3 columns]



# Sorting players by rank (Top run scorers first)
#------------------------------------------------

print(bastman_run.sort_values('rank'))

#              batter  batsman_run   rank
# 569         V Kohli         6634    1.0
# 462        S Dhawan         6244    2.0
# 130       DA Warner         5883    3.0
# 430       RG Sharma         5881    4.0
# 493        SK Raina         5536    5.0
# ..              ...          ...    ...
# 570  V Pratap Singh            0  594.0
# 63     Abdur Razzak            0  594.0
# 562          U Kaul            0  594.0
# 65       Akash Deep            0  594.0
# 57           AS Roy            0  594.0
#
# [605 rows x 3 columns]