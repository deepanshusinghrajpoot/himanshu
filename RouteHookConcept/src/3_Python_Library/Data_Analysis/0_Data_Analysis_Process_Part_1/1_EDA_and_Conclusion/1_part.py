

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import os





path = os.path.dirname(__file__)
path_file_train = os.path.join(path, './0_DataSet/0_Titanic/train.csv')



train = pd.read_csv(path_file_train)

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


'''

Steps of doing Univariate Analysis on Categorical columns
---------------------------------------------------------

Descriptive Statistics: Compute the frequency distribution of the categories in the column. This will give a general understanding 
....................... of the distribution of the categories and their relative frequencies.

Visualizations: Create visualizations to explore the distribution of the categories. Some common visualizations for categorical
............... data include count plots and pie charts. These visualizations provide a visual representation of the distribution 
                of the categories and can help identify any patterns or anomalies in the data.

Missing Values: Check for missing values in the data and decide how to handle them. Missing values can be imputed or 
............... excluded from the analysis, depending on the research question and the data set.

Conclusion: Summarize the findings of the EDA and make decisions about how to proceed with further analysis.
...........

'''








#==========================================================
# Univariant Analysis on numerical column
#==========================================================


#-------------------------------------------------------------------------------------------------------------------------------------------
'''
 Survived Column
-----------------

Conclusion
    - Accident was very dedly because more than 40% could not servive
'''


# Descriptive Statistics & Visualizations
#----------------------------------------

print(train['Survived'].value_counts())
'''
Survived
0    549
1    342
Name: count, dtype: int64
'''

train['Survived'].value_counts().plot(kind='bar')
plt.show()


train['Survived'].value_counts().plot(kind='pie', autopct='%0.1f%%')
plt.show()



# Check missing value
#---------------------

print(train['Survived'].isnull().sum())
# 0 :- There are no missing value



#--------------------------------------------------------------------------------------------


'''
 Pclass Column
---------------

Conclusion
    - Serpriously Pclass 2 has more pasenser comparision to Pclass 1
'''


# Descriptive Statistics & Visualizations
#----------------------------------------

print(train['Pclass'].value_counts())
'''
Pclass
3    491
1    216
2    184
Name: count, dtype: int64
'''

train['Pclass'].value_counts().plot(kind='bar')
plt.show()


train['Pclass'].value_counts().plot(kind='pie', autopct='%0.1f%%')
plt.show()



# Check missing value
#---------------------

print(train['Pclass'].isnull().sum())
# 0 :- There are no missing value





#--------------------------------------------------------------------------------------------


'''
 Sex Column
------------

Conclusion
    
'''


# Descriptive Statistics & Visualizations
#----------------------------------------

print(train['Sex'].value_counts())
'''
Sex
male      577
female    314
Name: count, dtype: int64
'''

train['Sex'].value_counts().plot(kind='bar')
plt.show()


train['Sex'].value_counts().plot(kind='pie', autopct='%0.1f%%')
plt.show()



# Check missing value
#---------------------

print(train['Sex'].isnull().sum())
# 0 :- There are no missing value






#--------------------------------------------------------------------------------------------


'''
SibSp Column (number of sibling travel with person)
------------


Conclusion
    - Parch and SibSp cols can be merged to form a new col call family_size
    - Create a new col called is_alone
'''


# Descriptive Statistics & Visualizations
#----------------------------------------

print(train['SibSp'].value_counts())
'''
SibSp
0    608    : 0 mean only travel person
1    209    : 1 mean one sibling travel with person
2     28    : 2 mean two sibling travel with person
4     18    : 4 mean four sibling travel with person
3     16    : 3 mean three sibling travel with person
8      7    : 8 mean eight sibling travel with person
5      5    : 5 mean five sibling travel with person
Name: count, dtype: int64
'''

train['SibSp'].value_counts().plot(kind='bar')
plt.show()


train['SibSp'].value_counts().plot(kind='pie', autopct='%0.1f%%')
plt.show()



# Check missing value
#---------------------

print(train['SibSp'].isnull().sum())
# 0 :- There are no missing value






#--------------------------------------------------------------------------------------------


'''
Parch Column (number of parent or child travel)
------------

Conclusion
    - Parch and SibSp cols can be merged to form a new col call family_size
    - Create a new col called is_alone
'''


# Descriptive Statistics & Visualizations
#----------------------------------------

print(train['Parch'].value_counts())
'''
Parch
0    678
1    118
2     80
5      5
3      5
4      4
6      1
Name: count, dtype: int64
'''

train['Parch'].value_counts().plot(kind='bar')
plt.show()


train['Parch'].value_counts().plot(kind='pie', autopct='%0.1f%%')
plt.show()



# Check missing value
#---------------------

print(train['Parch'].isnull().sum())
# 0 :- There are no missing value










#--------------------------------------------------------------------------------------------


'''
Embarked Column (Where was pasenger start journey)
------------

Conclusion
    - Two pasenser starting journey missing
'''


# Descriptive Statistics & Visualizations
#----------------------------------------

print(train['Embarked'].value_counts())
'''
Embarked
S    644
C    168
Q     77
Name: count, dtype: int64
'''

train['Embarked'].value_counts().plot(kind='bar')
plt.show()


train['Embarked'].value_counts().plot(kind='pie', autopct='%0.1f%%')
plt.show()



# Check missing value
#---------------------

print(train['Embarked'].isnull().sum())
# 2 :- There are no missing value

print(train[train['Embarked'].isnull()])


