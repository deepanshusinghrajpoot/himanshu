

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px



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




gap = px.data.gapminder()


print(gap)

'''
          country continent  year  lifeExp       pop   gdpPercap iso_alpha  iso_num
0     Afghanistan      Asia  1952   28.801   8425333  779.445314       AFG        4
1     Afghanistan      Asia  1957   30.332   9240934  820.853030       AFG        4
2     Afghanistan      Asia  1962   31.997  10267083  853.100710       AFG        4
3     Afghanistan      Asia  1967   34.020  11537966  836.197138       AFG        4
4     Afghanistan      Asia  1972   36.088  13079460  739.981106       AFG        4
...           ...       ...   ...      ...       ...         ...       ...      ...
1699     Zimbabwe    Africa  1987   62.351   9216418  706.157306       ZWE      716
1700     Zimbabwe    Africa  1992   60.377  10704340  693.420786       ZWE      716
1701     Zimbabwe    Africa  1997   46.809  11404948  792.449960       ZWE      716
1702     Zimbabwe    Africa  2002   39.989  11926563  672.038623       ZWE      716
1703     Zimbabwe    Africa  2007   43.487  12311143  469.709298       ZWE      716

[1704 rows x 8 columns]
'''



temp_df = gap.pivot(index='country', columns='year', values='lifeExp')

'''
year                  1952    1957    1962    1967    1972    1977    1982    1987    1992    1997    2002    2007
country
Afghanistan         28.801  30.332  31.997  34.020  36.088  38.438  39.854  40.822  41.674  41.763  42.129  43.828
Albania             55.230  59.280  64.820  66.220  67.690  68.930  70.420  72.000  71.581  72.950  75.651  76.423
Algeria             43.077  45.685  48.303  51.407  54.518  58.014  61.368  65.799  67.744  69.152  70.994  72.301
Angola              30.015  31.999  34.000  35.985  37.928  39.483  39.942  39.906  40.647  40.963  41.003  42.731
Argentina           62.485  64.399  65.142  65.634  67.065  68.481  69.942  70.774  71.868  73.275  74.340  75.320
...                    ...     ...     ...     ...     ...     ...     ...     ...     ...     ...     ...     ...
Vietnam             40.412  42.887  45.363  47.838  50.254  55.764  58.816  62.820  67.662  70.672  73.017  74.249
West Bank and Gaza  43.160  45.671  48.127  51.631  56.532  60.765  64.406  67.046  69.718  71.096  72.370  73.422
Yemen, Rep.         32.548  33.970  35.180  36.984  39.848  44.175  49.113  52.922  55.599  58.020  60.308  62.698
Zambia              42.038  44.077  46.023  47.768  50.107  51.386  51.821  50.821  46.100  40.238  39.193  42.384
Zimbabwe            48.451  50.469  52.358  53.995  55.635  57.674  60.363  62.351  60.377  46.809  39.989  43.487

[142 rows x 12 columns]
'''





'''

(3). Matrix Plot
=====================

gpt explain imp point about matrix plot

Plots under this section
------------------------

(i). hitmap 
(ii). Clustermap

'''

# Hellow gpt give all attribute of relational plot and what is its working and how is it use and add other information if required



# Matrix Plot 
#---------------

# sns.hitmap() -> axes level method -> rectangular 
#......................................................


plt.figure(figsize=(15, 10))

sns.heatmap(data=temp_df)

plt.show()




# Attribute
#------------

# annot
#.......

temp_df_1 = gap[gap['continent'] == 'Europe'].pivot(index='country', columns='year', values='lifeExp')


plt.figure(figsize=(15, 10))

sns.heatmap(data=temp_df_1, annot=True)

plt.show()



# linewidth
#...........

plt.figure(figsize=(15, 10))

sns.heatmap(data=temp_df_1, annot=True, linewidth=0.5)

plt.show()


# cmap
#......

plt.figure(figsize=(15, 10))

sns.heatmap(data=temp_df_1, annot=True, linewidth=0.5, cmap='viridis')

plt.show()










