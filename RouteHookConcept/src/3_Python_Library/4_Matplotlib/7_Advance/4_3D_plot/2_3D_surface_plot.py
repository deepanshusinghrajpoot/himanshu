

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




# 3D Surface Plots
#==================


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


fig = plt.figure(figsize=(12, 8))

ax = plt.subplot(projection='3d')

p = ax.plot_surface(xx, yy, z, cmap='viridis')

fig.colorbar(p)

plt.show()






# Multiple 3D Surface Plots using subplots()
#==========================================

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

xx, yy = np.meshgrid(x, y)

z1 = xx**2 + yy**2
z2 = np.sin(xx) + np.cos(yy)
z3 = np.sqrt(xx**2 + yy**2)
z4 = np.sin(xx*yy)

fig, ax = plt.subplots(2, 2, figsize=(14,10),
                       subplot_kw={'projection':'3d'})

p1 = ax[0,0].plot_surface(xx, yy, z1, cmap='viridis')
ax[0,0].set_title("Surface 1")

p2 = ax[0,1].plot_surface(xx, yy, z2, cmap='plasma')
ax[0,1].set_title("Surface 2")

p3 = ax[1,0].plot_surface(xx, yy, z3, cmap='inferno')
ax[1,0].set_title("Surface 3")

p4 = ax[1,1].plot_surface(xx, yy, z4, cmap='cool')
ax[1,1].set_title("Surface 4")

plt.subplots_adjust(hspace=0.3, wspace=0.3)

plt.show()







# Multiple 3D Surface Plots using add_subplot()
#==============================================

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

xx, yy = np.meshgrid(x, y)

z = xx**2 + yy**2

fig = plt.figure(figsize=(14,10))

ax1 = fig.add_subplot(2,2,1, projection='3d')
ax1.plot_surface(xx, yy, z, cmap='viridis')

ax2 = fig.add_subplot(2,2,2, projection='3d')
ax2.plot_surface(xx, yy, np.sin(xx)+np.cos(yy), cmap='plasma')

ax3 = fig.add_subplot(2,2,3, projection='3d')
ax3.plot_surface(xx, yy, np.sqrt(xx**2+yy**2), cmap='cool')

ax4 = fig.add_subplot(2,2,4, projection='3d')
ax4.plot_surface(xx, yy, np.sin(xx*yy), cmap='inferno')

plt.show()







# Multiple 3D Surface Plots using subplot()
#==========================================

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

xx, yy = np.meshgrid(x, y)

z = xx**2 + yy**2

plt.figure(figsize=(14,10))

ax1 = plt.subplot(2,2,1, projection='3d')
ax1.plot_surface(xx, yy, z, cmap='viridis')

ax2 = plt.subplot(2,2,2, projection='3d')
ax2.plot_surface(xx, yy, np.sin(xx)+np.cos(yy), cmap='plasma')

ax3 = plt.subplot(2,2,3, projection='3d')
ax3.plot_surface(xx, yy, np.sqrt(xx**2+yy**2), cmap='cool')

ax4 = plt.subplot(2,2,4, projection='3d')
ax4.plot_surface(xx, yy, np.sin(xx*yy), cmap='inferno')

plt.show()