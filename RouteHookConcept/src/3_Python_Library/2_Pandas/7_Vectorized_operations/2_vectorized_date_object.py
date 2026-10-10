
import datetime as dt

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


import os


# Vectorized Timestamp Object
#=============================


# Timestamp Object
#------------------

# Time stamps reference particular moments in time (eg : Oct 24th, 2026, at 7:00pm)


# Creating Timestamp objects
#............................

print(pd.Timestamp('2026/03/03'))
'''
2026-03-03 00:00:00
'''

print(type(pd.Timestamp('2026/03/03')))
'''
<class 'pandas.Timestamp'>
'''

# variation
#...........

print(pd.Timestamp('2026-03-03'))
'''
2026-03-03 00:00:00
'''

print(type(pd.Timestamp('2026,03,03')))
'''
<class 'pandas.Timestamp'>
'''



# only year
#..........

print(pd.Timestamp('2026'))
'''
2026-01-01 00:00:00
'''


# using text
#...........

print(pd.Timestamp('3rd march 2026'))
'''
2026-03-03 00:00:00
'''


# providng time also
#....................

print(pd.Timestamp('5th January 2023 9:21PM'))
'''
2023-01-05 21:21:00
'''




# AM and PM
#------------


# using datetime.datetime object
#................................

print(type(dt.datetime(2023, 1, 5, 9, 21, 56)))
'''
<class 'datetime.datetime'>
'''

print(dt.datetime(2023, 1, 5, 9, 21, 56))
'''
2023-01-05 09:21:56
'''


# ....................................................

x = pd.Timestamp(dt.datetime(2023, 1, 5, 9, 21, 56))
print(x)
'''
2023-01-05 09:21:56
'''

print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)
'''
2023
1
5
9
21
56
'''



# Why separate objects to handle data and time when python already has datetime functionality?
#----------------------------------------------------------------------------------------------

# syntax wise datetime is very convenient
# But the performance takes a hit while huge data. List vs Numpy Array
# The weaknesses of python's datetime format inspired the NumPy team to add a set of native time series data type to NumPy.
# The datetime64 dtype encodes dates as 64-bit integers, and thus allows array of date to be represented very compactly.


date = np.array('2015-07-04', dtype=np.datetime64)
print(date)
'''
2015-07-04
'''

print(date + np.arange(12))
'''
['2015-07-04' '2015-07-05' '2015-07-06' '2015-07-07' '2015-07-08'
 '2015-07-09' '2015-07-10' '2015-07-11' '2015-07-12' '2015-07-13'    
 '2015-07-14' '2015-07-15']
'''


# Because of the uniform type in NumPy datetime64 arrays, this type of operation can be accomplished much more quickly if we were
# working directly with Python's datetime objects, especially as array get large

# Pandas Timestamp object combines the ease-of-use of python datetime with the efficient storage and vectorized interface of numpy.datetime64

# From a group of these Timestamp objects, Pandas can construct a DatetimeIndex that can be used to index date in a series or DateFrame






# DatetimeIndex Object
#========================

# A collection of pandas timestamp

date_time = pd.DatetimeIndex(['2023/1/1', '2024/1/1', '2025/1/1', '2026/1/1'])

# from strings
#..............

print(date_time)
'''
DatetimeIndex(['2023-01-01', '2024-01-01', '2025-01-01', '2026-01-01'], dtype='datetime64[us]', freq=None)
'''


print(type(date_time))
'''
<class 'pandas.DatetimeIndex'>
'''


print(type(date_time[0]))
'''
<class 'pandas.Timestamp'>
'''



# using python datetime object
#.............................

print(pd.DatetimeIndex([dt.datetime(2023,1,1), dt.datetime(2024,1,1), dt.datetime(2025,1,1), dt.datetime(2026,1,1)]))
'''
DatetimeIndex(['2023-01-01', '2024-01-01', '2025-01-01', '2026-01-01'], dtype='datetime64[us]', freq=None)
'''


print(type(pd.DatetimeIndex([dt.datetime(2023,1,1), dt.datetime(2024,1,1), dt.datetime(2025,1,1), dt.datetime(2026,1,1)])))
'''
<class 'pandas.DatetimeIndex'>
'''


print(type(pd.DatetimeIndex([dt.datetime(2023,1,1), dt.datetime(2024,1,1), dt.datetime(2025,1,1), dt.datetime(2026,1,1)])[0]))
'''
<class 'pandas.Timestamp'>
'''



# using pd.Timestamps
#.....................


print(type(pd.DatetimeIndex([pd.Timestamp(2023,1,1), pd.Timestamp(2024,1,1), pd.Timestamp(2025,1,1), pd.Timestamp(2026,1,1)])))
'''
<class 'pandas.DatetimeIndex'>
'''


print(type(pd.DatetimeIndex([pd.Timestamp(2023,1,1), pd.Timestamp(2024,1,1), pd.Timestamp(2025,1,1), pd.Timestamp(2026,1,1)])[0]))
'''
<class 'pandas.Timestamp'>
'''




# using DatetimeIndex as series index
#--------------------------------------

dt_time = pd.DatetimeIndex([pd.Timestamp(2023,1,1), pd.Timestamp(2024,1,1), pd.Timestamp(2025,1,1), pd.Timestamp(2026,1,1)])

print(pd.Series([1, 2, 3, 4], index=dt_time))
'''
2023-01-01    1
2024-01-01    2
2025-01-01    3
2026-01-01    4
dtype: int64
'''




# date_range function
#======================

# D :- day
#-----------

print(pd.date_range(start='2026/3/1', end='2026/3/31', freq='D'))

'''
DatetimeIndex(['2026-03-01', '2026-03-02', '2026-03-03', '2026-03-04',
               '2026-03-05', '2026-03-06', '2026-03-07', '2026-03-08',
               '2026-03-09', '2026-03-10', '2026-03-11', '2026-03-12',
               '2026-03-13', '2026-03-14', '2026-03-15', '2026-03-16',
               '2026-03-17', '2026-03-18', '2026-03-19', '2026-03-20',
               '2026-03-21', '2026-03-22', '2026-03-23', '2026-03-24',
               '2026-03-25', '2026-03-26', '2026-03-27', '2026-03-28',
               '2026-03-29', '2026-03-30', '2026-03-31'],
              dtype='datetime64[us]', freq='D')
'''


# alternate days in a give range
#................................
print(pd.date_range(start='2026/3/1', end='2026/3/31', freq='2D'))
'''
DatetimeIndex(['2026-03-01', '2026-03-03', '2026-03-05', '2026-03-07',
               '2026-03-09', '2026-03-11', '2026-03-13', '2026-03-15',
               '2026-03-17', '2026-03-19', '2026-03-21', '2026-03-23',
               '2026-03-25', '2026-03-27', '2026-03-29', '2026-03-31'],
              dtype='datetime64[us]', freq='2D')
'''

print(pd.date_range(start='2026/3/1', end='2026/3/31', freq='5D'))
'''
DatetimeIndex(['2026-03-01', '2026-03-06', '2026-03-11', '2026-03-16',
               '2026-03-21', '2026-03-26', '2026-03-31'],
              dtype='datetime64[us]', freq='5D')
'''



# B -> business days
#--------------------

print(pd.date_range(start='2026/3/1', end='2026/3/31', freq='B'))
'''
DatetimeIndex(['2026-03-02', '2026-03-03', '2026-03-04', '2026-03-05',
               '2026-03-06', '2026-03-09', '2026-03-10', '2026-03-11',
               '2026-03-12', '2026-03-13', '2026-03-16', '2026-03-17',
               '2026-03-18', '2026-03-19', '2026-03-20', '2026-03-23',
               '2026-03-24', '2026-03-25', '2026-03-26', '2026-03-27',
               '2026-03-30', '2026-03-31'],
              dtype='datetime64[us]', freq='B')
'''


# W -> one week per day
#-----------------------

print(pd.date_range(start='2026/3/1', end='2026/3/31', freq='W'))
'''
DatetimeIndex(['2026-03-01', '2026-03-08', '2026-03-15', '2026-03-22',
               '2026-03-29'],
              dtype='datetime64[us]', freq='W-SUN')
'''

print(pd.date_range(start='2026/3/1', end='2026/3/31', freq='W-MON'))
'''
DatetimeIndex(['2026-03-02', '2026-03-09', '2026-03-16', '2026-03-23',
               '2026-03-30'],
              dtype='datetime64[us]', freq='W-MON')
'''

print(pd.date_range(start='2026/3/1', end='2026/3/31', freq='W-TUE'))
'''
DatetimeIndex(['2026-03-03', '2026-03-10', '2026-03-17', '2026-03-24',
               '2026-03-31'],
              dtype='datetime64[us]', freq='W-TUE')
'''



# H -> Hourly data(factor)
#.........................

print(pd.date_range(start='2026/3/1', end='2026/3/31', freq='h'))
'''
DatetimeIndex(['2026-03-01 00:00:00', '2026-03-01 01:00:00',
               '2026-03-01 02:00:00', '2026-03-01 03:00:00',
               '2026-03-01 04:00:00', '2026-03-01 05:00:00',
               '2026-03-01 06:00:00', '2026-03-01 07:00:00',
               '2026-03-01 08:00:00', '2026-03-01 09:00:00',
               ...
               '2026-03-30 15:00:00', '2026-03-30 16:00:00',
               '2026-03-30 17:00:00', '2026-03-30 18:00:00',
               '2026-03-30 19:00:00', '2026-03-30 20:00:00',
               '2026-03-30 21:00:00', '2026-03-30 22:00:00',
               '2026-03-30 23:00:00', '2026-03-31 00:00:00'],
              dtype='datetime64[us]', length=721, freq='h')
'''


# ME -> Month end
#------------------

print(pd.date_range(start='2026/3/2', end='2026/3/31', freq='ME'))
'''
DatetimeIndex(['2026-03-31'], dtype='datetime64[us]', freq='ME')
'''




# MS -> Month start
#-------------------

print(pd.date_range(start='2026/3/1', end='2026/3/31', freq='MS'))
'''
DatetimeIndex(['2026-03-01'], dtype='datetime64[us]', freq='MS') 
'''



# YE -> Year end
#----------------

print(pd.date_range(start='2026/3/1', end='2030/3/31', freq='YE'))
'''
DatetimeIndex(['2026-12-31', '2027-12-31', '2028-12-31', '2029-12-31'], dtype='datetime64[us]', freq='YE-DEC')
'''


print(pd.date_range(start='2026/3/1', end='2030/3/31', freq='YS'))
'''
DatetimeIndex(['2027-01-01', '2028-01-01', '2029-01-01', '2030-01-01'], dtype='datetime64[us]', freq='YS-JAN')
'''



# using periods(Number of results)
#---------------------------------

print(pd.date_range(start='2023/1/5', periods=25, freq='D')) # next 25 days
'''
DatetimeIndex(['2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08',
               '2023-01-09', '2023-01-10', '2023-01-11', '2023-01-12',
               '2023-01-13', '2023-01-14', '2023-01-15', '2023-01-16',
               '2023-01-17', '2023-01-18', '2023-01-19', '2023-01-20',
               '2023-01-21', '2023-01-22', '2023-01-23', '2023-01-24',
               '2023-01-25', '2023-01-26', '2023-01-27', '2023-01-28',
               '2023-01-29'],
              dtype='datetime64[us]', freq='D')
'''



print(pd.date_range(start='2023/1/5', periods=25, freq='h')) # next 25 hours
'''
DatetimeIndex(['2023-01-05 00:00:00', '2023-01-05 01:00:00',
               '2023-01-05 02:00:00', '2023-01-05 03:00:00',
               '2023-01-05 04:00:00', '2023-01-05 05:00:00',
               '2023-01-05 06:00:00', '2023-01-05 07:00:00',
               '2023-01-05 08:00:00', '2023-01-05 09:00:00',
               '2023-01-05 10:00:00', '2023-01-05 11:00:00',
               '2023-01-05 12:00:00', '2023-01-05 13:00:00',
               '2023-01-05 14:00:00', '2023-01-05 15:00:00',
               '2023-01-05 16:00:00', '2023-01-05 17:00:00',
               '2023-01-05 18:00:00', '2023-01-05 19:00:00',
               '2023-01-05 20:00:00', '2023-01-05 21:00:00',
               '2023-01-05 22:00:00', '2023-01-05 23:00:00',
               '2023-01-06 00:00:00'],
              dtype='datetime64[us]', freq='h')
'''






# to_datetime function
#========================

# convert an existing objects to pandas timestamp/datetimeindex object

s = pd.Series(['2026/3/1', '2026/3/2', '2026/3/3'])

print(pd.to_datetime(s).dt.year)
'''
0    2026
1    2026
2    2026
dtype: int32
'''



print(pd.to_datetime(s).dt.month)
'''
1    3
2    3
dtype: int32
'''



print(pd.to_datetime(s).dt.month_name())
'''
0    March
1    March
2    March
dtype: str
'''



print(pd.to_datetime(s).dt.day)
'''
0    1
1    2
2    3
dtype: int32
'''



print(pd.to_datetime(s).dt.day_name())
'''
0     Sunday
1     Monday
2    Tuesday
dtype: str
'''



print(pd.to_datetime(s).dt.is_leap_year)
'''
0    False
1    False
2    False
dtype: bool
'''


print(pd.to_datetime(s).dt.is_year_start)
'''
0    False
1    False
2    False
'''


print(pd.to_datetime(s).dt.is_year_end)
'''
dtype: bool
0    False
1    False
2    False
dtype: bool
'''


print(pd.to_datetime(s).dt.is_month_start)
'''
0     True
1    False
2    False
dtype: bool
'''


print(pd.to_datetime(s).dt.is_month_end)
'''
0    False
1    False
2    False
dtype: bool
'''


print(pd.to_datetime(s).dt.is_quarter_start)
'''
0    False
1    False
2    False
dtype: bool
'''


print(pd.to_datetime(s).dt.is_quarter_end)
'''
0    False
1    False
2    False
dtype: bool
'''

print(pd.to_datetime(s).dt.isocalendar)
'''
<bound method DatetimeProperties.isocalendar of <pandas.core.indexes.accessors.DatetimeProperties object at 0x0000015AB10AD7F0>>
'''




# with error
#............

s = pd.Series(['2026/3/1', '2026/3/2', '2026/30000/3'])

print(pd.to_datetime(s, errors='coerce'))
'''
0   2026-03-01
1   2026-03-02
2          NaT
dtype: datetime64[us]
'''

print(pd.to_datetime(s, errors='coerce').dt.month_name())
'''
0    March
1    March
2      NaN
dtype: str
'''












# Practice
#============




path_dir = os.path.dirname(__file__)

path_file_expense = os.path.join(path_dir, '../1_Dataset/expense_data.csv')



expense = pd.read_csv(path_file_expense)



print(expense.info())
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




print(expense.columns)
'''
Index(['Date', 'Account', 'Category', 'Subcategory', 'Note', 'INR',
       'Income/Expense', 'Note.1', 'Amount', 'Currency', 'Account.1'],
      dtype='str')
'''



print(expense)
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






print(pd.to_datetime(expense['Date'], errors='coerce'))
'''
0     2022-03-02 10:11:00
1     2022-03-02 10:11:00
2     2022-03-01 19:50:00
3     2022-03-01 18:56:00
4     2022-03-01 18:22:00
              ...
272   2021-11-22 14:16:00
273   2021-11-22 14:16:00
274   2021-11-21 17:07:00
275   2021-11-21 15:50:00
276   2021-11-21 13:30:00
Name: Date, Length: 277, dtype: datetime64[us]
'''


expense['Date'] = pd.to_datetime(expense['Date'], errors='coerce')


print(expense)
'''
                   Date               Account        Category  Subcategory                Note     INR Income/Expense  Note.1  Amount Currency  Account.1
0   2022-03-02 10:11:00  CUB - online payment            Food          NaN             Brownie    50.0        Expense     NaN    50.0      INR       50.0    
1   2022-03-02 10:11:00  CUB - online payment           Other          NaN    To lended people   300.0        Expense     NaN   300.0      INR      300.0    
2   2022-03-01 19:50:00  CUB - online payment            Food          NaN              Dinner    78.0        Expense     NaN    78.0      INR       78.0    
3   2022-03-01 18:56:00  CUB - online payment  Transportation          NaN               Metro    30.0        Expense     NaN    30.0      INR       30.0    
4   2022-03-01 18:22:00  CUB - online payment            Food          NaN              Snacks    67.0        Expense     NaN    67.0      INR       67.0    
..                  ...                   ...             ...          ...                 ...     ...            ...     ...     ...      ...        ...    
272 2021-11-22 14:16:00  CUB - online payment            Food          NaN              Dinner    90.0        Expense     NaN    90.0      INR       90.0    
273 2021-11-22 14:16:00  CUB - online payment            Food          NaN  Lunch with company    97.0        Expense     NaN    97.0      INR       97.0    
274 2021-11-21 17:07:00  CUB - online payment  Transportation          NaN              Rapido   130.0        Expense     NaN   130.0      INR      130.0    
275 2021-11-21 15:50:00  CUB - online payment            Food          NaN               Lunch   875.0        Expense     NaN   875.0      INR      875.0    
276 2021-11-21 13:30:00  CUB - online payment           Other          NaN       Got from gobi  2000.0         Income     NaN  2000.0      INR     2000.0    

[277 rows x 11 columns]
'''



# dt accessor
#............

# Accessor object for datetimelike properties of the Series values.

print(expense['Date'].dt.month_name())
'''
0         March
1         March
2         March
3         March
4         March
         ...
272    November
273    November
274    November
275    November
276    November
Name: Date, Length: 277, dtype: str
'''



print(expense['Date'].dt.day_name())
'''
0      Wednesday
1      Wednesday
2        Tuesday
3        Tuesday
4        Tuesday
         ...
272       Monday
273       Monday
274       Sunday
275       Sunday
276       Sunday
Name: Date, Length: 277, dtype: str
'''




# graph plt
#-----------

plt.plot(expense['Date'], expense['INR'])
plt.show()



# Ques : plot the grop to repersent day wise expense
#...................................................

expense['day'] = expense['Date'].dt.day_name()

x = expense.groupby('day')['INR'].sum()

print(x)
'''
day
Friday        6910.00
Monday        6248.95
Saturday     34421.02
Sunday       31542.40
Thursday      9570.51
Tuesday      17344.65
Wednesday     7740.47
Name: INR, dtype: float64
'''

expense.groupby('day')['INR'].sum().plot(kind='bar')
plt.show()



expense['month'] = expense['Date'].dt.month_name()

expense.groupby('month')['INR'].sum().plot(kind='bar')
plt.show()



#  How to work on timeseries date :- teach in paid class