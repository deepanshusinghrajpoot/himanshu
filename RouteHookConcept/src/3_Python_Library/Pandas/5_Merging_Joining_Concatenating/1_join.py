


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
# Pandas merge() / join() - Interview Spoken Notes
# =============================================================================

# lll Definition:
#     merge() is a pandas function used to combine two DataFrames
#     based on one or more common columns, similar to SQL JOIN.

# In simple words:
# It is used to connect related tables using key columns.


# =============================================================================
# Syntax
# =============================================================================

# pd.merge(left_df, right_df, how='inner', on='column_name')

# OR

# left_df.merge(right_df, how='inner', on='column_name')


# It has Parameters:
#          (Indicate)
# how         ->         type of join
# on          ->         common column name
# left_on     ->         left table join column
# right_on    ->         right table join column
# suffixes (handle duplicate column names)


reg = pd.concat([nov, dec], ignore_index=True)




# =============================================================================
# 1. Inner Join
# =============================================================================


print(students.merge(reg, how='inner', on='student_id'))

'''
    student_id                name  partner  course_id
0            1       Kailash Harjo       23          1
1            1       Kailash Harjo       23          6
2            1       Kailash Harjo       23         10
3            1       Kailash Harjo       23          9
4            2         Esha Butala        1          5
5            3      Parveen Bhalla        3          3
6            3      Parveen Bhalla        3          5
7            7        Tarun Thaker        9          8
8            7        Tarun Thaker        9         10
9            7        Tarun Thaker        9          7
10           7        Tarun Thaker        9          2
11           7        Tarun Thaker        9          6
12          11  David Mukhopadhyay       20          7
13          11  David Mukhopadhyay       20          8
14          11  David Mukhopadhyay       20         10
15          12          Radha Dutt       19         10
16          12          Radha Dutt       19          1
17          12          Radha Dutt       19          5
18          12          Radha Dutt       19          7
19          13      Munni Varghese       24          3
20          14    Pranab Natarajan       22          9
21          14    Pranab Natarajan       22          6
22          14    Pranab Natarajan       22          4
23          14    Pranab Natarajan       22          1
24          15           Preet Sha       16          5
25          15           Preet Sha       16          1
26          16        Elias Dodiya       25          9
27          16        Elias Dodiya       25          5
28          16        Elias Dodiya       25          7
'''




# =============================================================================
# 2. Left Join
# =============================================================================


print(courses.merge(reg, how='left', on='course_id'))

'''
    course_id       course_name  price  student_id
0           1            python   2499        23.0
1           1            python   2499        18.0
2           1            python   2499         1.0
3           1            python   2499        15.0
4           1            python   2499        21.0
5           1            python   2499        25.0
6           1            python   2499        12.0
7           1            python   2499        14.0
8           1            python   2499        38.0
9           2               sql   3499        19.0
10          2               sql   3499         7.0
11          3     data analysis   4999        22.0
12          3     data analysis   4999        13.0
13          3     data analysis   4999        23.0
14          3     data analysis   4999         3.0
15          3     data analysis   4999        16.0
16          4  machine learning   9999        23.0
17          4  machine learning   9999        19.0
18          4  machine learning   9999        24.0
19          4  machine learning   9999        14.0
20          5           tableau   2499        15.0
21          5           tableau   2499        16.0
22          5           tableau   2499         3.0
23          5           tableau   2499        12.0
24          5           tableau   2499         2.0
25          5           tableau   2499        22.0
26          5           tableau   2499        23.0
27          6          power bi   1899        18.0
28          6          power bi   1899         1.0
29          6          power bi   1899        23.0
30          6          power bi   1899        14.0
31          6          power bi   1899         7.0
32          6          power bi   1899        22.0
33          7          ms sxcel   1599        11.0
34          7          ms sxcel   1599        17.0
35          7          ms sxcel   1599        16.0
36          7          ms sxcel   1599         7.0
37          7          ms sxcel   1599        12.0
38          8            pandas   1099         7.0
39          8            pandas   1099        11.0
40          8            pandas   1099        18.0
41          8            pandas   1099        50.0
42          9            plotly    699        16.0
43          9            plotly    699        14.0
44          9            plotly    699         1.0
45          9            plotly    699        23.0
46          9            plotly    699        42.0
47         10           pyspark   2499         7.0
48         10           pyspark   2499        25.0
49         10           pyspark   2499        12.0
50         10           pyspark   2499        17.0
51         10           pyspark   2499         1.0
52         10           pyspark   2499        11.0
53         11             Numpy    699         NaN
54         12               C++   1299         NaN
'''



# =============================================================================
# 3. Right Join
# =============================================================================


temp_df = pd.DataFrame({
    'student_id':[26, 27, 28],
    'name':['Nitish', 'Ankit', 'Rahul'],
    'partner':[28, 26, 17]
})

students = pd.concat([students, temp_df], ignore_index=True)

print(students.merge(reg, how='right', on='student_id'))

'''
    student_id                name  partner  course_id
0           23      Chhavi Lachman     18.0          1
1           15           Preet Sha     16.0          5
2           18     Fardeen Mahabir     13.0          6
3           23      Chhavi Lachman     18.0          4
4           16        Elias Dodiya     25.0          9
5           18     Fardeen Mahabir     13.0          1
6            1       Kailash Harjo     23.0          1
7            7        Tarun Thaker      9.0          8
8           22          Yash Sethi     21.0          3
9           15           Preet Sha     16.0          1
10          19        Qabeel Raman     12.0          4
11           1       Kailash Harjo     23.0          6
12           7        Tarun Thaker      9.0         10
13          11  David Mukhopadhyay     20.0          7
14          13      Munni Varghese     24.0          3
15          24        Radhika Suri     17.0          4
16          21          Seema Kota     15.0          1
17          16        Elias Dodiya     25.0          5
18          23      Chhavi Lachman     18.0          3
19          17        Yasmin Palan      7.0          7
20          23      Chhavi Lachman     18.0          6
21          25     Shashank D’Alia      2.0          1
22          19        Qabeel Raman     12.0          2
23          25     Shashank D’Alia      2.0         10
24           3      Parveen Bhalla      3.0          3
25           3      Parveen Bhalla      3.0          5
26          16        Elias Dodiya     25.0          7
27          12          Radha Dutt     19.0         10
28          12          Radha Dutt     19.0          1
29          14    Pranab Natarajan     22.0          9
30           7        Tarun Thaker      9.0          7
31           7        Tarun Thaker      9.0          2
32          16        Elias Dodiya     25.0          3
33          17        Yasmin Palan      7.0         10
34          11  David Mukhopadhyay     20.0          8
35          14    Pranab Natarajan     22.0          6
36          12          Radha Dutt     19.0          5
37          12          Radha Dutt     19.0          7
38          18     Fardeen Mahabir     13.0          8
39           1       Kailash Harjo     23.0         10
40           1       Kailash Harjo     23.0          9
41           2         Esha Butala      1.0          5
42           7        Tarun Thaker      9.0          6
43          22          Yash Sethi     21.0          5
44          22          Yash Sethi     21.0          6
45          23      Chhavi Lachman     18.0          9
46          23      Chhavi Lachman     18.0          5
47          14    Pranab Natarajan     22.0          4
48          14    Pranab Natarajan     22.0          1
49          11  David Mukhopadhyay     20.0         10
50          42                 NaN      NaN          9
51          50                 NaN      NaN          8
52          38                 NaN      NaN          1
'''



# =============================================================================
# 4. Outer Join
# =============================================================================


print(students.merge(reg, how='outer', on='student_id').tail(10))

'''
    student_id             name  partner  course_id
53          23   Chhavi Lachman     18.0        5.0
54          24     Radhika Suri     17.0        4.0
55          25  Shashank D’Alia      2.0        1.0
56          25  Shashank D’Alia      2.0       10.0
57          26           Nitish     28.0        NaN
58          27            Ankit     26.0        NaN
59          28            Rahul     17.0        NaN
60          38              NaN      NaN        1.0
61          42              NaN      NaN        9.0
62          50              NaN      NaN        8.0
'''




# =============================================================================
# 5. Self Join
# =============================================================================

print(students.merge(students, how='inner', left_on='partner', right_on='student_id')[['name_x', 'name_y']])

'''
                name_x              name_y
0        Kailash Harjo      Chhavi Lachman
1          Esha Butala       Kailash Harjo
2       Parveen Bhalla      Parveen Bhalla
3          Marlo Dugal    Pranab Natarajan
4          Kusum Bahri  Lakshmi Contractor
5   Lakshmi Contractor      Aayushman Sant
6         Tarun Thaker   Nitika Chatterjee
7       Radheshyam Dey         Kusum Bahri
8    Nitika Chatterjee         Marlo Dugal
9       Aayushman Sant      Radheshyam Dey
10  David Mukhopadhyay       Hanuman Hegde
11          Radha Dutt        Qabeel Raman
12      Munni Varghese        Radhika Suri
13    Pranab Natarajan          Yash Sethi
14           Preet Sha        Elias Dodiya
15        Elias Dodiya     Shashank D’Alia
16        Yasmin Palan        Tarun Thaker
17     Fardeen Mahabir      Munni Varghese
18        Qabeel Raman          Radha Dutt
19       Hanuman Hegde  David Mukhopadhyay
20          Seema Kota           Preet Sha
21          Yash Sethi          Seema Kota
22      Chhavi Lachman     Fardeen Mahabir
23        Radhika Suri        Yasmin Palan
24     Shashank D’Alia         Esha Butala
25              Nitish               Rahul
26               Ankit              Nitish
27               Rahul        Yasmin Palan
'''





# Alternative way to apply join
#------------------------------

print(pd.merge(students, reg, how='inner', on='student_id'))

'''
    student_id                name  partner  course_id
0            1       Kailash Harjo       23          1
1            1       Kailash Harjo       23          6
2            1       Kailash Harjo       23         10
3            1       Kailash Harjo       23          9
4            2         Esha Butala        1          5
5            3      Parveen Bhalla        3          3
6            3      Parveen Bhalla        3          5
7            7        Tarun Thaker        9          8
8            7        Tarun Thaker        9         10
9            7        Tarun Thaker        9          7
10           7        Tarun Thaker        9          2
11           7        Tarun Thaker        9          6
12          11  David Mukhopadhyay       20          7
13          11  David Mukhopadhyay       20          8
14          11  David Mukhopadhyay       20         10
15          12          Radha Dutt       19         10
16          12          Radha Dutt       19          1
17          12          Radha Dutt       19          5
18          12          Radha Dutt       19          7
19          13      Munni Varghese       24          3
20          14    Pranab Natarajan       22          9
21          14    Pranab Natarajan       22          6
22          14    Pranab Natarajan       22          4
23          14    Pranab Natarajan       22          1
24          15           Preet Sha       16          5
25          15           Preet Sha       16          1
26          16        Elias Dodiya       25          9
27          16        Elias Dodiya       25          5
28          16        Elias Dodiya       25          7
29          16        Elias Dodiya       25          3
30          17        Yasmin Palan        7          7
31          17        Yasmin Palan        7         10
32          18     Fardeen Mahabir       13          6
33          18     Fardeen Mahabir       13          1
34          18     Fardeen Mahabir       13          8
35          19        Qabeel Raman       12          4
36          19        Qabeel Raman       12          2
37          21          Seema Kota       15          1
38          22          Yash Sethi       21          3
39          22          Yash Sethi       21          5
40          22          Yash Sethi       21          6
41          23      Chhavi Lachman       18          1
42          23      Chhavi Lachman       18          4
43          23      Chhavi Lachman       18          3
44          23      Chhavi Lachman       18          6
45          23      Chhavi Lachman       18          9
46          23      Chhavi Lachman       18          5
47          24        Radhika Suri       17          4
48          25     Shashank D’Alia        2          1
49          25     Shashank D’Alia        2         10














# =============================================================================
# left_on and right_on
# =============================================================================

df1.merge(df2, left_on='emp_id', right_on='id')

# Used when column names are different
# in both DataFrames.


# =============================================================================
# suffixes Parameter
# =============================================================================

df1.merge(df2, on='id', suffixes=('_left', '_right'))

# Used when same column names exist
# in both DataFrames.


# =============================================================================
# merge() vs concat()
# =============================================================================

# merge():
# Combines using common key column.

# concat():
# Combines by stacking rows or columns.

# lll Interview Spoken:
#     merge pandas function use when relationship exists.
#     concat pandas function use when we want to stack datasets.


# =============================================================================
# SQL Join Mapping
# =============================================================================

# SQL INNER JOIN  = how='inner'
# SQL LEFT JOIN   = how='left'
# SQL RIGHT JOIN  = how='right'
# SQL FULL OUTER  = how='outer'


# =============================================================================
# Real Time Examples
# =============================================================================

# Customers table + Orders table
# Employees table + Department table
# Students table + Courses table


# =============================================================================
# Common Interview Questions
# =============================================================================

# Q1. Default join type in pandas merge()?
# Answer: inner

# Q2. Difference between left and right join?
# Answer:
# Left keeps left table all rows.
# Right keeps right table all rows.

# Q3. Why NaN appears after merge?
# Answer:
# Because matching record not found.

# Q4. Can we join on different column names?
# Answer:
# Yes, using left_on and right_on.

# Q5. What is self join?
# Answer:
# Joining same table with itself.


# =============================================================================
# Best Spoken 1 Minute Answer
# =============================================================================

# merge() in pandas is used to combine two DataFrames
# based on common columns, similar to SQL joins.
# We can perform inner, left, right, outer, and self joins.
# It is mainly used to combine relational datasets.


# =============================================================================
# One-Line Best Answer
# =============================================================================

# merge() joins DataFrames using key columns,
# just like SQL JOIN operations.




'''








