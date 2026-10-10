


import pandas as pd


import os



# 2. Opening a local csv file
#-----------------------------

path = os.path.dirname(__file__)
path_file_1 = os.path.join(path, '../../../../../Pandas/1_Dataset/batter.csv')

batter = pd.read_csv(path_file_1)

print(batter)
'''
             batter  runs        avg  strike_rate
0           V Kohli  6634  36.251366   125.977972
1          S Dhawan  6244  34.882682   122.840842
2         DA Warner  5883  41.429577   136.401577
3         RG Sharma  5881  30.314433   126.964594
4          SK Raina  5536  32.374269   132.535312
..              ...   ...        ...          ...
600         C Nanda     0   0.000000     0.000000
601      Akash Deep     0   0.000000     0.000000
602         S Ladda     0   0.000000     0.000000
603  V Pratap Singh     0   0.000000     0.000000
604    S Lamichhane     0   0.000000     0.000000

[605 rows x 4 columns]
'''




# 3. Opening a csv file from an URL
#-----------------------------------

'''

🔹 What requests does
-----------------------

requests module in python is used to

Get data from a website (HTTP GET)
Send data to a website (HTTP POST)
Handle headers, cookies, authentication
Work with APIs (JSON, XML, etc.) easily
Handle errors and timeouts gracefully


'''

"""
Title: Load CSV Data from a URL into Pandas DataFrame
Author: [Your Name]
Date: [YYYY-MM-DD]
Description: This script fetches a CSV file from a given URL over HTTP
             using the Requests library, converts it into a Pandas DataFrame,
             and displays the first 5 rows.
"""

# ===============================
# 1. Import Required Libraries
# ===============================
import requests
import pandas as pd
from io import StringIO

# ===============================
# 2. Define CSV URL and Headers
# ===============================
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# ===============================
# 3. Send HTTP GET Request
# ===============================
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error fetching the CSV file:", e)
    exit()

# ===============================
# 4. Convert CSV Text to File-Like Object
# ===============================
csv_data = StringIO(response.text)

# ===============================
# 5. Read CSV into Pandas DataFrame
# ===============================
df = pd.read_csv(csv_data)

# ===============================
# 6. Inspect the DataFrame
# ===============================

print(df.head())
'''
  sepal_length  sepal_width  petal_length  petal_width species
0           5.1          3.5           1.4          0.2  setosa      
1           4.9          3.0           1.4          0.2  setosa      
2           4.7          3.2           1.3          0.2  setosa      
3           4.6          3.1           1.5          0.2  setosa      
4           5.0          3.6           1.4          0.2  setosa      
'''

print(df.info())
'''
<class 'pandas.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   sepal_length  150 non-null    float64
 1   sepal_width   150 non-null    float64
 2   petal_length  150 non-null    float64
 3   petal_width   150 non-null    float64
 4   species       150 non-null    str
dtypes: float64(4), str(1)
memory usage: 6.0 KB
None 
'''







# 4. sep parameter
#------------------

path_file_2 = os.path.join(path, '../../../../../Pandas/1_Dataset/employee.tsv')

data = pd.read_csv(path_file_2)
print(data)
'''
         1\tName_1\t49\tFinance\t111560
0       2\tName_2\t28\tMarketing\t55124
1              3\tName_3\t31\tIT\t72036
2         4\tName_4\t53\tFinance\t92290
3             5\tName_5\t41\tIT\t108451
4         6\tName_6\t34\tFinance\t76990
..                                  ...
94     96\tName_96\t24\tFinance\t106245
95     97\tName_97\t55\tFinance\t102065
96     98\tName_98\t40\tFinance\t114315
97      99\tName_99\t36\tFinance\t67909
98  100\tName_100\t22\tMarketing\t80681

[99 rows x 1 columns]
'''


data = pd.read_csv(path_file_2, sep='\t')
print(data)
'''
      1    Name_1  49    Finance  111560
0     2    Name_2  28  Marketing   55124
1     3    Name_3  31         IT   72036
2     4    Name_4  53    Finance   92290
3     5    Name_5  41         IT  108451
4     6    Name_6  34    Finance   76990
..  ...       ...  ..        ...     ...
94   96   Name_96  24    Finance  106245
95   97   Name_97  55    Finance  102065
96   98   Name_98  40    Finance  114315
97   99   Name_99  36    Finance   67909
98  100  Name_100  22  Marketing   80681

[99 rows x 5 columns]
'''

# name
#......
data = pd.read_csv(path_file_2, sep='\t', names=['ID', 'name', 'department', 'salary'])
print(data)
'''
           ID  name department  salary
1      Name_1    49    Finance  111560
2      Name_2    28  Marketing   55124
3      Name_3    31         IT   72036
4      Name_4    53    Finance   92290
5      Name_5    41         IT  108451
..        ...   ...        ...     ...
96    Name_96    24    Finance  106245
97    Name_97    55    Finance  102065
98    Name_98    40    Finance  114315
99    Name_99    36    Finance   67909
100  Name_100    22  Marketing   80681

[100 rows x 4 columns]
'''




# 5. index_col parameter
#-----------------------

data = pd.read_csv(path_file_1, index_col='batter')
print(data)
'''
                runs        avg  strike_rate
batter
V Kohli         6634  36.251366   125.977972
S Dhawan        6244  34.882682   122.840842
DA Warner       5883  41.429577   136.401577
RG Sharma       5881  30.314433   126.964594
SK Raina        5536  32.374269   132.535312
...              ...        ...          ...
C Nanda            0   0.000000     0.000000
Akash Deep         0   0.000000     0.000000
S Ladda            0   0.000000     0.000000
V Pratap Singh     0   0.000000     0.000000
S Lamichhane       0   0.000000     0.000000

[605 rows x 3 columns]
'''



# 6. Header parameter
#---------------------

path_file_test = os.path.join(path, '../../../../../Pandas/1_Dataset/test.csv')

test = pd.read_csv(path_file_test)
print(test)
'''
     0     Name  Age Department  Salary
0    1   Name_1   49    Finance  111560
1    2   Name_2   28  Marketing   55124
2    3   Name_3   31         IT   72036
3    4   Name_4   53    Finance   92290
4    5   Name_5   41         IT  108451
5    6   Name_6   34    Finance   76990
6    7   Name_7   27    Finance  104190
7    8   Name_8   37  Marketing   67603
8    9   Name_9   22    Finance  102101
9   10  Name_10   58    Finance   78484
10  11  Name_11   44    Finance   31972
11  12  Name_12   40    Finance   97441
12  13  Name_13   49  Marketing   39147
13  14  Name_14   31    Finance   57952
14  15  Name_15   22    Finance  105089
15  16  Name_16   55    Finance   82603
16  17  Name_17   28    Finance   73417
17  18  Name_18   52  Marketing  108278
18  19  Name_19   34    Finance   97003
19  20  Name_20   42    Finance   44241
'''

test = pd.read_csv(path_file_test, header=1)
print(test)
'''
     1   Name_1  49    Finance  111560
0    2   Name_2  28  Marketing   55124
1    3   Name_3  31         IT   72036
2    4   Name_4  53    Finance   92290
3    5   Name_5  41         IT  108451
4    6   Name_6  34    Finance   76990
5    7   Name_7  27    Finance  104190
6    8   Name_8  37  Marketing   67603
7    9   Name_9  22    Finance  102101
8   10  Name_10  58    Finance   78484
9   11  Name_11  44    Finance   31972
10  12  Name_12  40    Finance   97441
11  13  Name_13  49  Marketing   39147
12  14  Name_14  31    Finance   57952
13  15  Name_15  22    Finance  105089
14  16  Name_16  55    Finance   82603
15  17  Name_17  28    Finance   73417
16  18  Name_18  52  Marketing  108278
17  19  Name_19  34    Finance   97003
18  20  Name_20  42    Finance   44241
'''




# 7. use_cols parameter
#-----------------------

data_7 = pd.read_csv(path_file_1, usecols=['batter','runs'])
print(data_7)
'''
             batter  runs
0           V Kohli  6634
1          S Dhawan  6244
2         DA Warner  5883
3         RG Sharma  5881
4          SK Raina  5536
..              ...   ...
600         C Nanda     0
601      Akash Deep     0
602         S Ladda     0
603  V Pratap Singh     0
604    S Lamichhane     0

[605 rows x 2 columns]
'''


# 8. squeeze parameters
#-----------------------

data_8 = pd.read_csv(path_file_1, usecols=['batter'])
print(type(data_8))
'''
<class 'pandas.DataFrame'>
'''


data_8 = pd.read_csv(path_file_1, usecols=['batter']).squeeze('columns')
print(type(data_8))
'''
<class 'pandas.Series'>
'''





# 9. skiprows/nrows parameter
#-----------------------------

data_9 = pd.read_csv(path_file_1)
print(data_9.head())
'''
      batter  runs        avg  strike_rate
0    V Kohli  6634  36.251366   125.977972
1   S Dhawan  6244  34.882682   122.840842
2  DA Warner  5883  41.429577   136.401577
3  RG Sharma  5881  30.314433   126.964594
4   SK Raina  5536  32.374269   132.535312
'''

data_9 = pd.read_csv(path_file_1, skiprows=[1, 3, 4, 5, 6, 7, 8, 9, 10])
print(data_9.head())
'''
      batter  runs        avg  strike_rate
0   S Dhawan  6244  34.882682   122.840842
1  G Gambhir  4217  31.007353   119.665153
2  AT Rayudu  4190  28.896552   124.148148
3  AM Rahane  4074  30.863636   117.575758
4   KL Rahul  3895  46.927711   132.799182
'''


# nrows
#.......

print(pd.read_csv(path_file_1, nrows=3))
'''
      batter  runs        avg  strike_rate
0    V Kohli  6634  36.251366   125.977972
1   S Dhawan  6244  34.882682   122.840842
2  DA Warner  5883  41.429577   136.401577
'''




# 10. Encoding parameter
#------------------------
# when give error encoding

data_10 = pd.read_csv(path_file_1, encoding='UTF-8')
print(data_10.head())
'''
      batter  runs        avg  strike_rate
0    V Kohli  6634  36.251366   125.977972
1   S Dhawan  6244  34.882682   122.840842
2  DA Warner  5883  41.429577   136.401577
3  RG Sharma  5881  30.314433   126.964594
4   SK Raina  5536  32.374269   132.535312
'''



# 11. skip bad lines
#....................
# when give error pandas.errors.ParserError:

path_file_bad = os.path.join(path, '../../../../../Pandas/1_Dataset/bad.csv')

data_11 = pd.read_csv(path_file_bad, on_bad_lines='skip')
print(data_11)
'''
     ID   Name     Age Department Salary
0   1.0  Alice      25         HR  50000
1   2.0    Bob  thirty         IT  60000
2   3.0    NaN      22    Finance    abc
3   4.0  David      40        NaN  75000
4   NaN    Eve      35  Marketing  80000
5   6.0  Frank     NaN         HR    NaN
6  10.0   Jack      29  Marketing    ???
'''

'''

on_bad_lines accepts three options:

| Option    | Behavior                                   |
| --------- | ------------------------------------------ |
| `'error'` | Default. Raise `ParserError` for bad lines |
| `'skip'`  | Skip bad lines silently                    |
| `'warn'`  | Skip bad lines but print a warning         |

'''




# 13. Handling Dates
#--------------------

path_file_expense_data = os.path.join(path, '../../../../../Pandas/1_Dataset/expense_data.csv')
data_13 = pd.read_csv(path_file_expense_data)

print(data_13.info())
'''
<class 'pandas.DataFrame'>
RangeIndex: 277 entries, 0 to 276
Data columns (total 11 columns):
 #   Column          Non-Null Count  Dtype
---  ------          --------------  -----
 0   Date            277 non-null    str
 1   Account         277 non-null    str
 2   Category        277 non-null    str
 3   Subcategory     0 non-null      float64
 4   Note            273 non-null    str
 5   INR             277 non-null    float64
 6   Income/Expense  277 non-null    str
 7   Note.1          0 non-null      float64
 8   Amount          277 non-null    float64
 9   Currency        277 non-null    str
 10  Account.1       277 non-null    float64
dtypes: float64(5), str(6)
memory usage: 23.9 KB
None
'''

data_12 = pd.read_csv(path_file_expense_data, parse_dates=['Date']).info()

print(data_12)
'''
<class 'pandas.DataFrame'>
RangeIndex: 277 entries, 0 to 276
Data columns (total 11 columns):
 #   Column          Non-Null Count  Dtype
---  ------          --------------  -----
 0   Date            277 non-null    datetime64[us]
 1   Account         277 non-null    str
 2   Category        277 non-null    str
 3   Subcategory     0 non-null      float64
 4   Note            273 non-null    str
 5   INR             277 non-null    float64
 6   Income/Expense  277 non-null    str
 7   Note.1          0 non-null      float64
 8   Amount          277 non-null    float64
 9   Currency        277 non-null    str
 10  Account.1       277 non-null    float64
dtypes: datetime64[us](1), float64(5), str(5)
memory usage: 23.9 KB
None
'''






# 14. convertors
#-----------------


path_file_deliveries = os.path.join(path, '../../../../../Pandas/1_Dataset/deliveries.csv')

data_14 = pd.read_csv(path_file_deliveries).head()
print(data_14)

'''
   match_id  inning         batting_team                 bowling_team  over  ...  extra_runs total_runs player_dismissed dismissal_kind  fielder
0         1       1  Sunrisers Hyderabad  Royal Challengers Bangalore     1  ...           0          0              NaN            NaN      NaN
1         1       1  Sunrisers Hyderabad  Royal Challengers Bangalore     1  ...           0          0              NaN            NaN      NaN
2         1       1  Sunrisers Hyderabad  Royal Challengers Bangalore     1  ...           0          4              NaN            NaN      NaN
3         1       1  Sunrisers Hyderabad  Royal Challengers Bangalore     1  ...           0          0              NaN            NaN      NaN
4         1       1  Sunrisers Hyderabad  Royal Challengers Bangalore     1  ...           2          2              NaN            NaN      NaN

[5 rows x 21 columns]
'''


def change_bowling_team_name(name):
    if name == 'Royal Challengers Bangalore':
        return 'RCB'
    else:
        return name


data_14 = pd.read_csv(path_file_deliveries, converters={'bowling_team':change_bowling_team_name}).head()

print(data_14)
'''
   match_id  inning         batting_team bowling_team  over  ball  ... batsman_runs extra_runs total_runs  player_dismissed  dismissal_kind  fielder
0         1       1  Sunrisers Hyderabad          RCB     1     1  ...            0          0          0               NaN             NaN      NaN
1         1       1  Sunrisers Hyderabad          RCB     1     2  ...            0          0          0               NaN             NaN      NaN
2         1       1  Sunrisers Hyderabad          RCB     1     3  ...            4          0          4               NaN             NaN      NaN
3         1       1  Sunrisers Hyderabad          RCB     1     4  ...            0          0          0               NaN             NaN      NaN
4         1       1  Sunrisers Hyderabad          RCB     1     5  ...            0          2          2               NaN             NaN      NaN

[5 rows x 21 columns]
'''



# 14. na_values parameter
#-------------------------

# This attribute is mostly use to set a value NaN for handing perfect
# eg :-   _, % etc
# na_values=['Sunrisers Hyderabad']

data_14 = pd.read_csv(path_file_deliveries, na_values=['Sunrisers Hyderabad']).head()
print(data_14)
'''
   match_id  inning batting_team                 bowling_team  over  ball  ... batsman_runs extra_runs total_runs  player_dismissed  dismissal_kind  fielder
0         1       1          NaN  Royal Challengers Bangalore     1     1  ...            0          0          0               NaN             NaN      NaN 
1         1       1          NaN  Royal Challengers Bangalore     1     2  ...            0          0          0               NaN             NaN      NaN 
2         1       1          NaN  Royal Challengers Bangalore     1     3  ...            4          0          4               NaN             NaN      NaN 
3         1       1          NaN  Royal Challengers Bangalore     1     4  ...            0          0          0               NaN             NaN      NaN 
4         1       1          NaN  Royal Challengers Bangalore     1     5  ...            0          2          2               NaN             NaN      NaN 

[5 rows x 21 columns]
'''


# 16. Loading a huge dataset in chunks
#--------------------------------------

dfs = pd.read_csv(path_file_deliveries, chunksize=5000)


for chuncks in dfs:
    print(chuncks.shape)


'''
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(5000, 21)
(4078, 21)
'''