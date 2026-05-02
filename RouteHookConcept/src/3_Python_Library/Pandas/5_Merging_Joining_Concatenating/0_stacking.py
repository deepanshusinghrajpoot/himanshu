


import numpy as np
import pandas as pd


import os


path_dir = os.path.dirname(__file__)


path_file_courses = os.path.join(path_dir, '../1_Dataset/courses.csv')
path_file_students = os.path.join(path_dir, '../1_Dataset/students.csv')
path_file_reg_month_1 = os.path.join(path_dir, '../1_Dataset/reg-month1.csv')
path_file_reg_month_2 = os.path.join(path_dir, '../1_Dataset/reg-month2.csv')
path_file_deliveries = os.path.join(path_dir, '../1_Dataset/deliveries.csv')
path_file_matches = os.path.join(path_dir, '../1_Dataset/matches.csv')

courses = pd.read_csv(path_file_courses)
students = pd.read_csv(path_file_students)
nov = pd.read_csv(path_file_reg_month_1)
dec = pd.read_csv(path_file_reg_month_2)

matches = pd.read_csv(path_file_matches)
delivery = pd.read_csv(path_file_deliveries)


print(courses.info())
# <class 'pandas.DataFrame'>
# RangeIndex: 12 entries, 0 to 11
# Data columns (total 3 columns):
#      Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
# 0   course_id    12 non-null     int64
# 1   course_name  12 non-null     str
# 2   price        12 non-null     int64
# dtypes: int64(2), str(1)
# memory usage: 420.0 bytes
# None


print(students.info())
# <class 'pandas.DataFrame'>
# RangeIndex: 25 entries, 0 to 24
# Data columns (total 3 columns):
#     Column      Non-Null Count  Dtype
#---  ------      --------------  -----
# 0   student_id  25 non-null     int64
# 1   name        25 non-null     str
# 2   partner     25 non-null     int64
# dtypes: int64(2), str(1)
# memory usage: 732.0 bytes
# None


print(nov.info())
# <class 'pandas.DataFrame'>
# RangeIndex: 25 entries, 0 to 24
# Data columns (total 2 columns):
#     Column      Non-Null Count  Dtype
#---  ------      --------------  -----
# 0   student_id  25 non-null     int64
# 1   course_id   25 non-null     int64
# dtypes: int64(2)
# memory usage: 532.0 bytes
# None


print(dec.info())
# <class 'pandas.DataFrame'>
# RangeIndex: 28 entries, 0 to 27
# Data columns (total 2 columns):
#     Column      Non-Null Count  Dtype
#---  ------      --------------  -----
# 0   student_id  28 non-null     int64
# 1   course_id   28 non-null     int64
# dtypes: int64(2)
# memory usage: 580.0 bytes
# None


print(matches.info())
# <class 'pandas.DataFrame'>
# RangeIndex: 636 entries, 0 to 635
# Data columns (total 18 columns):
#     Column           Non-Null Count  Dtype
#---  ------           --------------  -----
# 0   id               636 non-null    int64
# 1   season           636 non-null    int64
# 2   city             629 non-null    str
# 3   date             636 non-null    str
# 4   team1            636 non-null    str
# 5   team2            636 non-null    str
# 6   toss_winner      636 non-null    str
# 7   toss_decision    636 non-null    str
# 8   result           636 non-null    str
# 9   dl_applied       636 non-null    int64
# 10  winner           633 non-null    str
# 11  win_by_runs      636 non-null    int64
# 12  win_by_wickets   636 non-null    int64
# 13  player_of_match  633 non-null    str
# 14  venue            636 non-null    str
# 15  umpire1          635 non-null    str
# 16  umpire2          635 non-null    str
# 17  umpire3          0 non-null      float64
# dtypes: float64(1), int64(5), str(12)
# memory usage: 89.6 KB
# None



print(delivery.info())
# <class 'pandas.DataFrame'>
# RangeIndex: 179078 entries, 0 to 179077
# Data columns (total 21 columns):
#     Column            Non-Null Count   Dtype
#---  ------            --------------   -----
# 0   match_id          179078 non-null  int64
# 1   inning            179078 non-null  int64
# 2   batting_team      179078 non-null  str
# 3   bowling_team      179078 non-null  str
# 4   over              179078 non-null  int64
# 5   ball              179078 non-null  int64
# 6   batsman           179078 non-null  str
# 7   non_striker       179078 non-null  str
# 8   bowler            179078 non-null  str
# 9   is_super_over     179078 non-null  int64
# 10  wide_runs         179078 non-null  int64
# 11  bye_runs          179078 non-null  int64
# 12  legbye_runs       179078 non-null  int64
# 13  noball_runs       179078 non-null  int64
# 14  penalty_runs      179078 non-null  int64
# 15  batsman_runs      179078 non-null  int64
# 16  extra_runs        179078 non-null  int64
# 17  total_runs        179078 non-null  int64
# 18  player_dismissed  8834 non-null    str
# 19  dismissal_kind    8834 non-null    str
# 20  fielder           6448 non-null    str
# dtypes: int64(13), str(8)
# memory usage: 28.7 MB
# None









# =============================================================================
# pd.concat() : Interview Spoken Notes
# =============================================================================

# lll Definition:
#     pd.concat() is a Pandas function used to combine two or more DataFrames
#     or Series either vertically (row-wise) or horizontally (column-wise).

# In simple words:
# It is used to stack multiple datasets into one dataset.


# =============================================================================
# Syntax
# =============================================================================

# pd.concat(objs, axis=0, ignore_index=False, keys=None)

# lll It has parameter 
#                (Indicate)
#     objs           ->       List of DataFrames / Series
#     axis=0         ->       Vertical stacking (default) |   Way of stacking
#     axis=1         ->       Horizontal stacking         |
#     ignore_index   ->       Reset index after stacking
#     keys           ->       MultiIndex labels





# For pd.concat(), stacking happens in two ways:
#================================================


# lll Vertical Stacking (axis=0):
#     ----------------------------
#     Best condition: 
#              Columns should be same.
#              If columns are different, pandas adds new columns and fills missing values with NaN.

# lll Horizontal Stacking (axis=1):
#     -------------------------------
#     Best condition: 
#               Index should be same.
#               If indexes are different, pandas fills unmatched rows with NaN.

# Easy Rule:
# axis=0 → Match Columns
# axis=1 → Match Index






# Vertical Stacking (axis=0):
#----------------------------

print(pd.concat([nov, dec])) 

'''
    student_id  course_id
0           23          1
1           15          5
2           18          6
3           23          4
4           16          9
5           18          1
6            1          1
7            7          8
8           22          3
9           15          1
10          19          4
11           1          6
12           7         10
13          11          7
14          13          3
15          24          4
16          21          1
17          16          5
18          23          3
19          17          7
20          23          6
21          25          1
22          19          2
23          25         10
24           3          3
0            3          5
1           16          7
2           12         10
3           12          1
4           14          9
5            7          7
6            7          2
7           16          3
8           17         10
9           11          8
10          14          6
11          12          5
12          12          7
13          18          8
14           1         10
15           1          9
16           2          5
17           7          6
18          22          5
19          22          6
20          23          9
21          23          5
22          14          4
23          14          1
24          11         10
25          42          9
26          50          8
27          38          1

'''


print(pd.concat([nov, dec], ignore_index=True))

'''
    student_id  course_id
0           23          1
1           15          5
2           18          6
3           23          4
4           16          9
5           18          1
6            1          1
7            7          8
8           22          3
9           15          1
10          19          4
11           1          6
12           7         10
13          11          7
14          13          3
15          24          4
16          21          1
17          16          5
18          23          3
19          17          7
20          23          6
21          25          1
22          19          2
23          25         10
24           3          3
25           3          5
26          16          7
27          12         10
28          12          1
29          14          9
30           7          7
31           7          2
32          16          3
33          17         10
34          11          8
35          14          6
36          12          5
37          12          7
38          18          8
39           1         10
40           1          9
41           2          5
42           7          6
43          22          5
44          22          6
45          23          9
46          23          5
47          14          4
48          14          1
49          11         10
50          42          9
51          50          8
52          38          1

'''



# =============================================================================
# 3. MultiIndex using keys
# =============================================================================


print(pd.concat([nov, dec], keys=['Nov', 'Dec']))

'''

        student_id  course_id
Nov 0           23          1
    1           15          5
    2           18          6
    3           23          4
    4           16          9
    5           18          1
    6            1          1
    7            7          8
    8           22          3
    9           15          1
    10          19          4
    11           1          6
    12           7         10
    13          11          7
    14          13          3
    15          24          4
    16          21          1
    17          16          5
    18          23          3
    19          17          7
    20          23          6
    21          25          1
    22          19          2
    23          25         10
    24           3          3
Dec 0            3          5
    1           16          7
    2           12         10
    3           12          1
    4           14          9
    5            7          7
    6            7          2
    7           16          3
    8           17         10
    9           11          8
    10          14          6
    11          12          5
    12          12          7
    13          18          8
    14           1         10
    15           1          9
    16           2          5
    17           7          6
    18          22          5
    19          22          6
    20          23          9
    21          23          5
    22          14          4
    23          14          1
    24          11         10
    25          42          9
    26          50          8
    27          38          1

'''

# =============================================================================
# Access MultiIndex Data
# =============================================================================

print(pd.concat([nov, dec], keys=['Nov', 'Dec']).loc['Nov'])

'''
    student_id  course_id
0           23          1
1           15          5
2           18          6
3           23          4
4           16          9
5           18          1
6            1          1
7            7          8
8           22          3
9           15          1
10          19          4
11           1          6
12           7         10
13          11          7
14          13          3
15          24          4
16          21          1
17          16          5
18          23          3
19          17          7
20          23          6
21          25          1
22          19          2
23          25         10
24           3          3

'''


print(pd.concat([nov, dec], keys=['Nov', 'Dec']).loc[('Nov', 5)])

'''
student_id    18
course_id      1
Name: (Nov, 5), dtype: int64
'''



print(pd.concat([nov, dec], keys=['Nov', 'Dec']).loc[('Dec', 7)])

'''
student_id    16
course_id      3
Name: (Dec, 7), dtype: int64
'''







# Horizontal Stacking (axis=1):
#-------------------------------

print(pd.concat([nov, dec], axis=1))

'''
    student_id  course_id  student_id  course_id
0         23.0        1.0           3          5
1         15.0        5.0          16          7
2         18.0        6.0          12         10
3         23.0        4.0          12          1
4         16.0        9.0          14          9
5         18.0        1.0           7          7
6          1.0        1.0           7          2
7          7.0        8.0          16          3
8         22.0        3.0          17         10
9         15.0        1.0          11          8
10        19.0        4.0          14          6
11         1.0        6.0          12          5
12         7.0       10.0          12          7
13        11.0        7.0          18          8
14        13.0        3.0           1         10
15        24.0        4.0           1          9
16        21.0        1.0           2          5
17        16.0        5.0           7          6
18        23.0        3.0          22          5
19        17.0        7.0          22          6
20        23.0        6.0          23          9
21        25.0        1.0          23          5
22        19.0        2.0          14          4
23        25.0       10.0          14          1
24         3.0        3.0          11         10
25         NaN        NaN          42          9
26         NaN        NaN          50          8
27         NaN        NaN          38          1





# =============================================================================
# concat() vs merge()
# =============================================================================

# concat():
# Used for stacking DataFrames

# merge():
# Used for joining DataFrames using common column like SQL Join


# =============================================================================
# Interview Spoken Difference
# =============================================================================

# Use concat() when appending datasets.
# Use merge() when joining related tables using key columns.



'''



