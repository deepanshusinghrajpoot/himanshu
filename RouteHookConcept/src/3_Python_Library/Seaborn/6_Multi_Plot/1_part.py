

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









'''

(6). Multi Plot
=====================

. explain pgt imp point

Plots under this section
------------------------

(i). Joint Plot
(ii). Pair Plot

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
149           5.9          3.0           5.1          1.8  virginica

[150 rows x 5 columns]

'''




# Hellow gpt give all attribute of relational plot and what is its working and how is it use and add other information if required



# (ii). Joint Plot
#==================


# Plotting Joinwise Relationship (JointGrid Vs jointplot)
#-------------------------------------------------------


# jointplot
#==========

sns.jointplot(data=tips, x='total_bill', y='tip', kind='hist')

plt.show()



# JointGrid
#===========


g = sns.JointGrid(data=tips, x='total_bill', y='tip')

g.plot(sns.scatterplot, sns.boxplot)

plt.show()











