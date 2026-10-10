


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

Steps of doing Bivariate Analysis
Select 2 cols

Understand type of relationship

    1. Numerical - Numerical
          a. You can plot graphs like scatterplot(regression plots), 2D histplot, 2D KDEplots
          b. Check correlation coefficent to check linear relationship

    2. Numerical - Categorical - create visualizations that compare the distribution of the numerical data across different categories of the categorical data.
          a. You can plot graphs like barplot, boxplot, kdeplot violinplot even scatterplots

    3. Categorical - Categorical
          a. You can create cross-tabulations or contingency tables that show the distribution of values in one categorical column, grouped by the values in the other categorical column.
          b. You can plots like heatmap, stacked barplots, treemaps

          
Write your conclusions
    - Pclass pasenger servive chance 1 > 2 > 3
    - Female servive chance high comparision to male
    - On basis of pasenger start journey servive chance C > Q > S
               Because there are many Pclass 1 pasenger start journey from station C

'''


'''

Bivariate Analysis 
------------------
There are total combination 11 * 10
it take more time because there are so many combination

So we are choose important column according to our goal
just like our goal is make a modle to predict the pasenger servive or not 

'''



#--------------------------------------------------------------------------------------------------------

'''
Selected two columns : Survived, Pclass
     Here,
            Survived is Categorical column
            Pclass is also a Categorical column

          So, 
             We apply :-  3. Categorical - Categorical
'''

print(pd.crosstab(train['Survived'], train['Pclass']))
'''
Pclass      1   2    3
Survived
0          80  97  372
1         136  87  119
'''

# crosstab
#----------
# attribute
# normalize contain three parameter :- index, column, all

print(pd.crosstab(train['Survived'], train['Pclass'], normalize='columns'))
'''
Pclass          1         2         3
Survived
0         0.37037  0.527174  0.757637
1         0.62963  0.472826  0.242363
'''

print(pd.crosstab(train['Survived'], train['Pclass'], normalize='columns')*100)
'''
Pclass            1          2          3
Survived
0         37.037037  52.717391  75.763747
1         62.962963  47.282609  24.236253
'''


sns.heatmap(pd.crosstab(train['Survived'], train['Pclass'], normalize='columns')*100)
plt.show()




#--------------------------------------------------------------------------------------------------------

'''
Selected two columns : Survived, Sex
     Here,
            Survived is Categorical column
            Sex is also a Categorical column

          So, 
             We apply :-  3. Categorical - Categorical
'''

print(pd.crosstab(train['Survived'], train['Sex']))
'''
Sex       female  male
Survived
0             81   468
1            233   109
'''

# crosstab
#----------
# attribute
# normalize contain three parameter :- index, column, all

print(pd.crosstab(train['Survived'], train['Sex'], normalize='columns'))
'''
Sex         female      male
Survived
0         0.257962  0.811092
1         0.742038  0.188908
'''

print(pd.crosstab(train['Survived'], train['Sex'], normalize='columns')*100)
'''
Sex          female       male
Survived
0         25.796178  81.109185
1         74.203822  18.890815
'''

sns.heatmap(pd.crosstab(train['Survived'], train['Sex'], normalize='columns')*100)
plt.show()








#--------------------------------------------------------------------------------------------------------

'''
Selected two columns : Survived, Embarked
     Here,
            Survived is Categorical column
            Embarked is also a Categorical column

          So, 
             We apply :-  3. Categorical - Categorical
'''

print(pd.crosstab(train['Survived'], train['Embarked']))
'''
Embarked   C   Q    S
Survived
0         75  47  427
1         93  30  217
'''

# crosstab
#----------
# attribute
# normalize contain three parameter :- index, column, all

print(pd.crosstab(train['Survived'], train['Embarked'], normalize='columns'))
'''
Embarked         C        Q         S
Survived
0         0.446429  0.61039  0.663043
1         0.553571  0.38961  0.336957
'''

print(pd.crosstab(train['Survived'], train['Embarked'], normalize='columns')*100)
'''
Embarked          C          Q          S
Survived
0         44.642857  61.038961  66.304348
1         55.357143  38.961039  33.695652
'''

sns.heatmap(pd.crosstab(train['Survived'], train['Embarked'], normalize='columns')*100)
plt.show()


'''
My Assumption On basis of pasenger start journey servive chance C > Q > S 
  1 - There are many female pasenger start journey from station C
  2 - There are many Pclass 1 pasenger start journey from station C

'''


print(pd.crosstab(train['Sex'], train['Embarked'], normalize='columns')*100)
'''
Embarked          C          Q          S
Sex
female    43.452381  46.753247  31.521739
male      56.547619  53.246753  68.478261
'''

# My First Assumption is wrong


print(pd.crosstab(train['Pclass'], train['Embarked'], normalize='columns')*100)
'''
Embarked          C          Q          S
Pclass
1         50.595238   2.597403  19.720497
2         10.119048   3.896104  25.465839
3         39.285714  93.506494  54.813665
'''

# My Second Assumption is right







#--------------------------------------------------------------------------------------------------------

'''
Selected two columns : Survived, Age
     Here,
            Survived is Categorical column
            Embarked is also a Numerical column

          So, 
             We apply :-  2. Numerical - Categorical
'''


train[train['Survived'] == 1]['Age'].plot(kind='kde', lable='Servived')
train[train['Survived'] == 0]['Age'].plot(kind='kde', lable='Not Servived')

plt.legend()
plt.show()