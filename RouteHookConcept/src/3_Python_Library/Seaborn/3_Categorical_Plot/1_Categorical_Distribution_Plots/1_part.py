

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px



tips = sns.load_dataset('tips')

print(tips)
'''
     total_bill   tip     sex smoker   day    time  size
0         16.99  1.01  Female     No   Sun  Dinner     2
1         10.34  1.66    Male     No   Sun  Dinner     3
2         21.01  3.50    Male     No   Sun  Dinner     3
3         23.68  3.31    Male     No   Sun  Dinner     2
4         24.59  3.61  Female     No   Sun  Dinner     4
..          ...   ...     ...    ...   ...     ...   ...
239       29.03  5.92    Male     No   Sat  Dinner     3
240       27.18  2.00  Female    Yes   Sat  Dinner     2
241       22.67  2.00    Male    Yes   Sat  Dinner     2
242       17.82  1.75    Male     No   Sat  Dinner     2
243       18.78  3.00  Female     No  Thur  Dinner     2

[244 rows x 7 columns]
'''




iris = sns.load_dataset('iris')

print(iris)

'''
     sepal_length  sepal_width  petal_length  petal_width    species
0             5.1          3.5           1.4          0.2     setosa
1             4.9          3.0           1.4          0.2     setosa
2             4.7          3.2           1.3          0.2     setosa
3             4.6          3.1           1.5          0.2     setosa
4             5.0          3.6           1.4          0.2     setosa
..            ...          ...           ...          ...        ...
145           6.7          3.0           5.2          2.3  virginica
146           6.3          2.5           5.0          1.9  virginica
147           6.5          3.0           5.2          2.0  virginica
148           6.2          3.4           5.4          2.3  virginica
149           5.9          3.0           5.1          1.8  virginica

[150 rows x 5 columns]
'''


# Categorical Plots
#===================

'''

Categorical Scatter Plot
------------------------

. Stripplot
. Swarmplot


Categorical Distribution Plots
------------------------------

. Boxplot
. Violinplot


Categorical Estimate Plot -> for central tendency
-------------------------------------------------

. Barplot
. Pointplot
. Countplot
 
'''


# Hellow gpt give all attribute of relational plot and what is its working and how is it use and add other information if required




# Categorical Distribution Plot
# ==============================


# Axis level plot
#------------------

# sns.violinplot() -> axes level method -> rectangular  (violinplot = Boxplot + KDEplot)
#......................................................


sns.violinplot(data=tips, x='day', y='total_bill')

plt.show()

# gpt give the diagram on vs code to explain meaning




# Figure level plot
#...................

# sns.catplot() -> figure level method -> square shape
#......................................................

sns.catplot(data=tips, x='day', y='total_bill', kind='violin')

plt.show()



# gpt give the diagram on vs code to explain meaning



# Single boxplot
# ..............

sns.catplot(data=tips, y='total_bill', kind='violin')

plt.show()


# gpt give the diagram on vs code to explain meaning




#------------
# Attributs
#------------


# hue
#.....


sns.catplot(data=tips, x='day', y='total_bill', hue='sex', kind='violin')

plt.show()


# split
#.......

sns.catplot(data=tips, x='day', y='total_bill', hue='sex', kind='violin', split=True)

plt.show()




# feceting using col and row -> not work with axis leve method
#............................

sns.catplot(data=tips, x='day', y='total_bill', col='sex', kind='violin')
plt.show()





