
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


import os





# Pivot Table
#==============

# The pivot table takes simple column-wise data as input, and groups the entires into a two dimentional table that provide a multidimentional
# summmarization of the data


df = sns.load_dataset('tips')
print(df)

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




# Ques : Find out total avg bill according to gender
#....................................................

print(df.groupby('sex')['total_bill'].mean())
'''
sex
Male      20.744076
Female    18.056897
Name: total_bill, dtype: float64
'''


# Ques : Find out total avg bill according to gender and smoker
#..............................................................

print(df.groupby(['sex', 'smoker'])[['total_bill']].mean())
'''
sex    smoker
Male   Yes      22.284500
       No       19.791237
Female Yes      17.977879
       No       18.105185
'''


print(df.groupby(['sex', 'smoker'])[['total_bill']].mean().unstack())

'''
       total_bill
smoker        Yes         No
sex
Male    22.284500  19.791237
Female  17.977879  18.105185
'''



# pivot_table
#--------------

# In pivot_table by default aggfunc='mean'

print(df.pivot_table(index='sex', columns='smoker', values='total_bill'))

'''
smoker        Yes         No
sex
Male    22.284500  19.791237
Female  17.977879  18.105185
'''



# sum

print(df.pivot_table(index='sex', columns='smoker', values='total_bill', aggfunc='sum'))

'''
smoker      Yes       No
sex
Male    1337.07  1919.75
Female   593.27   977.68
'''


# Note: When we not give values column then it perform operation automaticaly on every numerical collumns
#---------------------------------------------------------------------------------------------------------

print(df.pivot_table(index='sex', columns='smoker', values=['total_bill', 'tip', 'size']))

'''
            size                 tip           total_bill
smoker       Yes        No       Yes        No        Yes         No
sex
Male    2.500000  2.711340  3.051167  3.113402  22.284500  19.791237
Female  2.242424  2.592593  2.931515  2.773519  17.977879  18.105185
'''



print(df)
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



# multi dimentional analysis
#----------------------------

print(df.pivot_table(index=['sex', 'smoker'], columns=['day', 'time'], values=['total_bill', 'tip']))
'''
                    tip                                         total_bill
day                Thur          Fri              Sat       Sun       Thur               Fri                Sat        Sun
time              Lunch Dinner Lunch Dinner    Dinner    Dinner      Lunch Dinner      Lunch  Dinner     Dinner     Dinner
sex    smoker
Male   Yes     3.058000    NaN  1.90  3.246  2.879259  3.521333  19.171000    NaN  11.386667  25.892  21.837778  26.141333
       No      2.941500    NaN   NaN  2.500  3.256563  3.115349  18.486500    NaN        NaN  17.475  19.929063  20.403256
Female Yes     2.990000    NaN  2.66  2.700  2.868667  3.500000  19.218571    NaN  13.260000  12.200  20.266667  16.540000
       No      2.437083    3.0  3.00  3.250  2.724615  3.329286  15.899167  18.78  15.980000  22.750  19.003846  20.824286
'''



print(df.pivot_table(index=['sex', 'smoker'], columns=['day', 'time'], values=['total_bill', 'tip'], aggfunc={'total_bill':'sum', 'tip':'mean'}))
'''
                    tip                                         total_bill
day                Thur          Fri              Sat       Sun       Thur           Fri             Sat     Sun
time              Lunch Dinner Lunch Dinner    Dinner    Dinner      Lunch Dinner  Lunch  Dinner  Dinner  Dinner
sex    smoker
Male   Yes     3.058000    NaN  1.90  3.246  2.879259  3.521333     191.71    NaN  34.16  129.46  589.62  392.12
       No      2.941500    NaN   NaN  2.500  3.256563  3.115349     369.73    NaN    NaN   34.95  637.73  877.34
Female Yes     2.990000    NaN  2.66  2.700  2.868667  3.500000     134.53    NaN  39.78   48.80  304.00   66.16
       No      2.437083    3.0  3.00  3.250  2.724615  3.329286     381.58  18.78  15.98   22.75  247.05  291.54
'''




# margin
#--------

print(df.pivot_table(index='sex', columns='smoker', values='total_bill', margins=True))
'''
smoker        Yes         No        All
sex
Male    22.284500  19.791237  20.744076
Female  17.977879  18.105185  18.056897
All     20.756344  19.188278  19.785943
'''










# plotting graphs
#-----------------

path_dir = os.path.dirname(__file__)
path_file_expense = os.path.join(path_dir, '../1_Dataset/expense_data.csv')

expense_df = pd.read_csv(path_file_expense)

print(expense_df)
'''
                 Date               Account        Category  Subcategory                Note     INR Income/Expense  Note.1  Amount Currency  Account.1
0      3/2/2022 10:11  CUB - online payment            Food          NaN             Brownie    50.0        Expense     NaN    50.0      INR       50.0      
1      3/2/2022 10:11  CUB - online payment           Other          NaN    To lended people   300.0        Expense     NaN   300.0      INR      300.0      
2      3/1/2022 19:50  CUB - online payment            Food          NaN              Dinner    78.0        Expense     NaN    78.0      INR       78.0      
3      3/1/2022 18:56  CUB - online payment  Transportation          NaN               Metro    30.0        Expense     NaN    30.0      INR       30.0      
4      3/1/2022 18:22  CUB - online payment            Food          NaN              Snacks    67.0        Expense     NaN    67.0      INR       67.0      
..                ...                   ...             ...          ...                 ...     ...            ...     ...     ...      ...        ...      
272  11/22/2021 14:16  CUB - online payment            Food          NaN              Dinner    90.0        Expense     NaN    90.0      INR       90.0      
273  11/22/2021 14:16  CUB - online payment            Food          NaN  Lunch with company    97.0        Expense     NaN    97.0      INR       97.0      
274  11/21/2021 17:07  CUB - online payment  Transportation          NaN              Rapido   130.0        Expense     NaN   130.0      INR      130.0      
275  11/21/2021 15:50  CUB - online payment            Food          NaN               Lunch   875.0        Expense     NaN   875.0      INR      875.0      
276  11/21/2021 13:30  CUB - online payment           Other          NaN       Got from gobi  2000.0         Income     NaN  2000.0      INR     2000.0      

[277 rows x 11 columns]
'''

print(expense_df.info())
'''
<class 'pandas.DataFrame'>
RangeIndex: 277 entries, 0 to 276
Data columns (total 11 columns):
 #   Column          Non-Null Count  Dtype
---  ------          --------------  -----
 0   Date            277 non-null    str
 1   Account         277 non-null    str
 2   Category        277 non-null    str
 3   Subcategory     0 non-null      float64
 4   Note            273 non-null    str
 5   INR             277 non-null    float64
 6   Income/Expense  277 non-null    str
 7   Note.1          0 non-null      float64
 8   Amount          277 non-null    float64
 9   Currency        277 non-null    str
 10  Account.1       277 non-null    float64
dtypes: float64(5), str(6)
memory usage: 23.9 KB
None
'''

expense_df['Date'] = pd.to_datetime(expense_df['Date'])

print(expense_df.info())
'''
<class 'pandas.DataFrame'>
RangeIndex: 277 entries, 0 to 276
Data columns (total 11 columns):
 #   Column          Non-Null Count  Dtype
---  ------          --------------  -----
 0   Date            277 non-null    datetime64[us]
 1   Account         277 non-null    str
 2   Category        277 non-null    str
 3   Subcategory     0 non-null      float64
 4   Note            273 non-null    str
 5   INR             277 non-null    float64
 6   Income/Expense  277 non-null    str
 7   Note.1          0 non-null      float64
 8   Amount          277 non-null    float64
 9   Currency        277 non-null    str
 10  Account.1       277 non-null    float64
dtypes: datetime64[us](1), float64(5), str(5)
memory usage: 23.9 KB
None
'''

expense_df['month'] = expense_df['Date'].dt.month_name()

print(expense_df.info())
'''
<class 'pandas.DataFrame'>
RangeIndex: 277 entries, 0 to 276
Data columns (total 12 columns):
 #   Column          Non-Null Count  Dtype
---  ------          --------------  -----
 0   Date            277 non-null    datetime64[us]
 1   Account         277 non-null    str
 2   Category        277 non-null    str
 3   Subcategory     0 non-null      float64
 4   Note            273 non-null    str
 5   INR             277 non-null    float64
 6   Income/Expense  277 non-null    str
 7   Note.1          0 non-null      float64
 8   Amount          277 non-null    float64
 9   Currency        277 non-null    str
 10  Account.1       277 non-null    float64
 11  month           277 non-null    str
dtypes: datetime64[us](1), float64(5), str(6)
memory usage: 26.1 KB
None
'''



expense_df.pivot_table(index='month', columns='Category', values='INR', aggfunc='sum', fill_value=0).plot()
plt.show()

expense_df.pivot_table(index='month', columns='Income/Expense', values='INR', aggfunc='sum', fill_value=0).plot()
plt.show()

expense_df.pivot_table(index='month', columns='Account', values='INR', aggfunc='sum', fill_value=0).plot()
plt.show()