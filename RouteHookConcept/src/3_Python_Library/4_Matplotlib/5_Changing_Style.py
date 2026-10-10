


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



import os



path = os.path.dirname(__file__)

path_file_arr = os.path.join(path, '../Pandas/1_Dataset/big-array.npy')

arr = np.load(path_file_arr)


print(arr)
'''
[33 39 37 ... 33 30 39]
'''

print(arr.shape)
'''
(11949,)
'''




# Changing styles
#=================

print(plt.style.available)
'''
[
 'Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 
 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'petroff10', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 
 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 
 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 
 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10'
]
'''


plt.style.use('fivethirtyeight')


plt.hist(arr, bins=[0, 10, 20, 30, 40, 50, 60, 70], log=True)

plt.show()



plt.style.use('grayscale')


plt.hist(arr, bins=[0, 10, 20, 30, 40, 50, 60, 70], log=True)

plt.show()