

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


import os



path = os.path.dirname(__file__)

path_file_gayle_175 = os.path.join(path, '../Pandas/1_Dataset/gayle-175.csv')


gayle = pd.read_csv(path_file_gayle_175)


print(gayle)
'''
          batsman  batsman_runs
0  AB de Villiers            31
1        CH Gayle           175
2       R Rampaul             0
3       SS Tiwary             2
4      TM Dilshan            33
5         V Kohli            11
'''



# pie chart
#===========

# gpt give perfect interview spoken diffinition

# pie chart use for Univariate/Bivariate Analysis :- mean bar chart apply on one or two column
# apply on both categorical and numerical column both

# Use cases - To find contribution on a standard scale



# simple data
#.............

data = [23, 45, 100, 20, 49]
subjects = ['eng', 'science', 'maths', 'sst', 'hindi']

plt.pie(data, labels=subjects)

plt.show()



# dataset
#.........

plt.pie(gayle['batsman_runs'], labels=gayle['batsman'])

plt.show()



# percentage and colors
#.......................

plt.pie(gayle['batsman_runs'], labels=gayle['batsman'], autopct='%0.1f%%', colors=['blue', 'green', 'yellow', 'pink', 'red', 'orange'])

plt.show()




# explode
#.........

plt.pie(gayle['batsman_runs'], labels=gayle['batsman'], autopct='%0.1f%%', colors=['blue', 'green', 'yellow', 'pink', 'red', 'orange'], explode=[0.1, 0, 0, 0, 0, 0.1])

plt.show()





