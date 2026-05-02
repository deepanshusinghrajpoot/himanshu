


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


import os



path = os.path.dirname(__file__)

path_file_vk = os.path.join(path, '../Pandas/1_Dataset/vk.csv')
path_file_arr = os.path.join(path, '../Pandas/1_Dataset/big-array.npy')

vk = pd.read_csv(path_file_vk)
arr = np.load(path_file_arr)

print(vk)
'''
     match_id  batsman_runs
0          12            62
1          17            28
2          20            64
3          27             0
4          30            10
..        ...           ...
136       624            75
137       626           113
138       632            54
139       633             0
140       636            54

[141 rows x 2 columns]
'''


print(arr)
'''
[33 39 37 ... 33 30 39]
'''

print(arr.shape)
'''
(11949,)
'''



# bar chart
#==========

# gpt give perfect interview spoken diffinition

# bar chart use for Univariate Analysis :- mean bar chart apply on one column
# numerical column

# Use cases - Frequency Count



# simple data  and handle bins
#.............................

import matplotlib.pyplot as plt

data = [32, 45, 56, 10, 15, 27, 61]

plt.hist(data, bins=[10, 25, 40, 55, 70], edgecolor='black')

plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.title("Histogram Example")

plt.show()




# on some data
#..............

plt.hist(vk['batsman_runs'], bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
plt.show()




# logarithmic scale
#...................


plt.hist(arr, log=True)
plt.show()