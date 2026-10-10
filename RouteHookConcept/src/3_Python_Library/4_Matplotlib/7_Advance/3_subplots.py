

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os


path = os.path.dirname(__file__)

path_file_batter = os.path.join(path, '../../Pandas/1_Dataset/batter.csv')


batter = pd.read_csv(path_file_batter)


print(batter)
'''
             batter  runs        avg  strike_rate
0           V Kohli  6634  36.251366   125.977972
1          S Dhawan  6244  34.882682   122.840842
2         DA Warner  5883  41.429577   136.401577
3         RG Sharma  5881  30.314433   126.964594
4          SK Raina  5536  32.374269   132.535312
..              ...   ...        ...          ...
600         C Nanda     0   0.000000     0.000000
601      Akash Deep     0   0.000000     0.000000
602         S Ladda     0   0.000000     0.000000
603  V Pratap Singh     0   0.000000     0.000000
604    S Lamichhane     0   0.000000     0.000000

[605 rows x 4 columns]
'''





# A diff way to plot graphs
#--------------------------

fig, ax = plt.subplots(figsize=(15, 6))

ax.scatter(batter['avg'], batter['strike_rate'])

ax.set_title('Avg V/s Strike rate')
ax.set_xlabel('Avg')
ax.set_ylabel('Strike rate')

ax.axhline(100, color='red')
ax.axvline(30, color='red')

plt.show()





# batter dataset
#----------------


fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(18, 10))

print(fig, ax)
'''
Figure(640x480) [<Axes: > <Axes: >]
'''

print(ax)
'''
[<Axes: > <Axes: >]
'''

print(fig)
'''
Figure(640x480)
'''


ax[0].scatter(batter['avg'], batter['strike_rate'], color='blue')
ax[1].scatter(batter['avg'], batter['runs'], color='green')


ax[0].set_title('Avg V/s Strike rate')
ax[0].set_xlabel('Avg')
ax[0].set_ylabel('Strick rate')

ax[1].set_title('Avg V/s Runs')
ax[1].set_xlabel('Avg')
ax[1].set_ylabel('Runs')

plt.show()






# Increase gap
#-------------
'''
| Parameter | Meaning                          |
| --------- | -------------------------------- |
| `hspace`  | Vertical space between rows      |
| `wspace`  | Horizontal space between columns |
'''



fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(18, 10))

print(fig, ax)
'''
Figure(640x480) [<Axes: > <Axes: >]
'''

print(ax)
'''
[<Axes: > <Axes: >]
'''

print(fig)
'''
Figure(640x480)
'''


ax[0].scatter(batter['avg'], batter['strike_rate'], color='blue')
ax[1].scatter(batter['avg'], batter['runs'], color='green')


ax[0].set_title('Avg V/s Strike rate')
ax[0].set_xlabel('Avg')
ax[0].set_ylabel('Strick rate')

ax[1].set_title('Avg V/s Runs')
ax[1].set_xlabel('Avg')
ax[1].set_ylabel('Runs')

plt.subplots_adjust(hspace=0.5)

plt.show()




# fontsize, color
#-----------------



fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(18, 10))

print(fig, ax)
'''
Figure(640x480) [<Axes: > <Axes: >]
'''

print(ax)
'''
[<Axes: > <Axes: >]
'''

print(fig)
'''
Figure(640x480)
'''


ax[0].scatter(batter['avg'], batter['strike_rate'], color='blue')
ax[1].scatter(batter['avg'], batter['runs'], color='green')


ax[0].set_title('Avg V/s Strike rate', fontsize=18, color='darkred')
ax[0].set_xlabel('Avg', fontsize=14, color='purple')
ax[0].set_ylabel('Strick rate', fontsize=14, color='purple')

ax[1].set_title('Avg V/s Runs', fontsize=18, color='darkred')
ax[1].set_xlabel('Avg', fontsize=14, color='brown')
ax[1].set_ylabel('Runs', fontsize=14, color='brown')

plt.subplots_adjust(hspace=0.5)

plt.show()


# sharex(boolean)
#-----------------



fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(18, 10))

print(fig, ax)
'''
Figure(640x480) [<Axes: > <Axes: >]
'''

print(ax)
'''
[<Axes: > <Axes: >]
'''

print(fig)
'''
Figure(640x480)
'''


ax[0].scatter(batter['avg'], batter['strike_rate'], color='blue')
ax[1].scatter(batter['avg'], batter['runs'], color='green')


ax[0].set_title('Avg V/s Strike rate', fontsize=18, color='darkred')
ax[0].set_ylabel('Strick rate', fontsize=14, color='purple')

ax[1].set_title('Avg V/s Runs', fontsize=18, color='darkred')
ax[1].set_xlabel('Avg', fontsize=14, color='brown')
ax[1].set_ylabel('Runs', fontsize=14, color='brown')

plt.subplots_adjust(hspace=0.2)

plt.show()






# foure graph (Second Way)(cleaner way)
#============

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(18, 10))

ax[0,0].scatter(batter['avg'], batter['strike_rate'], color='blue')
ax[0,1].scatter(batter['avg'], batter['runs'], color='green')

ax[0,0].set_title('Avg V/s Strike rate', fontsize=18, color='darkred')
ax[0,0].set_ylabel('Strike rate', fontsize=14, color='purple')
ax[0,0].set_xlabel('Avg', fontsize=14, color='purple')

ax[0,1].set_title('Avg V/s Runs', fontsize=18, color='darkred')
ax[0,1].set_ylabel('Runs', fontsize=14, color='brown')
ax[0,1].set_xlabel('Avg', fontsize=14, color='brown')


# Histogram plots
ax[1,0].hist(batter['avg'], color='blue')
ax[1,1].hist(batter['runs'], color='green')

ax[1,0].set_title('Distribution of Avg', fontsize=18, color='darkred')
ax[1,0].set_ylabel('Frequency', fontsize=14, color='purple')
ax[1,0].set_xlabel('Avg', fontsize=14, color='purple')

ax[1,1].set_title('Distribution of Runs', fontsize=18, color='darkred')
ax[1,1].set_ylabel('Frequency', fontsize=14, color='brown')
ax[1,1].set_xlabel('Runs', fontsize=14, color='brown')


# spacing
plt.subplots_adjust(hspace=0.4, wspace=0.3)

plt.show()







# Four graphs (Third way)
#========================

fig = plt.figure(figsize=(18,10))

ax1 = fig.add_subplot(2,2,1)
ax1.scatter(batter['avg'], batter['strike_rate'], color='blue')

ax2 = fig.add_subplot(2,2,2)
ax2.scatter(batter['avg'], batter['runs'], color='green')

ax3 = fig.add_subplot(2,2,3)
ax3.hist(batter['avg'], color='blue')

ax4 = fig.add_subplot(2,2,4)
ax4.hist(batter['runs'], color='green')


ax1.set_title('Avg V/s Strike rate', fontsize=18, color='darkred')
ax1.set_xlabel('Avg', fontsize=14, color='purple')
ax1.set_ylabel('Strike rate', fontsize=14, color='purple')

ax2.set_title('Avg V/s Runs', fontsize=18, color='darkred')
ax2.set_xlabel('Avg', fontsize=14, color='brown')
ax2.set_ylabel('Runs', fontsize=14, color='brown')

ax3.set_title('Distribution of Avg', fontsize=18, color='darkred')
ax3.set_xlabel('Avg', fontsize=14, color='purple')
ax3.set_ylabel('Frequency', fontsize=14, color='purple')

ax4.set_title('Distribution of Runs', fontsize=18, color='darkred')
ax4.set_xlabel('Runs', fontsize=14, color='brown')
ax4.set_ylabel('Frequency', fontsize=14, color='brown')


plt.subplots_adjust(hspace=0.4, wspace=0.3)

plt.show()




'''
🎯 Matplotlib Subplot — 3 Ways (Very Important)

| Method   | Example             | Usage            |
| -------- | ------------------- | ---------------- |
| Method 1 | `plt.subplot()`     | Simple scripts   |
| Method 2 | `plt.subplots()`    | Most common      |
| Method 3 | `fig.add_subplot()` | Advanced control |

For Data Analyst / Data Science, Method 2 (plt.subplots) is most professional.
'''