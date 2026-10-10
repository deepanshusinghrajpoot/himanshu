

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import os



path = os.path.dirname(__file__)

path_file_batsman_sesson_record = os.path.join(path, '../Pandas/1_Dataset/batsman_season_record.csv')



batsman_season_record = pd.read_csv(path_file_batsman_sesson_record)

print(batsman_season_record)
'''
          batsman  2015  2016  2017
0  AB de Villiers   513   687   216
1       DA Warner   562   848   641
2        MS Dhoni   372   284   290
3       RG Sharma   482   489   333
4         V Kohli   505   973   308
'''


# bar chart
#==========

# gpt give perfect interview spoken diffinition

# bar chart use for Bivariate Analysis :- mean bar chart apply on two column
# numerical(y) -> categorical(x)

# Use cases - Aggregate analysis of groups


# sipmle bar char
#-----------------

children = [10, 20, 40, 10, 30]
colors = ['red', 'blue', 'green', 'yellow', 'pink']

plt.bar(colors, children)
plt.show()
          

# all attribute and function apply on this graph : gpt give table all attribute and method what role of that attribute and method





# There are two type of bar char
#---------------------------------

# 1. Vertical bar chart
# 2. Horizontal bar chart


plt.barh(colors, children)
plt.show()



# Where we use vertical bar chart and Horizontal barchar
#.......................................................

# Vertical bar chart use when categorcal column only less then 5
# Horizontal bar chart use when categorical column grater that 5


plt.bar(batsman_season_record['batsman'], batsman_season_record['2015'])
plt.show()





# Nultiple Bar chart : Suppose that we want see 2015, 2016, 2017 record
#......................................................................

# xticks

plt.bar(np.arange(batsman_season_record.shape[0]) - 0.2, batsman_season_record['2015'], width=0.2)
plt.bar(np.arange(batsman_season_record.shape[0]), batsman_season_record['2016'], width=0.2)
plt.bar(np.arange(batsman_season_record.shape[0]) + 0.2, batsman_season_record['2017'], width=0.2)

plt.xticks(np.arange(batsman_season_record.shape[0]), batsman_season_record['batsman'])

plt.show()



# A problem
#-----------

children = [10, 20, 40, 10, 30]
colors = ['red red red red', 'blue blue blue blue', 'green green green green', 'yellow yellow yellow yellow', 'pink pink pink pink']

plt.figure(figsize=(8, 6))   # increase graph size

plt.bar(colors, children)

plt.xticks(rotation='vertical')

plt.tight_layout()          # automatically adjust spacing

plt.show()






# Stacked Bar chart
#-------------------

plt.bar(batsman_season_record['batsman'], batsman_season_record['2017'], label='2017')
plt.bar(batsman_season_record['batsman'], batsman_season_record['2016'], bottom=batsman_season_record['2017'], label='2016')
plt.bar(batsman_season_record['batsman'], batsman_season_record['2015'], bottom=(batsman_season_record['2017'] + batsman_season_record['2016']), label='2015')


plt.legend()

plt.show()