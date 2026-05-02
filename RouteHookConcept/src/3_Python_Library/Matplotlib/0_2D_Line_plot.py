
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



import os


path = os.path.dirname(__file__)

path_file_sharma_kohli = os.path.join(path, '../Pandas/1_Dataset/sharma-kohli.csv')

batsman = pd.read_csv(path_file_sharma_kohli)


print(batsman.info())



'''
<class 'pandas.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 3 columns):
 #   Column     Non-Null Count  Dtype
---  ------     --------------  -----
 0   index      10 non-null     int64
 1   RG Sharma  10 non-null     int64
 2   V Kohli    10 non-null     int64
dtypes: int64(3)
memory usage: 372.0 bytes
None
'''

print(batsman)
'''
   index  RG Sharma  V Kohli
0   2008        404      165
1   2009        362      246
2   2010        404      307
3   2011        372      557
4   2012        433      364
5   2013        538      639
6   2014        390      359
7   2015        482      505
8   2016        489      973
9   2017        333      308
'''




# Types of Data
#===============

# 1. Numerical Data
# 2. Categorical Data







# 2D Line plot
#===============

# gpt give perfect interview spoken diffinition

# 2D line plot use for Bivariate Analysis :- mean 2D line plot apply on two column
# categorical(first column) -> numberical(second column)
#  and 
# numerical(first column) -> numerical(second column)

# Use cases - Time series data




# Plotting a simple function
#===========================

price = [48000, 54000, 57000, 49000, 47000, 45000]
year = [2015, 2016, 2017, 2018, 2019, 2020]

plt.plot(year, price)
plt.show()



# From a pandas dataframe
#-------------------------

plt.plot(batsman['index'], batsman['V Kohli'])
plt.show()



plt.plot(batsman['index'], batsman['RG Sharma'])
plt.show()



plt.plot(batsman['index'], batsman['V Kohli'])
plt.plot(batsman['index'], batsman['RG Sharma'])
plt.show()




# labels title
#--------------


plt.plot(batsman['index'], batsman['V Kohli'])
plt.plot(batsman['index'], batsman['RG Sharma'])

plt.title('Rohit Sharma Vs Virat Kohli Comparison')
plt.xlabel('Season')
plt.ylabel('Runs Scored')

plt.show()



# color(hex) and line(width and style) and marker(size)
#-------------------------------------------------------


# color(hex)
#............

plt.plot(batsman['index'], batsman['V Kohli'], color='green')
plt.plot(batsman['index'], batsman['RG Sharma'], color='black')

plt.title('Rohit Vs Virat Kohli Career Comparison')
plt.xlabel('Season')
plt.ylabel('Runs Scored')

plt.show()


# linestyle : solid(default), dashed, dotted, dashdot
#.....................................................


plt.plot(batsman['index'], batsman['V Kohli'], color='green', linestyle='dashdot')
plt.plot(batsman['index'], batsman['RG Sharma'], color='black', linestyle='dotted')

plt.title('Rohit Vs Virat Kohli Career Comparison')
plt.xlabel('Season')
plt.ylabel('Runs Scored')

plt.show()



# linewidth 
#..........


plt.plot(batsman['index'], batsman['V Kohli'], color='green', linestyle='solid', linewidth=3)
plt.plot(batsman['index'], batsman['RG Sharma'], color='black', linestyle='dashdot', linewidth=2)

plt.title('Rohit Vs Virat Kohli Career Comparison')
plt.xlabel('Season')
plt.ylabel('Runs Scored')

plt.show()



# marker : D, +, ., >, o
#........


plt.plot(batsman['index'], batsman['V Kohli'], color='green', linestyle='solid', linewidth=3, marker='D')
plt.plot(batsman['index'], batsman['RG Sharma'], color='black', linestyle='dashdot', linewidth=2, marker='o')

plt.title('Rohit Vs Virat Kohli Career Comparison')
plt.xlabel('Season')
plt.ylabel('Runs Scored')

plt.show()



# markersize
#............

plt.plot(batsman['index'], batsman['V Kohli'], color='green', linestyle='solid', linewidth=3, marker='D', markersize=5)
plt.plot(batsman['index'], batsman['RG Sharma'], color='black', linestyle='dashdot', linewidth=2, marker='o', markersize=3)

plt.title('Rohit Vs Virat Kohli Career Comparison')
plt.xlabel('Season')
plt.ylabel('Runs Scored')

plt.show()



# legend() -> location(label)
#------------------------------

# label : best(default), upper right, upper left, lower left, lower right, right, center left, center right, lower center

plt.plot(batsman['index'], batsman['V Kohli'], color='green', linestyle='solid', linewidth=3, marker='D', markersize=5, label='Virat')
plt.plot(batsman['index'], batsman['RG Sharma'], color='black', linestyle='dashdot', linewidth=2, marker='o', markersize=3, label='Rohit')

plt.title('Rohit Vs Virat Kohli Career Comparison')
plt.xlabel('Season')
plt.ylabel('Runs Scored')

plt.legend()

plt.show()











# limiting axes
#==============



price = [48000, 54000, 57000, 49000, 47000, 45000, 4500000]
year = [2015, 2016, 2017, 2018, 2019, 2020, 2021]

plt.plot(year, price)

plt.ylim(0, 75000)
plt.xlim(2017, 2019)

plt.show()







# grid()
#========


plt.plot(batsman['index'], batsman['V Kohli'], color='green', linestyle='solid', linewidth=3, marker='D', markersize=5, label='Virat')
plt.plot(batsman['index'], batsman['RG Sharma'], color='black', linestyle='dashdot', linewidth=2, marker='o', markersize=3, label='Rohit')

plt.title('Rohit Vs Virat Kohli Career Comparison')
plt.xlabel('Season')
plt.ylabel('Runs Scored')

plt.legend()

plt.grid()

plt.show()



# show()
#========







# all attribute and function apply on this graph : gpt give table all attribute and method what role of that attribute and method
