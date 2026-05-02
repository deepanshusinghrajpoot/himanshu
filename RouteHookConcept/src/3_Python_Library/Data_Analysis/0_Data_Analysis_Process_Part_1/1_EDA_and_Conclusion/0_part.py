

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
Expolatory Data Analysis (EDA)
==============================

Why do EDA
-----------

1. Model building : Suppose that when we are want to make model to predict the pesenger servive or not
2. Analysis and reporting : Supose I have company data to identify why our company going to loss 
3. Validate assumptions :
4. Handling missing values :
5. Feature engineering :
6. Detecting outliers :


#--------------------------------------
# Remember it is an iterative process
#--------------------------------------

'''

'''

EDA Step
#=======

Step 1 : label col 
Step 2 : Univariate
Step 3 : Bivariate
Step 4 : Multivariate
      Step 5 : Feature Engineering (Outlier, Impute Missing Value)

Now repeate step


Step 1 : label col 
==================

lable our table column

Column Types
------------

Table - Train

Numerical - Age,Fare,PassengerId
Categorical - Survived, Pclass, Sex, SibSp, Parch,Embarked
Mixed - Name, Ticket, Cabin



Step 2 : Univariate Analysis
=============================

Univariate analysis focuses on analyzing each feature in the dataset independently.

Distribution analysis: The distribution of each feature is examined to identify its shape, central tendency(mean, median, mode), and dispersion.
......................

Identifying potential issues: Univariate analysis helps in identifying potential problems with the data such as outliers, skewness, and missing values
.............................



shape
------

The shape of a data distribution refers to its overall pattern or form as it is represented on a graph. Some common shapes of data distributions include:

Normal Distribution: A symmetrical and bell-shaped distribution where the mean, median, and mode are equal and the majority of the data falls in the middle of the distribution with gradually decreasing frequencies towards the tails.
....................

Skewed Distribution: A distribution that is not symmetrical, with one tail being longer than the other. It can be either positively skewed (right-skewed) or negatively skewed (left-skewed).
....................

Bimodal Distribution: A distribution with two peaks or modes.
.....................

Uniform Distribution: A distribution where all values have an equal chance of occurring.
.....................

The shape of the data distribution is important in identifying the presence of outliers, skewness, and the type of statistical tests and models that can be used for further analysis.





Dispersion
-----------

Dispersion is a statistical term used to describe the spread or variability of a set of data. 
It measures how far the values in a data set are spread out from the central tendency (mean, median, or mode) of the data.

There are several measures of dispersion, including:

Range: The difference between the largest and smallest values in a data set.
......

Variance: The average of the squared deviations of each value from the mean of the data set.
.........

Standard Deviation: The square root of the variance. It provides a measure of the spread of the data that is in the same units as the original data.
...................

Interquartile range (IQR): The range between the first quartile (25th percentile) and the third quartile (75th percentile) of the data.
..........................

Dispersion helps to describe the spread of the data, which can help to identify the presence of outliers and skewness in the data.

'''







'''

Steps of doing Univariate Analysis on Numerical columns
--------------------------------------------------------

Descriptive Statistics: Compute basic summary statistics for the column, such as mean, median, mode, standard deviation, range, and quartiles.
....................... These statistics give a general understanding of the distribution of the data and can help identify skewness or outliers.


Visualizations: Create visualizations to explore the distribution of the data. Some common visualizations for numerical data include histograms, 
............... box plots, and density plots. These visualizations provide a visual representation of the distribution of the data and can help 
                identify skewness an outliers.


Identifying Outliers: Identify and examine any outliers in the data. Outliers can be identified using visualizations. 
..................... It is important to determine whether the outliers are due to measurement errors, data entry errors, or 
                      legitimate differences in the data, and to decide whether to include or exclude them from the analysis.


Skewness: Check for skewness in the data and consider transforming the data or using robust statistical methods that are 
......... less sensitive to skewness, if necessary.


Conclusion: Summarize the findings of the EDA and make decisions about how to proceed with further analysis.
...........

'''




print(train.head())
'''
   PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked
0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S    
1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C    
2            3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S    
3            4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0            113803  53.1000  C123        S    
4            5         0       3                           Allen, Mr. William Henry    male  35.0      0      0            373450   8.0500   NaN        S    
'''                   










'''
 Age Column
-------------

Conclusion
    - Age is normally(almost) distributed
    - 20% of the values are missing
    - There are some outliers

    
 Fare Column
-------------

Conclusion
    - The data is highly(positively) skewed
    - Fare column ectually contains the group fare and not the individual fare
      (This might be an issue )
    - We need to create a new column called individual fare
'''




#==========================================================
# Univariant Analysis on numerical column
#==========================================================


#-------------------------------------------------------------------------------------------------------------------------------------------
'''
 Age Column
-------------

Conclusion
    - Age is normally(almost) distributed
    - 20% of the values are missing
    - There are some outliers
'''


# Descriptive Statistics & Visualizations
#----------------------------------------

print(train['Age'].describe())
'''
count    714.000000
mean      29.699118
std       14.526497
min        0.420000
25%       20.125000
50%       28.000000
75%       38.000000
max       80.000000
Name: Age, dtype: float64


Here, 25% people age less than 20.125000
Here, 50% people age less than 28.000000
Here, 75% people age less than 38.000000
'''

train['Age'].plot(kind='hist', bins=20)
plt.show()


train['Age'].plot(kind='kde')
plt.show()



# Skewness:
#-----------
'''
Check skewness
--------------

if skew number is near to zero mean almost normal distributed data
if skew number is more positive than it is positive skew data
if skew number is more negative than it is negative skew data
'''

print(train['Age'].skew())
# 0.38910778230082704





'''

BOX PLOT INTERPRETATION
-----------------------

A box plot represents the distribution of data using quartiles.

STRUCTURE

Min ─────|──────[ Q1 ─ Median ─ Q3 ]──────|──── Max
               <----- IQR ----->

Q1 → 25th percentile
Median → 50th percentile
Q3 → 75th percentile

The box between Q1 and Q3 is called the Interquartile Range (IQR).
It contains the middle 50% of the data.

WHISKERS

The lines extending from the box are called whiskers.
They show the spread of the remaining data.

OUTLIERS

Points that fall outside the whiskers are called outliers.

Outliers are calculated using:

Lower Bound = Q1 − 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR

Any value outside these bounds is plotted as a dot
outside the whiskers.




Note : Box plot is use to find outliers

'''

train['Age'].plot(kind='box')
plt.show()


# After see box plot we are observ outlier exist after age 60
# So, we are confirm that oulier is realy a outlier or valid data

print(train[train['Age'] > 60])
'''
     PassengerId  Survived  Pclass                                       Name     Sex   Age  SibSp  Parch       Ticket      Fare        Cabin Embarked
33            34         0       2                      Wheadon, Mr. Edward H    male  66.0      0      0   C.A. 24579   10.5000          NaN        S       
54            55         0       1             Ostby, Mr. Engelhart Cornelius    male  65.0      0      1       113509   61.9792          B30        C       
96            97         0       1                  Goldschmidt, Mr. George B    male  71.0      0      0     PC 17754   34.6542           A5        C       
116          117         0       3                       Connors, Mr. Patrick    male  70.5      0      0       370369    7.7500          NaN        Q       
170          171         0       1                  Van der hoef, Mr. Wyckoff    male  61.0      0      0       111240   33.5000          B19        S       
252          253         0       1                  Stead, Mr. William Thomas    male  62.0      0      0       113514   26.5500          C87        S       
275          276         1       1          Andrews, Miss. Kornelia Theodosia  female  63.0      1      0        13502   77.9583           D7        S       
280          281         0       3                           Duane, Mr. Frank    male  65.0      0      0       336439    7.7500          NaN        Q       
326          327         0       3                  Nysveen, Mr. Johan Hansen    male  61.0      0      0       345364    6.2375          NaN        S       
438          439         0       1                          Fortune, Mr. Mark    male  64.0      1      4        19950  263.0000  C23 C25 C27        S       
456          457         0       1                  Millet, Mr. Francis Davis    male  65.0      0      0        13509   26.5500          E38        S       
483          484         1       3                     Turkula, Mrs. (Hedwig)  female  63.0      0      0         4134    9.5875          NaN        S       
493          494         0       1                    Artagaveytia, Mr. Ramon    male  71.0      0      0     PC 17609   49.5042          NaN        C       
545          546         0       1               Nicholson, Mr. Arthur Ernest    male  64.0      0      0          693   26.0000          NaN        S       
555          556         0       1                         Wright, Mr. George    male  62.0      0      0       113807   26.5500          NaN        S       
570          571         1       2                         Harris, Mr. George    male  62.0      0      0  S.W./PP 752   10.5000          NaN        S       
625          626         0       1                      Sutton, Mr. Frederick    male  61.0      0      0        36963   32.3208          D50        S       
630          631         1       1       Barkworth, Mr. Algernon Henry Wilson    male  80.0      0      0        27042   30.0000          A23        S       
672          673         0       2                Mitchell, Mr. Henry Michael    male  70.0      0      0   C.A. 24580   10.5000          NaN        S       
745          746         0       1               Crosby, Capt. Edward Gifford    male  70.0      1      1    WE/P 5735   71.0000          B22        S       
829          830         1       1  Stone, Mrs. George Nelson (Martha Evelyn)  female  62.0      0      0       113572   80.0000          B28      NaN       
851          852         0       3                        Svensson, Mr. Johan    male  74.0      0      0       347060    7.7750          NaN        S       
'''


# missing value
#---------------

print((train['Age'].isnull().sum()/len(train['Age']))*100)
# 19.865319865319865 : % value are missing


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


'''
 Fare Column
-------------

Conclusion
    - The data is highly(positively) skewed
    - Fare column ectually contains the group fare and not the individual fare
      (This might be an issue )
    - We need to create a new column called individual fare
'''



# Descriptive Statistics & Visualizations
#----------------------------------------

print(train['Fare'].describe())
'''
count    891.000000
mean      32.204208
std       49.693429
min        0.000000
25%        7.910400
50%       14.454200
75%       31.000000
max      512.329200
Name: Fare, dtype: float64
'''

train['Fare'].plot(kind='hist')
plt.show()

train['Fare'].plot(kind='kde')
plt.show()



# check skewness
#----------------

print(train['Fare'].skew())
# 4.787316519674893 : highly positive skew value


# check outliers
#---------------

train['Fare'].plot(kind='box')
plt.show()

# After observe the box plot we are see it contain so many outlier
print(train[train['Fare'] > 250])
'''
     PassengerId  Survived  Pclass                                   Name     Sex   Age  SibSp  Parch    Ticket      Fare            Cabin Embarked
27            28         0       1         Fortune, Mr. Charles Alexander    male  19.0      3      2     19950  263.0000      C23 C25 C27        S
88            89         1       1             Fortune, Miss. Mabel Helen  female  23.0      3      2     19950  263.0000      C23 C25 C27        S
258          259         1       1                       Ward, Miss. Anna  female  35.0      0      0  PC 17755  512.3292              NaN        C
311          312         1       1             Ryerson, Miss. Emily Borie  female  18.0      2      2  PC 17608  262.3750  B57 B59 B63 B66        C
341          342         1       1         Fortune, Miss. Alice Elizabeth  female  24.0      3      2     19950  263.0000      C23 C25 C27        S
438          439         0       1                      Fortune, Mr. Mark    male  64.0      1      4     19950  263.0000      C23 C25 C27        S
679          680         1       1     Cardeza, Mr. Thomas Drake Martinez    male  36.0      0      1  PC 17755  512.3292      B51 B53 B55        C
737          738         1       1                 Lesurer, Mr. Gustave J    male  35.0      0      0  PC 17755  512.3292             B101        C
742          743         1       1  Ryerson, Miss. Susan Parker "Suzette"  female  21.0      2      2  PC 17608  262.3750  B57 B59 B63 B66        C
'''


# check null
#-----------

print((train['Fare'].isnull().sum()/len(train['Fare']))*100)
# 0.0 :- here no any missing value exist



