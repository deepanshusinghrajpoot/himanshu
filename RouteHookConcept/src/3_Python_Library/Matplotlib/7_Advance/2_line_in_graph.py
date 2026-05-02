

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


batter_df = batter.head(100).sample(25, random_state=5)


# Horizontal and Vertical lines in graph 
#----------------------------------------

# axhline(point, color='')
# axvline(point, color='')

plt.figure(figsize=(18, 10))

plt.scatter(batter_df['avg'], batter_df['strike_rate'], s=batter_df['runs'])

plt.axhline(140, color='green')
plt.axhline(130, color='red')
plt.axvline(30, color='red')


for i in range(batter_df.shape[0]):
    plt.text(batter_df['avg'].values[i], batter_df['strike_rate'].values[i], batter_df['batter'].values[i])


plt.show()