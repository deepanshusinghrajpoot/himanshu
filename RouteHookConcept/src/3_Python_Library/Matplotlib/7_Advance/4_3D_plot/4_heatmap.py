

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


import os



path = os.path.dirname(__file__)

path_file_IPL_Ball_by_Ball_2008_2022 = os.path.join(path, '../../../Pandas/1_Dataset/IPL_Ball_by_Ball_2008_2022.csv')

delivery = pd.read_csv(path_file_IPL_Ball_by_Ball_2008_2022)


print(delivery.info())
'''
<class 'pandas.DataFrame'>
RangeIndex: 225954 entries, 0 to 225953
Data columns (total 17 columns):
 #   Column             Non-Null Count   Dtype
---  ------             --------------   -----
 0   ID                 225954 non-null  int64
 1   innings            225954 non-null  int64
 2   overs              225954 non-null  int64
 3   ballnumber         225954 non-null  int64
 4   batter             225954 non-null  str
 5   bowler             225954 non-null  str
 6   non-striker        225954 non-null  str
 7   extra_type         12049 non-null   str
 8   batsman_run        225954 non-null  int64
 9   extras_run         225954 non-null  int64
 10  total_run          225954 non-null  int64
 11  non_boundary       225954 non-null  int64
 12  isWicketDelivery   225954 non-null  int64
 13  player_out         11151 non-null   str
 14  kind               11151 non-null   str
 15  fielders_involved  7988 non-null    str
 16  BattingTeam        225954 non-null  str
dtypes: int64(9), str(8)
memory usage: 29.3 MB
None
'''

print(delivery['ballnumber'].unique())
'''
[ 1  2  3  4  5  6  7  8  9 10]
'''

temp_df = delivery[(delivery['ballnumber'].isin([1, 2, 3, 4, 5, 6])) & (delivery['batsman_run'] == 6)]


print(temp_df.pivot_table(index='overs', columns='ballnumber', values='batsman_run', aggfunc='count'))
'''
ballnumber    1    2    3    4    5    6
overs
0             9   17   31   39   33   27
1            31   40   49   56   58   54
2            75   62   70   72   58   76
3            60   74   74  103   74   71
4            71   76  112   80   81   72
5            77  102   63   86   78   80
6            34   56   49   59   64   38
7            59   62   73   70   69   56
8            86   83   79   81   73   52
9            54   62   86   61   74   67
10           82   92   83   69   72   70
11           91   72   87   79   87   70
12           87  109   79  100  100   84
13          101  101   99   97   90   88
14           90  124  103  100   86  106
15          102  120  129  121  113   96
16          107  115  111  100  120  101
17          126  142  137  151  117  129
18          118  114  151  132  138  128
19          136  120  151  151  116  148
'''


grid = temp_df.pivot_table(index='overs', columns='ballnumber', values='batsman_run', aggfunc='count')


# Hitmap
#========

plt.figure(figsize=(18, 10))

plt.imshow(grid)

plt.yticks(delivery['overs'].unique(), list(range(1, 21)))
plt.xticks(np.arange(0, 6), list(range(1, 7)))

plt.colorbar()

plt.show()




# Multiple Heatmaps using subplots
#=================================

fig, ax = plt.subplots(1, 2, figsize=(18,8))

im1 = ax[0].imshow(grid, cmap='viridis')
ax[0].set_title('Heatmap - Viridis')

im2 = ax[1].imshow(grid, cmap='hot')
ax[1].set_title('Heatmap - Hot')

fig.colorbar(im1, ax=ax[0])
fig.colorbar(im2, ax=ax[1])

plt.show()



# Four Heatmaps
#===============

fig, ax = plt.subplots(2,2, figsize=(18,10))

ax[0,0].imshow(grid, cmap='viridis')
ax[0,0].set_title('Viridis')

ax[0,1].imshow(grid, cmap='hot')
ax[0,1].set_title('Hot')

ax[1,0].imshow(grid, cmap='coolwarm')
ax[1,0].set_title('Coolwarm')

ax[1,1].imshow(grid, cmap='plasma')
ax[1,1].set_title('Plasma')

plt.show()



# Multiple Heatmaps using add_subplot
#====================================

fig = plt.figure(figsize=(18,8))

ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

ax1.imshow(grid, cmap='viridis')
ax1.set_title('Heatmap 1')

ax2.imshow(grid, cmap='hot')
ax2.set_title('Heatmap 2')

plt.show()




# Multiple Heatmaps using subplot
#================================

plt.figure(figsize=(18,8))

plt.subplot(1,2,1)
plt.imshow(grid, cmap='viridis')
plt.title('Heatmap 1')

plt.subplot(1,2,2)
plt.imshow(grid, cmap='hot')
plt.title('Heatmap 2')

plt.show()





# Heatmap with labels
#=====================

fig, ax = plt.subplots(figsize=(12,8))

im = ax.imshow(grid, cmap='viridis')

ax.set_xticks(np.arange(6))
ax.set_xticklabels(range(1,7))

ax.set_yticks(np.arange(20))
ax.set_yticklabels(range(1,21))

ax.set_xlabel('Ball Number')
ax.set_ylabel('Over')
ax.set_title('IPL Sixes Heatmap')

fig.colorbar(im)

plt.show()





# Shared colorbar heatmaps
#=========================

fig, ax = plt.subplots(1,3, figsize=(18,6))

im = ax[0].imshow(grid, cmap='viridis')
ax[0].set_title('Viridis')

ax[1].imshow(grid, cmap='plasma')
ax[1].set_title('Plasma')

ax[2].imshow(grid, cmap='inferno')
ax[2].set_title('Inferno')

fig.colorbar(im, ax=ax)

plt.show()