
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


import os



path = os.path.dirname(__file__)

path_file_iris = os.path.join(path, '../../Pandas/1_Dataset/iris.csv')


iris = pd.read_csv(path_file_iris)

print(iris)
'''
      Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm         Species
0      1            5.1           3.5            1.4           0.2     Iris-setosa
1      2            4.9           3.0            1.4           0.2     Iris-setosa
2      3            4.7           3.2            1.3           0.2     Iris-setosa
3      4            4.6           3.1            1.5           0.2     Iris-setosa
4      5            5.0           3.6            1.4           0.2     Iris-setosa
..   ...            ...           ...            ...           ...             ...
145  146            6.7           3.0            5.2           2.3  Iris-virginica
146  147            6.3           2.5            5.0           1.9  Iris-virginica
147  148            6.5           3.0            5.2           2.0  Iris-virginica
148  149            6.2           3.4            5.4           2.3  Iris-virginica
149  150            5.9           3.0            5.1           1.8  Iris-virginica

[150 rows x 6 columns]
'''


print(iris.sample(5))
'''
      Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm          Species
54    55            6.5           2.8            4.6           1.5  Iris-versicolor
107  108            7.3           2.9            6.3           1.8   Iris-virginica
28    29            5.2           3.4            1.4           0.2      Iris-setosa
14    15            5.8           4.0            1.2           0.2      Iris-setosa
84    85            5.4           3.0            4.5           1.5  Iris-versicolor
'''





# Scatter color encoding
#========================


plt.scatter(iris['SepalLengthCm'], iris['PetalLengthCm'])

plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')

plt.show()





iris['Species_num'] = iris['Species'].replace({'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2})

print(iris.sample(5))
'''
      Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm         Species Species_num
124  125            6.7           3.3            5.7           2.1  Iris-virginica           2
118  119            7.7           2.6            6.9           2.3  Iris-virginica           2
145  146            6.7           3.0            5.2           2.3  Iris-virginica           2
6      7            4.6           3.4            1.4           0.3     Iris-setosa           0
33    34            5.5           4.2            1.4           0.2     Iris-setosa           0
'''


# c
#...

plt.scatter(iris['SepalLengthCm'], iris['PetalLengthCm'], c=iris['Species_num'])

plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')

plt.show()



# cmap
#......

# documentation matplotlip.cmap


plt.scatter(iris['SepalLengthCm'], iris['PetalLengthCm'], c=iris['Species_num'], cmap='jet')

plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')

plt.show()


# alpha(opacity 0.0 - 0.7)
#.........................

plt.scatter(iris['SepalLengthCm'], iris['PetalLengthCm'], c=iris['Species_num'], cmap='jet', alpha=0.7)

plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')

plt.show()




# plt.colorbar()
#----------------

plt.scatter(iris['SepalLengthCm'], iris['PetalLengthCm'], c=iris['Species_num'], cmap='jet', alpha=0.7)

plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')

plt.colorbar()

plt.show()







# plot size
#=============

# syntax :- plt.figure(figsize=(3, 1))

plt.figure(figsize=(15, 7))

plt.scatter(iris['SepalLengthCm'], iris['PetalLengthCm'], c=iris['Species_num'], cmap='jet', alpha=0.7)

plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')

plt.colorbar()

plt.show()





