

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

(2). Distribution  Plot
=========================

. Used for univariate analysis
. Used to find out the distribution
. Range of the observation
. Central Tendency
. Is the data bimodal?
. Are there outliers?


Plots under this section
------------------------

(i). Hist Plot 
(ii). kdeplot
(iii). rugplot

'''

# Hellow gpt give all attribute of relational plot and what is its working and how is it use and add other information if required



# histlot 
#==============


# Axis level plot
#-----------------

# sns.histplot() -> axes level method -> rectangular 
#......................................................

sns.histplot(data=tips, x='total_bill')

plt.show()




# Figure level plot
#-------------------

# sns.displot() -> figure level method -> square shape
#...............................................

sns.displot(data=tips, x='total_bill', kind='hist')

plt.show()



sns.displot(data=tips, x='day', kind='hist')

plt.show()



# Where are we use figure level method
#--------------------------------------

# As seaborn library recommended to use figure level method




#------------
# Attributs
#------------


# hue
#.....

sns.displot(data=tips, x='tip', kind='hist', hue='sex')

plt.show()



# element
#.........


sns.displot(data=tips, x='tip', kind='hist', hue='sex', element='step')

plt.show()







# feceting using col and row -> not work with axis leve method
#............................

sns.displot(data=tips, x='tip', col='sex', kind='hist')
plt.show()