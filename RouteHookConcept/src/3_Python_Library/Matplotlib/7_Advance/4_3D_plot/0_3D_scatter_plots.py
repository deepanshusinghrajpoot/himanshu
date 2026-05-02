


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


import os


path = os.path.dirname(__file__)

path_file_batter = os.path.join(path, '../../../Pandas/1_Dataset/batter.csv')


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





# 3D Scatter Plots
#==================



fig = plt.figure(figsize=(18, 10))


ax = plt.subplot(projection='3d')



ax.scatter3D(batter['runs'], batter['avg'], batter['strike_rate'], color='blue')

ax.set_title('IPL batsman analysis', fontsize=18, color='darkred')

ax.set_xlabel('Runs', fontsize=14, color='brown')
ax.set_ylabel('Avg', fontsize=14, color='brown')
ax.set_zlabel('Strik rate', fontsize=14, color='brown')


plt.show()





# Multiple 3D Scatter Plots
#===========================

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(18,10))

# Graph 1
#---------
ax1 = fig.add_subplot(2,2,1, projection='3d')
ax1.scatter(batter['runs'], batter['avg'], batter['strike_rate'], color='blue')

ax1.set_title('Runs vs Avg vs Strike Rate')
ax1.set_xlabel('Runs')
ax1.set_ylabel('Avg')
ax1.set_zlabel('Strike Rate')


# Graph 2
#---------
ax2 = fig.add_subplot(2,2,2, projection='3d')
ax2.scatter(batter['avg'], batter['runs'], batter['strike_rate'], color='green')

ax2.set_title('Avg vs Runs vs Strike Rate')
ax2.set_xlabel('Avg')
ax2.set_ylabel('Runs')
ax2.set_zlabel('Strike Rate')


# Graph 3
#---------
ax3 = fig.add_subplot(2,2,3, projection='3d')
ax3.scatter(batter['strike_rate'], batter['runs'], batter['avg'], color='red')

ax3.set_title('Strike Rate vs Runs vs Avg')
ax3.set_xlabel('Strike Rate')
ax3.set_ylabel('Runs')
ax3.set_zlabel('Avg')


# Graph 4
#---------
ax4 = fig.add_subplot(2,2,4, projection='3d')
ax4.scatter(batter['runs'], batter['strike_rate'], batter['avg'], color='purple')

ax4.set_title('Runs vs Strike Rate vs Avg')
ax4.set_xlabel('Runs')
ax4.set_ylabel('Strike Rate')
ax4.set_zlabel('Avg')


# spacing
plt.subplots_adjust(hspace=0.3, wspace=0.3)

plt.show()






# ======================== ALL WAYS to create multiple 3D graphs in Matplotlib =====================================

# Multiple 3D Scatter Plots using subplots()
#============================================

import matplotlib.pyplot as plt

fig, ax = plt.subplots(2,2, figsize=(18,10), subplot_kw={'projection':'3d'})

ax[0,0].scatter(batter['runs'], batter['avg'], batter['strike_rate'], color='blue')
ax[0,0].set_title('Runs vs Avg vs Strike Rate')

ax[0,1].scatter(batter['avg'], batter['runs'], batter['strike_rate'], color='green')
ax[0,1].set_title('Avg vs Runs vs Strike Rate')

ax[1,0].scatter(batter['strike_rate'], batter['runs'], batter['avg'], color='red')
ax[1,0].set_title('Strike Rate vs Runs vs Avg')

ax[1,1].scatter(batter['runs'], batter['strike_rate'], batter['avg'], color='purple')
ax[1,1].set_title('Runs vs Strike Rate vs Avg')

plt.subplots_adjust(hspace=0.4, wspace=0.3)

plt.show()




# Multiple 3D Scatter Plots using add_subplot()
#===============================================

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(18,10))

ax1 = fig.add_subplot(2,2,1, projection='3d')
ax1.scatter(batter['runs'], batter['avg'], batter['strike_rate'], color='blue')

ax2 = fig.add_subplot(2,2,2, projection='3d')
ax2.scatter(batter['avg'], batter['runs'], batter['strike_rate'], color='green')

ax3 = fig.add_subplot(2,2,3, projection='3d')
ax3.scatter(batter['strike_rate'], batter['runs'], batter['avg'], color='red')

ax4 = fig.add_subplot(2,2,4, projection='3d')
ax4.scatter(batter['runs'], batter['strike_rate'], batter['avg'], color='purple')

plt.subplots_adjust(hspace=0.4, wspace=0.3)

plt.show()






# Multiple 3D Scatter Plots using subplot()
#===========================================

import matplotlib.pyplot as plt

plt.figure(figsize=(18,10))

ax1 = plt.subplot(2,2,1, projection='3d')
ax1.scatter(batter['runs'], batter['avg'], batter['strike_rate'])

ax2 = plt.subplot(2,2,2, projection='3d')
ax2.scatter(batter['avg'], batter['runs'], batter['strike_rate'])

ax3 = plt.subplot(2,2,3, projection='3d')
ax3.scatter(batter['strike_rate'], batter['runs'], batter['avg'])

ax4 = plt.subplot(2,2,4, projection='3d')
ax4.scatter(batter['runs'], batter['strike_rate'], batter['avg'])

plt.show()