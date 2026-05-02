

import numpy as np
import pandas as pd
import seaborn as sns


import os





# Why Seaborn?
#=================

'''

1. Provides a layer of abstraction hence simpler to use
2. Better aesthetics
3. More graphs included
4. Most popular



Seaborn Roadmap
---------------

Types of functions
..................

1. Figure Level
2. Axis Level


Main Classification
...................

1. Relational Plot
     (i). Scatter Plot
     (ii). Line Plot

2. Distribution Plot
     (i). Histogram Plot
     (ii). Kde Plot
     (iii). Rug Plot

3. Categorical Plot
     (i). Bar Plot
     (ii). Count Plot
     (iii). Box Plot
     (iv). Violin Plot
     (iiv). Swam Plot

4. Regression Plot
      
    
5. Matrix Plot
     (i). Heatmap Plot
     (ii). Clustormap Plot

6. Multiplots
     (i). Joint Plot
     (ii). Pair Plot



'''





# How are we see seaborn dataset
#===============================

print(sns.get_dataset_names())

'''
['anagrams', 'anscombe', 'attention', 'brain_networks', 'car_crashes', 'diamonds', 'dots',
 'dowjones', 'exercise', 'flights', 'fmri', 'geyser', 'glue', 'healthexp', 'iris', 'mpg', 'penguins',
 'planets', 'seaice', 'taxis', 'tips', 'titanic']
'''




# How to load specific dataset
#==============================

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