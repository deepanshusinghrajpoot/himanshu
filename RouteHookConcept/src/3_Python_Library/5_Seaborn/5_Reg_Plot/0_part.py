

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

(1). Regression Plot
=====================


Plots under this section
------------------------

(i). regplot
(ii). lmplot


. In the simplest invocation, both function draw a scatterplot of two variables, x and y, and then fit the regression model y ~ x and plot the
  resulting regression line a 95% confidence interval for that regression.


'''

# Hellow gpt give all attribute of relational plot and what is its working and how is it use and add other information if required



# Regression Plot 
#------------------

# sns.regplot() -> axes level method -> rectangular 
#......................................................

sns.regplot(data=tips, x='total_bill', y='tip')

plt.show()


# sns.lmplot() -> figure level method -> square shape
#...............................................

sns.lmplot(data=tips, x='total_bill', y='tip')

plt.show()





# Attributs
#------------


# hue
#.....


sns.lmplot(data=tips, x='total_bill', y='tip', hue='sex')

plt.show()










# sns.residplot() -> axes level method -> rectangular 
#=====================================================

sns.residplot(data=tips, x='total_bill', y='tip')

plt.show()