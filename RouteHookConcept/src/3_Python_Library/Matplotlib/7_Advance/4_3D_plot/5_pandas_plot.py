


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


import os


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






# Pandas Plot()
#==============

# Hellow gpt explain 


# gpt give all common attribute with what role how to use in table so we are learn easy 



# 📊 Common pandas.plot() Attributes
#-------------------------------------

'''
| Attribute           | Role / Meaning                | How to Use                                              | Example                |
| ------------------- | ----------------------------- | ------------------------------------------------------- | ---------------------- |
| `kind`              | Type of plot                  | `'line'`, `'bar'`, `'hist'`, `'pie'`, `'scatter'`, etc. | `df.plot(kind='bar')`  |
| `title`             | Title of the graph            | Adds heading at top                                     | `title='Sales Report'` |
| `xlabel`            | Label for X-axis              | Describes X-axis                                        | `xlabel='Year'`        |
| `ylabel`            | Label for Y-axis              | Describes Y-axis                                        | `ylabel='Revenue'`     |
| `figsize`           | Size of figure                | `(width, height)` in inches                             | `figsize=(10,6)`       |
| `color`             | Color of plot                 | Single or list of colors                                | `color='red'`          |
| `legend`            | Show legend                   | `True` or `False`                                       | `legend=True`          |
| `grid`              | Show grid lines               | `True` or `False`                                       | `grid=True`            |
| `marker`            | Marker style for line/scatter | `'o'`, `'+'`, `'*'`                                     | `marker='o'`           |
| `linestyle`         | Line style                    | `'--'`, `'-.'`, `':'`                                   | `linestyle='--'`       |
| `alpha`             | Transparency                  | Value between `0–1`                                     | `alpha=0.6`            |
| `stacked`           | Stacked bars                  | Used for bar plots                                      | `stacked=True`         |
| `bins`              | Number of bins in histogram   | Controls histogram grouping                             | `bins=20`              |
| `rot`               | Rotate x labels               | Angle in degrees                                        | `rot=45`               |
| `colormap` / `cmap` | Color theme                   | `'viridis'`, `'plasma'`, etc.                           | `colormap='viridis'`   |
| `s`                 | Size of scatter points        | Column or number                                        | `s='size'`             |
| `c`                 | Scatter color column          | Categorical coloring                                    | `c='sex'`              |

'''


# On a series
#-------------


s = pd.Series([1, 2, 3, 4, 5, 6, 7])


# 1️⃣ Series Pie Plot (With All Attributes)
#..........................................

s.plot(
    kind='pie',
    title='Distribution of Values',
    ylabel='',
    figsize=(6,6),
    autopct='%1.1f%%',
    legend=False,
    colormap='viridis'
)
plt.show()


# 2️⃣ Histogram
#...............

s.plot(
    kind='hist',
    bins=10,
    title='Histogram of Values',
    xlabel='Value',
    ylabel='Frequency',
    figsize=(8,5),
    color='skyblue',
    grid=True
)
plt.show()


# 3️⃣ Line Plot (Series)
#........................

s.plot(
    kind='line',
    title='Line Plot of Series',
    xlabel='Index',
    ylabel='Value',
    figsize=(8,5),
    marker='o',
    linestyle='--',
    grid=True
)
plt.show()



# 4️⃣ Scatter Plot (Tips Dataset)
#---------------------------------

tips['size'] = tips['size']*100

tips.plot(
    kind='scatter',
    x='total_bill',
    y='tip',
    title='Cost Analysis',
    xlabel='Total Bill',
    ylabel='Tip',
    figsize=(10,6),
    marker='+',
    s='size',
    c='sex',
    colormap='viridis',
    alpha=0.7
)
plt.show()




# 5️⃣ Line Plot for Column
#..........................

tips['total_bill'].plot(
    kind='line',
    title='Total Bill Trend',
    xlabel='Index',
    ylabel='Total Bill',
    figsize=(8,5),
    marker='o',
    color='green',
    grid=True
)
plt.show()




# 6️⃣ DataFrame Line Plot (Multiple Columns)
#...........................................

tips.plot(
    kind='line',
    title='Tips Dataset Line Plot',
    xlabel='Index',
    ylabel='Values',
    figsize=(10,6),
    grid=True,
    legend=True
)
plt.show()



# bar chart -> single -> horizontal -> multiple
#-----------------------------------------------

path = os.path.dirname(__file__)

path_file_bastman_season_record = os.path.join(path, '../../../Pandas/1_Dataset/batsman_season_record.csv')

temp = pd.read_csv(path_file_bastman_season_record)



# 1️⃣ Single Bar Chart
#......................

temp.plot(
    kind='bar',
    title='Batsman Season Record',
    xlabel='Season',
    ylabel='Runs',
    figsize=(10,6),
    color='skyblue',
    grid=True,
    rot=45
)

plt.show()




# 2️⃣ Horizontal Bar Chart
#.........................

temp.plot(
    kind='barh',
    title='Batsman Season Record (Horizontal)',
    xlabel='Runs',
    ylabel='Season',
    figsize=(10,6),
    color='orange',
    grid=True
)

plt.show()


# 3️⃣ Multiple Bar Chart
#.......................

temp.plot(
    kind='bar',
    title='Batsman Performance Comparison',
    xlabel='Season',
    ylabel='Runs',
    figsize=(12,6),
    colormap='viridis',
    grid=True,
    rot=45
)

plt.show()




# 8️⃣ Stacked Bar Chart
#-----------------------

temp.plot(
    kind='bar',
    stacked=True,
    title='Stacked Batsman Runs',
    xlabel='Season',
    ylabel='Runs',
    figsize=(12,6),
    colormap='plasma',
    grid=True
)
plt.show()


# 9️⃣ Histogram (DataFrame)
#--------------------------

temp.plot(
    kind='hist',
    bins=15,
    title='Distribution of Runs',
    xlabel='Runs',
    ylabel='Frequency',
    figsize=(10,6),
    alpha=0.6,
    grid=True
)
plt.show()



# 🔟 Pie Chart (DataFrame)
#--------------------------

df = pd.DataFrame(
    {
        'batsman':['Dhawan', 'Rohit', 'Kohli', 'SKY', 'Pandya', 'Pant'],
        'match1':[120, 90, 35, 45, 12, 10],
        'match2':[0, 1, 123, 130, 34, 45],
        'match3':[50, 24, 145, 45, 10, 90]
    }
)

print(df)
'''
  batsman  match1  match2  match3
0  Dhawan     120       0      50
1   Rohit      90       1      24
2   Kohli      35     123     145
3     SKY      45     130      45
4  Pandya      12      34      10
5    Pant      10      45      90
'''


df.set_index('batsman').plot(
    kind='pie',
    subplots=True,
    figsize=(12,8),
    autopct='%1.1f%%',
    title='Runs Distribution per Match'
)
plt.show()



# ⭐ Most Important kind Types
#==============================

'''
| Kind      | Graph             |
| --------- | ----------------- |
| `line`    | Line graph        |
| `bar`     | Vertical bar      |
| `barh`    | Horizontal bar    |
| `hist`    | Histogram         |
| `box`     | Boxplot           |
| `kde`     | Density curve     |
| `area`    | Area chart        |
| `pie`     | Pie chart         |
| `scatter` | Scatter plot      |
| `hexbin`  | Hexagonal scatter |

'''