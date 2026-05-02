



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





# 3D Line Plots
#==============


x = [0, 1, 5, 25]
y = [0, 10, 13, 0]
z = [0, 13, 20, 45]



fig = plt.figure()


ax = plt.subplot(projection='3d')



ax.scatter(x, y, z, s=[100, 100, 100, 100])

ax.plot3D(x, y, z, color='red')

plt.show()




# ALL COMMON WAYS to create multiple 3D Line
#============================================


# Multiple 3D Graphs using subplots()
#====================================

import matplotlib.pyplot as plt

x = [0, 1, 5, 25]
y = [0, 10, 13, 0]
z = [0, 13, 20, 45]

fig, ax = plt.subplots(2, 2, figsize=(12,8),
                       subplot_kw={'projection':'3d'})

# Graph 1
ax[0,0].scatter(x, y, z, s=100)
ax[0,0].plot3D(x, y, z, color='red')
ax[0,0].set_title("Graph 1")

# Graph 2
ax[0,1].scatter(y, x, z, s=100)
ax[0,1].plot3D(y, x, z, color='blue')
ax[0,1].set_title("Graph 2")

# Graph 3
ax[1,0].scatter(z, y, x, s=100)
ax[1,0].plot3D(z, y, x, color='green')
ax[1,0].set_title("Graph 3")

# Graph 4
ax[1,1].scatter(x, z, y, s=100)
ax[1,1].plot3D(x, z, y, color='purple')
ax[1,1].set_title("Graph 4")

plt.subplots_adjust(hspace=0.4, wspace=0.3)

plt.show()





# Multiple 3D Graphs using add_subplot()
#=======================================

import matplotlib.pyplot as plt

x = [0, 1, 5, 25]
y = [0, 10, 13, 0]
z = [0, 13, 20, 45]

fig = plt.figure(figsize=(12,8))

ax1 = fig.add_subplot(2,2,1, projection='3d')
ax1.scatter(x, y, z, s=100)
ax1.plot3D(x, y, z, color='red')

ax2 = fig.add_subplot(2,2,2, projection='3d')
ax2.scatter(y, x, z, s=100)
ax2.plot3D(y, x, z, color='blue')

ax3 = fig.add_subplot(2,2,3, projection='3d')
ax3.scatter(z, y, x, s=100)
ax3.plot3D(z, y, x, color='green')

ax4 = fig.add_subplot(2,2,4, projection='3d')
ax4.scatter(x, z, y, s=100)
ax4.plot3D(x, z, y, color='purple')

plt.subplots_adjust(hspace=0.4, wspace=0.3)

plt.show()





# Multiple 3D Graphs using subplot()
#===================================

import matplotlib.pyplot as plt

x = [0, 1, 5, 25]
y = [0, 10, 13, 0]
z = [0, 13, 20, 45]

plt.figure(figsize=(12,8))

ax1 = plt.subplot(2,2,1, projection='3d')
ax1.scatter(x, y, z)
ax1.plot3D(x, y, z)

ax2 = plt.subplot(2,2,2, projection='3d')
ax2.scatter(y, x, z)
ax2.plot3D(y, x, z)

ax3 = plt.subplot(2,2,3, projection='3d')
ax3.scatter(z, y, x)
ax3.plot3D(z, y, x)

ax4 = plt.subplot(2,2,4, projection='3d')
ax4.scatter(x, z, y)
ax4.plot3D(x, z, y)

plt.show()