


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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


reg = pd.concat([nov, dec], ignore_index=True)


# np.intersect1d()
#------------------

# gpt give perfect interview spoken diffinition

print(np.intersect1d(nov['student_id'], dec['student_id']))

# [ 1  3  7 11 16 17 18 22 23]



# np.intersect1d()
#------------------

# gpt give perfect interview spoken diffinition

# difference between  :- courses['course_id'] - reg['course_id']

print(np.setdiff1d(courses['course_id'], reg['course_id']))

# [11 12]





#============================================ Questions =================================================



# Ques : Find total revenue generated by compny
#-----------------------------------------------


print(courses.merge(reg, how='inner', on='course_id')['price'].sum())
# 154247



# Ques : Find total revenue of each course
#------------------------------------------

print(courses.merge(reg, how='inner', on='course_id').groupby(['course_id', 'course_name'])['price'].sum())

'''
course_id  course_name
1          python              22491
2          sql                  6998
3          data analysis       24995
4          machine learning    39996
5          tableau             17493
6          power bi            11394
7          ms sxcel             7995
8          pandas               4396
9          plotly               3495
10         pyspark             14994
Name: price, dtype: int64
'''



# Ques : Find month by month revenue
#------------------------------------

reg1 = pd.concat([nov, dec], keys=['Nov', 'Dec']).reset_index()
print(reg1)
'''
 level_0  level_1  student_id  course_id
0      Nov        0          23          1
1      Nov        1          15          5
2      Nov        2          18          6
3      Nov        3          23          4
4      Nov        4          16          9
5      Nov        5          18          1
6      Nov        6           1          1
7      Nov        7           7          8
8      Nov        8          22          3
9      Nov        9          15          1
10     Nov       10          19          4
11     Nov       11           1          6
12     Nov       12           7         10
13     Nov       13          11          7
14     Nov       14          13          3
15     Nov       15          24          4
16     Nov       16          21          1
17     Nov       17          16          5
18     Nov       18          23          3
19     Nov       19          17          7
20     Nov       20          23          6
21     Nov       21          25          1
22     Nov       22          19          2
23     Nov       23          25         10
24     Nov       24           3          3
25     Dec        0           3          5
26     Dec        1          16          7
27     Dec        2          12         10
28     Dec        3          12          1
29     Dec        4          14          9
30     Dec        5           7          7
31     Dec        6           7          2
32     Dec        7          16          3
33     Dec        8          17         10
34     Dec        9          11          8
35     Dec       10          14          6
36     Dec       11          12          5
37     Dec       12          12          7
38     Dec       13          18          8
39     Dec       14           1         10
40     Dec       15           1          9
41     Dec       16           2          5
42     Dec       17           7          6
43     Dec       18          22          5
44     Dec       19          22          6
45     Dec       20          23          9
46     Dec       21          23          5
47     Dec       22          14          4
48     Dec       23          14          1
49     Dec       24          11         10
50     Dec       25          42          9
51     Dec       26          50          8
52     Dec       27          38          1
'''


print(courses.merge(reg1, how='inner', on='course_id').groupby('level_0')['price'].sum())
'''
level_0
Dec    65072
Nov    89175
Name: price, dtype: int64
'''





# Ques : Print the registration table (cols -> name -> course -> price)
#-------------------------------------

print(students.merge(reg, how='inner', on='student_id').merge(courses, how='inner', on='course_id')[['name', 'course_name', 'price']])
'''
                  name       course_name  price
0        Kailash Harjo            python   2499
1        Kailash Harjo          power bi   1899
2        Kailash Harjo           pyspark   2499
3        Kailash Harjo            plotly    699
4          Esha Butala           tableau   2499
5       Parveen Bhalla     data analysis   4999
6       Parveen Bhalla           tableau   2499
7         Tarun Thaker            pandas   1099
8         Tarun Thaker           pyspark   2499
9         Tarun Thaker          ms sxcel   1599
10        Tarun Thaker               sql   3499
11        Tarun Thaker          power bi   1899
12  David Mukhopadhyay          ms sxcel   1599
13  David Mukhopadhyay            pandas   1099
14  David Mukhopadhyay           pyspark   2499
15          Radha Dutt           pyspark   2499
16          Radha Dutt            python   2499
17          Radha Dutt           tableau   2499
18          Radha Dutt          ms sxcel   1599
19      Munni Varghese     data analysis   4999
20    Pranab Natarajan            plotly    699
21    Pranab Natarajan          power bi   1899
22    Pranab Natarajan  machine learning   9999
23    Pranab Natarajan            python   2499
24           Preet Sha           tableau   2499
25           Preet Sha            python   2499
26        Elias Dodiya            plotly    699
27        Elias Dodiya           tableau   2499
28        Elias Dodiya          ms sxcel   1599
29        Elias Dodiya     data analysis   4999
30        Yasmin Palan          ms sxcel   1599
31        Yasmin Palan           pyspark   2499
32     Fardeen Mahabir          power bi   1899
33     Fardeen Mahabir            python   2499
34     Fardeen Mahabir            pandas   1099
35        Qabeel Raman  machine learning   9999
36        Qabeel Raman               sql   3499
37          Seema Kota            python   2499
38          Yash Sethi     data analysis   4999
39          Yash Sethi           tableau   2499
40          Yash Sethi          power bi   1899
41      Chhavi Lachman            python   2499
42      Chhavi Lachman  machine learning   9999
43      Chhavi Lachman     data analysis   4999
44      Chhavi Lachman          power bi   1899
45      Chhavi Lachman            plotly    699
46      Chhavi Lachman           tableau   2499
47        Radhika Suri  machine learning   9999
48     Shashank D’Alia            python   2499
49     Shashank D’Alia           pyspark   2499
'''



# Ques : Plot bar char for revenue/course
#----------------------------------------

print(courses.merge(reg, how='inner', on='course_id').groupby('course_name')['price'].sum())
courses.merge(reg, how='inner', on='course_id').groupby('course_name')['price'].sum().plot(kind='bar')
plt.show()





# Ques : Find students who enrolled in both the months
#------------------------------------------------------

common_student_enroll_both_month = np.intersect1d(nov['student_id'], dec['student_id'])
    
print(students[students['student_id'].isin(common_student_enroll_both_month)])
'''
    student_id                name  partner
0            1       Kailash Harjo       23
2            3      Parveen Bhalla        3
6            7        Tarun Thaker        9
10          11  David Mukhopadhyay       20
15          16        Elias Dodiya       25
16          17        Yasmin Palan        7
17          18     Fardeen Mahabir       13
21          22          Yash Sethi       21
22          23      Chhavi Lachman       18
'''




# Ques : Find course that got no enrollment
#-------------------------------------------

print(np.intersect1d(courses['course_id'], reg['course_id']))

print(courses[~(courses['course_id'].isin(np.intersect1d(courses['course_id'], reg['course_id'])))])
'''
    course_id course_name  price
10         11       Numpy    699
11         12         C++   1299
'''



# Ques : Find student who did not enroll into any courses
#---------------------------------------------------------

student_enroll = courses.merge(reg, how='inner', on='course_id')['student_id']

print(students[~(students['student_id'].isin(student_enroll))])

'''
    student_id                name  partner
3            4         Marlo Dugal       14
4            5         Kusum Bahri        6
5            6  Lakshmi Contractor       10
7            8      Radheshyam Dey        5
8            9   Nitika Chatterjee        4
9           10      Aayushman Sant        8
19          20       Hanuman Hegde       11
'''





# self join
#------------

# gpt give perfect interview spoken diffinition


# Ques : Print student name -> partner name for all enrolled students
#---------------------------------------------------------------------

print(students.merge(students, how='inner', left_on='student_id', right_on='partner')[['name_x', 'name_y']])

'''
                name_x              name_y
0        Kailash Harjo         Esha Butala
1          Esha Butala     Shashank D’Alia
2       Parveen Bhalla      Parveen Bhalla
3          Marlo Dugal   Nitika Chatterjee
4          Kusum Bahri      Radheshyam Dey
5   Lakshmi Contractor         Kusum Bahri
6         Tarun Thaker        Yasmin Palan
7       Radheshyam Dey      Aayushman Sant
8    Nitika Chatterjee        Tarun Thaker
9       Aayushman Sant  Lakshmi Contractor
10  David Mukhopadhyay       Hanuman Hegde
11          Radha Dutt        Qabeel Raman
12      Munni Varghese     Fardeen Mahabir
13    Pranab Natarajan         Marlo Dugal
14           Preet Sha          Seema Kota
15        Elias Dodiya           Preet Sha
16        Yasmin Palan        Radhika Suri
17     Fardeen Mahabir      Chhavi Lachman
18        Qabeel Raman          Radha Dutt
19       Hanuman Hegde  David Mukhopadhyay
20          Seema Kota          Yash Sethi
21          Yash Sethi    Pranab Natarajan
22      Chhavi Lachman       Kailash Harjo
23        Radhika Suri      Munni Varghese
24     Shashank D’Alia        Elias Dodiya
'''




# Ques : Find top 3 students who did most number enrollments
#------------------------------------------------------------


print(courses.merge(reg, how='inner', on='course_id').groupby('student_id')['course_name'].count().sort_values(ascending=False).head(3))
'''
23    6
7     5
1     4
Name: course_name, dtype: int64
'''
print(reg.merge(students, how='inner', on='student_id').groupby(['student_id', 'name'])['name'].count().sort_values(ascending=False).head(3))

'''
student_id  name
23          Chhavi Lachman      6
7           Tarun Thaker        5
14          Pranab Natarajan    4
Name: name, dtype: int64
'''




# Find top 3 students who spent most amount of money on courses
#---------------------------------------------------------------



print(students.merge(reg, how='inner', on='student_id').merge(courses, how='inner', on='course_id').groupby(['student_id', 'name'])['price'].sum().sort_values(ascending=False).head(3))
'''
student_id  name
23          Chhavi Lachman      22594
14          Pranab Natarajan    15096
19          Qabeel Raman        13498
Name: price, dtype: int64
'''







# IPL Problems
#--------------

# Ques : Find top 3 students with highest sixes/match ratio
#------------------------------------------------------------

temp_df = delivery.merge(matches, how='inner', left_on='match_id', right_on='id')
six_df = temp_df[temp_df['batsman_runs'] == 6]
num_six = six_df.groupby('venue')['venue'].count()
num_matches = matches['venue'].value_counts()

print((num_six/num_matches).sort_values(ascending=False).head(3))
'''
venue
Holkar Cricket Stadium     17.600000
M Chinnaswamy Stadium      13.227273
Sharjah Cricket Stadium    12.666667
dtype: float64
'''



# Ques: Find orange cap holder of all the seasons
#-------------------------------------------------


