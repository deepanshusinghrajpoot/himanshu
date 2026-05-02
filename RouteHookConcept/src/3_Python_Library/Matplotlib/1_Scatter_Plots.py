
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



import os


path = os.path.dirname(__file__)

path_file_batter = os.path.join(path, '../Pandas/1_Dataset/batter.csv')

batter = pd.read_csv(path_file_batter)


print(batter.info())

'''
<class 'pandas.DataFrame'>
RangeIndex: 605 entries, 0 to 604
Data columns (total 4 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   batter       605 non-null    str    
 1   runs         605 non-null    int64  
 2   avg          572 non-null    float64
 3   strike_rate  605 non-null    float64
dtypes: float64(2), int64(1), str(1)
memory usage: 19.0 KB
None
'''

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






# Scatter Plots
#===============

# gpt give perfect interview spoken diffinition

# Scateter plots use for Bivariate Analysis :- mean scatter plot apply on two column
# numerical(first column) -> numerical(second column)

# Use cases - find correlation etween two quantity


# plt.scatter simple function
#-----------------------------

# this is slower way to plot scatter plot

x = np.linspace(-10, 10, 50)
y = 10*x + 3 + np.random.randint(0, 300, 50)


plt.scatter(x, y)
plt.show()



# plt.scatter on pandas data
#----------------------------

batter_1 = batter.head(50)

plt.scatter(batter_1['avg'], batter_1['strike_rate'], color='green')

plt.title('Avg and SR analysis of Top 50 Batsman')
plt.xlabel('Average')
plt.ylabel('Strike rate')

plt.show()



# all attribute and function apply on this graph : gpt give table all attribute and method what role of that attribute and method




# size : gpt give perfect interview spoken diffinition
#........

tips = sns.load_dataset('tips')

print(tips)
'''
     total_bill   tip     sex smoker   day    time  size
0         16.99  1.01  Female     No   Sun  Dinner     2
1         10.34  1.66    Male     No   Sun  Dinner     3
2         21.01  3.50    Male     No   Sun  Dinner     3
3         23.68  3.31    Male     No   Sun  Dinner     2
4         24.59  3.61  Female     No   Sun  Dinner     4
..          ...   ...     ...    ...   ...     ...   ...
239       29.03  5.92    Male     No   Sat  Dinner     3
240       27.18  2.00  Female    Yes   Sat  Dinner     2
241       22.67  2.00    Male    Yes   Sat  Dinner     2
242       17.82  1.75    Male     No   Sat  Dinner     2
243       18.78  3.00  Female     No  Thur  Dinner     2

[244 rows x 7 columns]
'''


plt.scatter(tips['total_bill'], tips['tip'], s=tips['size']*20)
plt.show()



# scattering using plt.plot
#---------------------------

# we can also draw scattering using plt.plot
# this is faster way to plot scatter plot

plt.plot(tips['total_bill'], tips['tip'], 'O')













# *************************************************************************





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











# *****************************************************************************************


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


# Annotation
#==============

# gpt give perfect interview spoken diffinition

# eg:

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

plt.scatter(x, y)

plt.text(1, 5, 'Point 1', fontdict={'size':20, 'color':'pink'})
plt.text(2, 6, 'Point 2', fontdict={'size':5, 'color':'red'})
plt.text(3, 7, 'Point 3', fontdict={'size':10, 'color':'yellow'})
plt.text(4, 8, 'Point 4', fontdict={'size':15, 'color':'blue'})

plt.show()




# eg : 2


plt.figure(figsize=(18, 10))


plt.scatter(batter_df['avg'], batter_df['strike_rate'])

for i in range(batter_df.shape[0]):
    plt.text(batter_df['avg'].values[i], batter_df['strike_rate'].values[i], batter_df['batter'].values[i])


plt.show()



# s (size)
#----------

plt.figure(figsize=(18, 10))

plt.scatter(batter_df['avg'], batter_df['strike_rate'], s=batter_df['runs'])

for i in range(batter_df.shape[0]):
    plt.text(batter_df['avg'].values[i], batter_df['strike_rate'].values[i], batter_df['batter'].values[i])


plt.show()
