


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import os





path = os.path.dirname(__file__)
path_file_train = os.path.join(path, './0_DataSet/0_Titanic/train.csv')
path_file_test = os.path.join(path, './0_DataSet/0_Titanic/test.csv')


train = pd.read_csv(path_file_train)
test = pd.read_csv(path_file_test)

print(train.info())
'''
<class 'pandas.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   PassengerId  891 non-null    int64
 1   Survived     891 non-null    int64
 2   Pclass       891 non-null    int64
 3   Name         891 non-null    str
 4   Sex          891 non-null    str
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64
 7   Parch        891 non-null    int64
 8   Ticket       891 non-null    str
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    str
 11  Embarked     889 non-null    str
dtypes: float64(2), int64(5), str(5)
memory usage: 83.7 KB
None
'''


print(test.info())
'''
<class 'pandas.DataFrame'>
RangeIndex: 418 entries, 0 to 417
Data columns (total 11 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   PassengerId  418 non-null    int64
 1   Pclass       418 non-null    int64
 2   Name         418 non-null    str
 3   Sex          418 non-null    str
 4   Age          332 non-null    float64
 5   SibSp        418 non-null    int64
 6   Parch        418 non-null    int64
 7   Ticket       418 non-null    str
 8   Fare         417 non-null    float64
 9   Cabin        91 non-null     str
 10  Embarked     418 non-null    str
dtypes: float64(2), int64(4), str(5)
memory usage: 36.1 KB
None
'''



# Feature Engineering on Fare Col
#=================================


print(train['SibSp'].value_counts())
'''
SibSp
0    608
1    209
2     28
4     18
3     16
8      7
5      5
Name: count, dtype: int64
'''

print(train[train['SibSp'] == 8])
'''
     PassengerId  Survived  Pclass                               Name     Sex  Age  SibSp  Parch    Ticket   Fare Cabin Embarked
159          160         0       3         Sage, Master. Thomas Henry    male  NaN      8      2  CA. 2343  69.55   NaN        S
180          181         0       3       Sage, Miss. Constance Gladys  female  NaN      8      2  CA. 2343  69.55   NaN        S
201          202         0       3                Sage, Mr. Frederick    male  NaN      8      2  CA. 2343  69.55   NaN        S
324          325         0       3           Sage, Mr. George John Jr    male  NaN      8      2  CA. 2343  69.55   NaN        S
792          793         0       3            Sage, Miss. Stella Anna  female  NaN      8      2  CA. 2343  69.55   NaN        S
846          847         0       3           Sage, Mr. Douglas Bullen    male  NaN      8      2  CA. 2343  69.55   NaN        S
863          864         0       3  Sage, Miss. Dorothy Edith "Dolly"  female  NaN      8      2  CA. 2343  69.55   NaN        S
'''

# total fare = 69.55
# total family member including person = 8 + 2 + 1 = 11
# individual fare = 69.55 / 11  ~ 6.9_

print(train[train['Ticket'] == 'CA. 2343'])
'''
     PassengerId  Survived  Pclass                               Name     Sex  Age  SibSp  Parch    Ticket   Fare Cabin Embarked
159          160         0       3         Sage, Master. Thomas Henry    male  NaN      8      2  CA. 2343  69.55   NaN        S
180          181         0       3       Sage, Miss. Constance Gladys  female  NaN      8      2  CA. 2343  69.55   NaN        S
201          202         0       3                Sage, Mr. Frederick    male  NaN      8      2  CA. 2343  69.55   NaN        S
324          325         0       3           Sage, Mr. George John Jr    male  NaN      8      2  CA. 2343  69.55   NaN        S
792          793         0       3            Sage, Miss. Stella Anna  female  NaN      8      2  CA. 2343  69.55   NaN        S
846          847         0       3           Sage, Mr. Douglas Bullen    male  NaN      8      2  CA. 2343  69.55   NaN        S
863          864         0       3  Sage, Miss. Dorothy Edith "Dolly"  female  NaN      8      2  CA. 2343  69.55   NaN        S
'''

# There are only 8 family member were travel through this ticket CA. 2343 this is one of the problem

# I restof family member in test data set



df = pd.concat([train, test])
df.reset_index(inplace=True)

print(df[df['Ticket'] == 'CA. 2343'])
'''
     PassengerId  Survived  Pclass                               Name     Sex   Age  SibSp  Parch    Ticket   Fare Cabin Embarked
159          160       0.0       3         Sage, Master. Thomas Henry    male   NaN      8      2  CA. 2343  69.55   NaN        S
180          181       0.0       3       Sage, Miss. Constance Gladys  female   NaN      8      2  CA. 2343  69.55   NaN        S
201          202       0.0       3                Sage, Mr. Frederick    male   NaN      8      2  CA. 2343  69.55   NaN        S
324          325       0.0       3           Sage, Mr. George John Jr    male   NaN      8      2  CA. 2343  69.55   NaN        S
792          793       0.0       3            Sage, Miss. Stella Anna  female   NaN      8      2  CA. 2343  69.55   NaN        S
846          847       0.0       3           Sage, Mr. Douglas Bullen    male   NaN      8      2  CA. 2343  69.55   NaN        S
863          864       0.0       3  Sage, Miss. Dorothy Edith "Dolly"  female   NaN      8      2  CA. 2343  69.55   NaN        S
188         1080       NaN       3                    Sage, Miss. Ada  female   NaN      8      2  CA. 2343  69.55   NaN        S
342         1234       NaN       3              Sage, Mr. John George    male   NaN      1      9  CA. 2343  69.55   NaN        S
360         1252       NaN       3        Sage, Master. William Henry    male  14.5      8      2  CA. 2343  69.55   NaN        S
365         1257       NaN       3     Sage, Mrs. John (Annie Bullen)  female   NaN      1      9  CA. 2343  69.55   NaN        S
'''

print(df['Ticket'].value_counts())
'''
Ticket
CA. 2343              11
CA 2144                8
1601                   8
347082                 7
347077                 7
                      ..
365237                 1
347086                 1
A.5. 3236              1
SOTON/O.Q. 3101262     1
359309                 1
Name: count, Length: 929, dtype: int64
'''

print(df[df['Ticket'] == '1601'])
'''
     PassengerId  Survived  Pclass             Name   Sex   Age  SibSp  Parch Ticket     Fare Cabin Embarked
74            75       1.0       3    Bing, Mr. Lee  male  32.0      0      0   1601  56.4958   NaN        S
169          170       0.0       3    Ling, Mr. Lee  male  28.0      0      0   1601  56.4958   NaN        S
509          510       1.0       3   Lang, Mr. Fang  male  26.0      0      0   1601  56.4958   NaN        S
643          644       1.0       3  Foo, Mr. Choong  male   NaN      0      0   1601  56.4958   NaN        S
692          693       1.0       3     Lam, Mr. Ali  male   NaN      0      0   1601  56.4958   NaN        S
826          827       0.0       3     Lam, Mr. Len  male   NaN      0      0   1601  56.4958   NaN        S
838          839       1.0       3  Chip, Mr. Chang  male  32.0      0      0   1601  56.4958   NaN        S
39           931       NaN       3    Hee, Mr. Ling  male   NaN      0      0   1601  56.4958   NaN        S
'''



# Create a new column of Individual_fare

df['Individual_fare'] = df['Fare']/(df['SibSp'] + df['Parch'] + 1)


# Create a new column of Family_size

df['Family_size'] = df['SibSp'] + df['Parch'] + 1


# Create a new  column of Family_category

def transform_family_size(num):
    if num == 1:
        return 'alone'
    elif num > 1 and num < 5:
        return 'small'
    else:
        return 'large'

df['Family_category'] = df['Family_size'].apply(transform_family_size)


print(df[['Family_size', 'Family_category']])
'''
     Family_size Family_category
0              2           small
1              2           small
2              1           alone
3              2           small
4              1           alone
..           ...             ...
413            1           alone
414            1           alone
415            1           alone
416            1           alone
417            3           small

[1309 rows x 2 columns]
'''



print(pd.crosstab(df['Survived'], df['Family_category'], normalize='columns')*100)
'''
Family_category      alone      large      small
Survived
0.0              69.646182  83.870968  42.123288
1.0              30.353818  16.129032  57.876712
'''



df['surname'] = df['Name'].str.split(',').str.get(0)
df['title'] = df['Name'].str.split(',').str.get(1).str.split('.').str.get(0)

print(df['surname'])
print(df['title'].value_counts())

df['title'] = df['title'].str.replace('Rev', 'other')
df['title'] = df['title'].str.replace('Dr', 'other')
df['title'] = df['title'].str.replace('Col', 'other')
df['title'] = df['title'].str.replace('Major', 'other')
df['title'] = df['title'].str.replace('Don', 'other')
df['title'] = df['title'].str.replace('Capt', 'other')
df['title'] = df['title'].str.replace('The', 'other')
df['title'] = df['title'].str.replace('Jonkheer', 'other')

df['title'] = df['title'].str.replace('Ms', 'Miss')
df['title'] = df['title'].str.replace('Mlle', 'Miss')
df['title'] = df['title'].str.replace('Mme', 'Miss')
df['title'] = df['title'].str.replace('Lady', 'Miss')
df['title'] = df['title'].str.replace('Sir', 'Mr')
df['title'] = df['title'].str.replace('othera', 'other')
df['title'] = df['title'].str.replace('the Countess', 'other')


print(df['title'].value_counts())
'''
title
Mr        758
Miss      266
Mrs       197
Master     61
other      27
Name: count, dtype: int64
'''

print(pd.crosstab(df['Survived'], df['title'], normalize='columns')*100)
'''
title     Master       Miss         Mr   Mrs      other
Survived
0.0         42.5  29.411765  84.169884  20.8  71.428571
1.0         57.5  70.588235  15.830116  79.2  28.571429
'''



df.fillna({'Cabin': 'M'}, inplace=True)


print(df['Cabin'].value_counts())
'''
Cabin
M                  1014
C23 C25 C27           6
G6                    5
B57 B59 B63 B66       5
F33                   4
                   ...
C39                   1
B24                   1
D40                   1
D38                   1
C105                  1
Name: count, Length: 187, dtype: int64
'''


df['Deck'] = df['Cabin'].str[0]

print(df['Deck'].value_counts())
'''
Deck
M    1014
C      94
B      65
D      46
E      41
A      22
F      21
G       5
T       1
Name: count, dtype: int64
'''


print(pd.crosstab(df['Deck'], df['Pclass']))
'''
Pclass   1    2    3
Deck
A       22    0    0
B       65    0    0
C       94    0    0
D       40    6    0
E       34    4    3
F        0   13    8
G        0    0    5
M       67  254  693
T        1    0    0
'''


print(pd.crosstab(df['Deck'], df['Survived'], normalize='index')*100)

pd.crosstab(df['Deck'], df['Survived'], normalize='index').plot(kind='bar', stacked=True)
plt.show()