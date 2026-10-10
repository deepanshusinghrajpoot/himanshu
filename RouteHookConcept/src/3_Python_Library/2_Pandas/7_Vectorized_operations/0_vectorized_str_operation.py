

import numpy as np
import pandas as pd


import os




# Vectorized Operations
#========================

# gpt give perfect interview spoken diffinition 



# What are vectorized operations
#=================================

a = np.array([1, 2, 3, 4])
print(a * 4)
'''
[ 4  8 12 16]
'''



# Problem in vectorized operation in vanilla python
#===================================================

s = ['cat', 'mat', None, 'rat']

# first problem
#...............

# print([i.startswith('c') for i in s]) :- this give error because of string operation not applicable on non string


# second problem
#...............

# very slow


# Pandas handle these type of problem
#.....................................

# because of python build on numpy and numpy build on c





# How pandas solves this issue?
#===============================

m = pd.Series(['cat', 'mat', None, 'rat'])

print(m)
'''
0    cat
1    mat
2    NaN
3    rat
dtype: str
'''

# string accessor
#.................
print(m.astype(str).str.startswith('c'))






# import titanic
#==================


path_dir = os.path.dirname(__file__)

path_file_titanic = os.path.join(path_dir, '../1_Dataset/titanic.csv')



titanic = pd.read_csv(path_file_titanic)


print(titanic)
'''
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
4              5         0       3  ...   8.0500   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q

[891 rows x 12 columns]
'''


print(titanic.columns)
'''
Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
      dtype='str')
'''



# Common Functions
#==================

# lower/upper/capitalize/title
#...............................

print(titanic['Name'].str.lower())

'''
0                                braund, mr. owen harris
1      cumings, mrs. john bradley (florence briggs th...
2                                 heikkinen, miss. laina
3           futrelle, mrs. jacques heath (lily may peel)
4                               allen, mr. william henry
                             ...
886                                montvila, rev. juozas
887                         graham, miss. margaret edith
888             johnston, miss. catherine helen "carrie"
889                                behr, mr. karl howell
890                                  dooley, mr. patrick
Name: Name, Length: 891, dtype: str
'''



print(titanic['Name'].str.upper())
'''
0                                BRAUND, MR. OWEN HARRIS
1      CUMINGS, MRS. JOHN BRADLEY (FLORENCE BRIGGS TH...
2                                 HEIKKINEN, MISS. LAINA
3           FUTRELLE, MRS. JACQUES HEATH (LILY MAY PEEL)
4                               ALLEN, MR. WILLIAM HENRY
                             ...
886                                MONTVILA, REV. JUOZAS
887                         GRAHAM, MISS. MARGARET EDITH
888             JOHNSTON, MISS. CATHERINE HELEN "CARRIE"
889                                BEHR, MR. KARL HOWELL
890                                  DOOLEY, MR. PATRICK
Name: Name, Length: 891, dtype: str
'''



print(titanic['Name'].str.capitalize())
'''
0                                Braund, mr. owen harris
1      Cumings, mrs. john bradley (florence briggs th...
2                                 Heikkinen, miss. laina
3           Futrelle, mrs. jacques heath (lily may peel)
4                               Allen, mr. william henry
                             ...
886                                Montvila, rev. juozas
887                         Graham, miss. margaret edith
888             Johnston, miss. catherine helen "carrie"
889                                Behr, mr. karl howell
890                                  Dooley, mr. patrick
Name: Name, Length: 891, dtype: str
'''


print(titanic['Name'].str.title())
'''
0                                Braund, Mr. Owen Harris
1      Cumings, Mrs. John Bradley (Florence Briggs Th...
2                                 Heikkinen, Miss. Laina
3           Futrelle, Mrs. Jacques Heath (Lily May Peel)
4                               Allen, Mr. William Henry
                             ...
886                                Montvila, Rev. Juozas
887                         Graham, Miss. Margaret Edith
888             Johnston, Miss. Catherine Helen "Carrie"
889                                Behr, Mr. Karl Howell
890                                  Dooley, Mr. Patrick
Name: Name, Length: 891, dtype: str
'''



# len
#.....

print(titanic['Name'].str.len())
'''
0      23
1      51
2      22
3      44
4      24
       ..
886    21
887    28
888    40
889    21
890    19
Name: Name, Length: 891, dtype: int64
'''

# Ques : Find that which name length maximum

print(titanic[titanic['Name'].str.len().max() == titanic['Name'].str.len()])
'''
     PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch    Ticket   Fare Cabin Embarked
307          308         1       1  Penasco y Castellana, Mrs. Victor de Satode (M...  female  17.0      1      0  PC 17758  108.9   C65        C
'''


# strip :- gpt give perfect interview spoken diffinition 
#......

# print(titanic['Name'].str.strip())
'''
0                                Braund, Mr. Owen Harris
1      Cumings, Mrs. John Bradley (Florence Briggs Th...
2                                 Heikkinen, Miss. Laina
3           Futrelle, Mrs. Jacques Heath (Lily May Peel)
4                               Allen, Mr. William Henry
                             ...
886                                Montvila, Rev. Juozas
887                         Graham, Miss. Margaret Edith
888             Johnston, Miss. Catherine Helen "Carrie"
889                                Behr, Mr. Karl Howell
890                                  Dooley, Mr. Patrick
Name: Name, Length: 891, dtype: str
'''



# split -> get
#..............

# gpt give perfect interview spoken diffinition


print(titanic['Name'].str.split(','))
'''
0                             [Braund,  Mr. Owen Harris]
1      [Cumings,  Mrs. John Bradley (Florence Briggs ...
2                              [Heikkinen,  Miss. Laina]
3        [Futrelle,  Mrs. Jacques Heath (Lily May Peel)]
4                            [Allen,  Mr. William Henry]
                             ...
886                             [Montvila,  Rev. Juozas]
887                      [Graham,  Miss. Margaret Edith]
888          [Johnston,  Miss. Catherine Helen "Carrie"]
889                             [Behr,  Mr. Karl Howell]
890                               [Dooley,  Mr. Patrick]
Name: Name, Length: 891, dtype: object
'''


print(titanic['Name'].str.split(',').str.get(0))
'''
0         Braund
1        Cumings
2      Heikkinen
3       Futrelle
4          Allen
         ...
886     Montvila
887       Graham
888     Johnston
889         Behr
890       Dooley
Name: Name, Length: 891, dtype: object
'''

titanic['lastname'] = titanic['Name'].str.split(',').str.get(0)

print(titanic['lastname'])
'''
0         Braund
1        Cumings
2      Heikkinen
3       Futrelle
4          Allen
         ...
886     Montvila
887       Graham
888     Johnston
889         Behr
890       Dooley
Name: lastname, Length: 891, dtype: object
'''

print(titanic['Name'].str.split(',').str.get(1))
'''
0                                  Mr. Owen Harris
1       Mrs. John Bradley (Florence Briggs Thayer)
2                                      Miss. Laina
3               Mrs. Jacques Heath (Lily May Peel)
4                                Mr. William Henry
                          ...
886                                    Rev. Juozas
887                           Miss. Margaret Edith
888                 Miss. Catherine Helen "Carrie"
889                                Mr. Karl Howell
890                                    Mr. Patrick
Name: Name, Length: 891, dtype: object
'''


print(titanic['Name'].str.split(',').str.get(1).str.split('.'))
'''
0                                 [ Mr,  Owen Harris]
1      [ Mrs,  John Bradley (Florence Briggs Thayer)]
2                                     [ Miss,  Laina]
3              [ Mrs,  Jacques Heath (Lily May Peel)]
4                               [ Mr,  William Henry]
                            ...
886                                   [ Rev,  Juozas]
887                          [ Miss,  Margaret Edith]
888                [ Miss,  Catherine Helen "Carrie"]
889                               [ Mr,  Karl Howell]
890                                   [ Mr,  Patrick]
Name: Name, Length: 891, dtype: object
'''


print(titanic['Name'].str.split(',').str.get(1).str.split('.').str.get(0))
'''
0         Mr
1        Mrs
2       Miss
3        Mrs
4         Mr
       ...
886      Rev
887     Miss
888     Miss
889       Mr
890       Mr
Name: Name, Length: 891, dtype: object
'''

print(titanic['Name'].str.split(',').str.get(1).str.strip().str.split(' ', n=1, expand=True))
'''
         0                                      1
0      Mr.                            Owen Harris
1     Mrs.  John Bradley (Florence Briggs Thayer)
2    Miss.                                  Laina
3     Mrs.          Jacques Heath (Lily May Peel)
4      Mr.                          William Henry
..     ...                                    ...
886   Rev.                                 Juozas
887  Miss.                         Margaret Edith
888  Miss.               Catherine Helen "Carrie"
889    Mr.                            Karl Howell
890    Mr.                                Patrick

[891 rows x 2 columns]
'''


titanic[['title', 'firstname']] = titanic['Name'].str.split(',').str.get(1).str.strip().str.split(' ', n=1, expand=True)

print(titanic[['title', 'firstname', 'lastname']])
'''
     title                              firstname   lastname
0      Mr.                            Owen Harris     Braund
1     Mrs.  John Bradley (Florence Briggs Thayer)    Cumings
2    Miss.                                  Laina  Heikkinen
3     Mrs.          Jacques Heath (Lily May Peel)   Futrelle
4      Mr.                          William Henry      Allen
..     ...                                    ...        ...
886   Rev.                                 Juozas   Montvila
887  Miss.                         Margaret Edith     Graham
888  Miss.               Catherine Helen "Carrie"   Johnston
889    Mr.                            Karl Howell       Behr
890    Mr.                                Patrick     Dooley

[891 rows x 3 columns]
'''



# Ques : Find out how many person contain specific title

print(titanic['title'].value_counts())
'''
Mr.          517
Miss.        182
Mrs.         125
Master.       40
Dr.            7
Rev.           6
Major.         2
Mlle.          2
Col.           2
Don.           1
Mme.           1
Ms.            1
Lady.          1
Sir.           1
Capt.          1
the            1
Jonkheer.      1
Name: count, dtype: int64
'''

# here has same mean of Miss. , Ms. , Mlle.


# replace
#.........

titanic['title'] = titanic['title'].str.replace('Ms.', 'Miss.')
titanic['title'] = titanic['title'].str.replace('Mlle.', 'Miss.')

print(titanic['title'].value_counts())
'''
Mr.          517
Miss.        185
Mrs.         125
Master.       40
Dr.            7
Rev.           6
Major.         2
Col.           2
Don.           1
Mme.           1
Lady.          1
Sir.           1
Capt.          1
the            1
Jonkheer.      1
Name: count, dtype: int64
'''







# filtering
#===========

# startswith/endswith
#.....................

print(titanic[titanic['firstname'].str.startswith('A')])

'''
     PassengerId  Survived  Pclass                                Name     Sex   Age  ...     Fare  Cabin Embarked       lastname  title            firstname
13            14         0       3         Andersson, Mr. Anders Johan    male  39.0  ...  31.2750    NaN        S      Andersson    Mr.         Anders Johan
22            23         1       3         McGowan, Miss. Anna "Annie"  female  15.0  ...   8.0292    NaN        Q        McGowan  Miss.         Anna "Annie"
35            36         0       1      Holverson, Mr. Alexander Oskar    male  42.0  ...  52.0000    NaN        S      Holverson    Mr.      Alexander Oskar
38            39         0       3  Vander Planke, Miss. Augusta Maria  female  18.0  ...  18.0000    NaN        S  Vander Planke  Miss.        Augusta Maria
61            62         1       1                 Icard, Miss. Amelie  female  38.0  ...  80.0000    B28      NaN          Icard  Miss.               Amelie
..           ...       ...     ...                                 ...     ...   ...  ...      ...    ...      ...            ...    ...                  ...
842          843         1       1             Serepeca, Miss. Augusta  female  30.0  ...  31.0000    NaN        C       Serepeca  Miss.              Augusta
845          846         0       3                 Abbing, Mr. Anthony    male  42.0  ...   7.5500    NaN        S         Abbing    Mr.              Anthony
866          867         1       2        Duran y More, Miss. Asuncion  female  27.0  ...  13.8583    NaN        C   Duran y More  Miss.             Asuncion
875          876         1       3    Najib, Miss. Adele Kiamie "Jane"  female  15.0  ...   7.2250    NaN        C          Najib  Miss.  Adele Kiamie "Jane"
876          877         0       3       Gustafsson, Mr. Alfred Ossian    male  20.0  ...   9.8458    NaN        S     Gustafsson    Mr.        Alfred Ossian

[95 rows x 15 columns]
'''


print(titanic[titanic['firstname'].str.endswith('A')])
'''
     PassengerId  Survived  Pclass                   Name     Sex  Age  SibSp  Parch    Ticket     Fare Cabin Embarked lastname  title firstname
64            65         0       1  Stewart, Mr. Albert A    male  NaN      0      0  PC 17605  27.7208   NaN        C  Stewart    Mr.  Albert A
303          304         1       2    Keane, Miss. Nora A  female  NaN      0      0    226593  12.3500  E101        Q    Keane  Miss.    Nora A
'''



# isdigit/isalpha
#.................

print(titanic[titanic['firstname'].str.isdigit()])
'''
Columns: [PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked, lastname, title, firstname]
Index: []
'''






