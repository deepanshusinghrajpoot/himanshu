

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





# Contour Plots
#================

# Contour graph repersent 3D plot into 2D


# contour
#---------

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)


xx, yy = np.meshgrid(x, y)


print(xx.shape)
print(yy.shape)
'''
(100, 100)
(100, 100)
'''

z = xx**2 + yy**2
print(z.shape)
'''
(100, 100)
'''



fig = plt.figure(figsize=(12, 6))

ax = plt.subplot()

p = ax.contour(xx, yy, z, cmap='viridis')
fig.colorbar(p)

plt.show()






# contourf
#----------

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)


xx, yy = np.meshgrid(x, y)


print(xx.shape)
print(yy.shape)
'''
(100, 100)
(100, 100)
'''

z = xx**2 + yy**2
print(z.shape)
'''
(100, 100)
'''



fig = plt.figure(figsize=(12, 6))

ax = plt.subplot()

p = ax.contourf(xx, yy, z, cmap='viridis')
fig.colorbar(p)

plt.show()








# ============= ALL COMMON WAYS to create Multiple Contour / Contourf plots (2D representation of 3D data) ======================================


# 1️⃣ Using plt.subplots() (Most Common Way)
#--------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

xx, yy = np.meshgrid(x, y)

z1 = xx**2 + yy**2
z2 = np.sin(xx) * np.cos(yy)

fig, ax = plt.subplots(1, 2, figsize=(14,6))

p1 = ax[0].contour(xx, yy, z1, cmap='viridis')
p2 = ax[1].contourf(xx, yy, z2, cmap='plasma')

fig.colorbar(p1, ax=ax[0])
fig.colorbar(p2, ax=ax[1])

plt.show()






# 2️⃣ Using plt.figure() + add_subplot()
#---------------------------------------

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(14,6))

ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

p1 = ax1.contour(xx, yy, z1, cmap='viridis')
p2 = ax2.contourf(xx, yy, z2, cmap='plasma')

fig.colorbar(p1, ax=ax1)
fig.colorbar(p2, ax=ax2)

plt.show()




# 3️⃣ Using plt.subplot()
#-------------------------

fig = plt.figure(figsize=(14,6))

ax1 = plt.subplot(1,2,1)
ax2 = plt.subplot(1,2,2)

ax1.contour(xx, yy, z1, cmap='viridis')
ax2.contourf(xx, yy, z2, cmap='plasma')

plt.show()




# Creating 4 Contour Graphs
#================================


fig, ax = plt.subplots(2,2, figsize=(12,10))

ax[0,0].contour(xx, yy, z1, cmap='viridis')
ax[0,1].contourf(xx, yy, z2, cmap='plasma')
ax[1,0].contour(xx, yy, np.sin(xx)+np.cos(yy), cmap='coolwarm')
ax[1,1].contourf(xx, yy, np.sqrt(xx**2+yy**2), cmap='inferno')

plt.show()





# Contour + Contourf Together
#+============================

fig, ax = plt.subplots(1,2, figsize=(12,6))

p1 = ax[0].contour(xx, yy, z1, cmap='viridis')
p2 = ax[1].contourf(xx, yy, z1, cmap='viridis')

fig.colorbar(p1, ax=ax[0])
fig.colorbar(p2, ax=ax[1])

plt.show()



# Contour Plot with Levels (Advanced)
# ===================================

'''
| Plot         | Meaning                    |
| ------------ | -------------------------- |
| `contour()`  | Draws only contour lines   |
| `contourf()` | Draws filled color regions |

'''