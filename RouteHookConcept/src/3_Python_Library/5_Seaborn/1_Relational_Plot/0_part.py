

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

(1). Relational Plot
=====================

. To see the statistical relation between 2 or more variables.
. Bivariate Analysis


Plots under this section
------------------------

(i). Scatter Plot
(ii). Line Plot

'''

# Hellow gpt give all attribute of relational plot and what is its working and how is it use and add other information if required



# Scatter Plot 
#---------------

# sns.scatterplot() -> axes level method -> rectangular 
#......................................................

sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex', style='time', size='size')

plt.show()


# sns.relplot() -> figure level method -> square shape
#...............................................

sns.relplot(data=tips, x='total_bill', y='tip', kind='scatter', hue='sex', style='time', size='size')

plt.show()



# Where are we use figure level method
#--------------------------------------

# As seaborn library recommended to use figure level method






