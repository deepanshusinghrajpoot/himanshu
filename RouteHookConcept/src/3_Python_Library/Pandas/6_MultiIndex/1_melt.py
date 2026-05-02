


import numpy as np
import pandas as pd


import os


path_dir = os.path.dirname(__file__)


path_file_time_series_covid19_confirmed_global = os.path.join(path_dir, '../1_Dataset/time_series_covid19_confirmed_global.csv')
path_file_time_series_covid19_deaths_global = os.path.join(path_dir, '../1_Dataset/time_series_covid19_deaths_global.csv')


confirm = pd.read_csv(path_file_time_series_covid19_confirmed_global)
death = pd.read_csv(path_file_time_series_covid19_deaths_global)


print(confirm.info())
'''
<class 'pandas.DataFrame'>
RangeIndex: 289 entries, 0 to 288
Columns: 1081 entries, Province/State to 1/2/23
dtypes: float64(2), int64(1077), str(2)
memory usage: 2.4 MB
None
'''


print(death.info())
'''
<class 'pandas.DataFrame'>
RangeIndex: 289 entries, 0 to 288
Columns: 1081 entries, Province/State to 1/2/23
dtypes: float64(2), int64(1077), str(2)
memory usage: 2.4 MB
None
'''

print(death.columns)
'''
Index(['Province/State', 'Country/Region', 'Lat', 'Long', '1/22/20', '1/23/20',
       '1/24/20', '1/25/20', '1/26/20', '1/27/20',
       ...
       '12/24/22', '12/25/22', '12/26/22', '12/27/22', '12/28/22', '12/29/22',
       '12/30/22', '12/31/22', '1/1/23', '1/2/23'],
      dtype='str', length=1081)
'''

print(confirm.columns)
'''
Index(['Province/State', 'Country/Region', 'Lat', 'Long', '1/22/20', '1/23/20',
       '1/24/20', '1/25/20', '1/26/20', '1/27/20',
       ...
       '12/24/22', '12/25/22', '12/26/22', '12/27/22', '12/28/22', '12/29/22',
       '12/30/22', '12/31/22', '1/1/23', '1/2/23'],
      dtype='str', length=1081)
'''




# =============================================================================
# Long vs Wide Data
# =============================================================================

# Wide Format:
# One row represents one entity, and multiple columns store attributes.

'''
        Name            Height      Weight
        John            160         67
        Christopher     182         78
'''

# Long Format:
# One entity can have multiple rows.
# Attributes are stored vertically.

'''
        Name          Attribute      Value
        John          Height         160
        John          Weight          67
        Christopher   Height         182
        Christopher   Weight          78
'''



# =============================================================================
# melt() vs pivot()
# =============================================================================

# melt() : Pandas method used to convert wide format data
#          into long format data (Unpivot).

# pivot() : Pandas method used to convert long format data
#           into wide format data (Reshape).

# Interview Line: melt converts columns into rows,
#                 pivot converts rows into columns.







# =============================================================================
# Basic melt Example
# =============================================================================


print(pd.DataFrame({'cse':[120]}))
'''
   cse
0  120
'''

# melt -> branch with year
#..........................

print(pd.DataFrame({'cse':[120], 'ece':[100], 'mech':[50]}).melt(var_name='branch', value_name='num_students'))
'''
  branch  num_students
0    cse           120
1    ece           100
2   mech            50
'''


df_1 = pd.DataFrame(
    {
        'branch':['cse', 'ece', 'mech'],
        '2020':[100, 150, 60],
        '2021':[120, 130, 80],
        '2022':[150, 140, 70]
    }
)

print(df_1)
'''
  branch  2020  2021  2022
0    cse   100   120   150
1    ece   150   130   140
2   mech    60    80    70
'''

print(df_1.melt(var_name='branch', value_name='num_students'))

'''
    branch num_students
0   branch          cse
1   branch          ece
2   branch         mech
3     2020          100
4     2020          150
5     2020           60
6     2021          120
7     2021          130
8     2021           80
9     2022          150
10    2022          140
11    2022           70
'''


print(df_1.melt(id_vars=['branch'], var_name='year', value_name='num_students'))
'''
  branch  year  num_students
0    cse  2020           100
1    ece  2020           150
2   mech  2020            60
3    cse  2021           120
4    ece  2021           130
5   mech  2021            80
6    cse  2022           150
7    ece  2022           140
8   mech  2022            70
'''




print(death.head())
'''
  Province/State Country/Region       Lat       Long  1/22/20  1/23/20  1/24/20  ...  12/27/22  12/28/22  12/29/22  12/30/22  12/31/22  1/1/23  1/2/23
0            NaN    Afghanistan  33.93911  67.709953        0        0        0  ...      7846      7846      7847      7847      7849    7849    7849       
1            NaN        Albania  41.15330  20.168300        0        0        0  ...      3595      3595      3595      3595      3595    3595    3595       
2            NaN        Algeria  28.03390   1.659600        0        0        0  ...      6881      6881      6881      6881      6881    6881    6881       
3            NaN        Andorra  42.50630   1.521800        0        0        0  ...       165       165       165       165       165     165     165       
4            NaN         Angola -11.20270  17.873900        0        0        0  ...      1930      1930      1930      1930      1930    1930    1930

[5 rows x 1081 columns]    
'''


print(confirm.head())
'''
  Province/State Country/Region       Lat       Long  1/22/20  1/23/20  1/24/20  ...  12/27/22  12/28/22  12/29/22  12/30/22  12/31/22  1/1/23  1/2/23
0            NaN    Afghanistan  33.93911  67.709953        0        0        0  ...    207460    207493    207511    207550    207559  207616  207627       
1            NaN        Albania  41.15330  20.168300        0        0        0  ...    333751    333776    333776    333806    333806  333811  333812       
2            NaN        Algeria  28.03390   1.659600        0        0        0  ...    271202    271208    271217    271223    271228  271229  271229       
3            NaN        Andorra  42.50630   1.521800        0        0        0  ...     47686     47751     47751     47751     47751   47751   47751       
4            NaN         Angola -11.20270  17.873900        0        0        0  ...    105095    105095    105095    105095    105095  105095  105095       

[5 rows x 1081 columns]
'''





print(death.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], var_name='date', value_name='num_deaths'))

'''
       Province/State        Country/Region        Lat        Long     date  num_deaths
0                 NaN           Afghanistan  33.939110   67.709953  1/22/20           0
1                 NaN               Albania  41.153300   20.168300  1/22/20           0
2                 NaN               Algeria  28.033900    1.659600  1/22/20           0
3                 NaN               Andorra  42.506300    1.521800  1/22/20           0
4                 NaN                Angola -11.202700   17.873900  1/22/20           0
...               ...                   ...        ...         ...      ...         ...
311248            NaN    West Bank and Gaza  31.952200   35.233200   1/2/23        5708
311249            NaN  Winter Olympics 2022  39.904200  116.407400   1/2/23           0
311250            NaN                 Yemen  15.552727   48.516388   1/2/23        2159
311251            NaN                Zambia -13.133897   27.849332   1/2/23        4024
311252            NaN              Zimbabwe -19.015438   29.154857   1/2/23        5637

[311253 rows x 6 columns]
'''



print(confirm.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], var_name='date', value_name='num_confirms'))

'''
       Province/State        Country/Region        Lat        Long     date  num_confirms
0                 NaN           Afghanistan  33.939110   67.709953  1/22/20             0
1                 NaN               Albania  41.153300   20.168300  1/22/20             0
2                 NaN               Algeria  28.033900    1.659600  1/22/20             0
3                 NaN               Andorra  42.506300    1.521800  1/22/20             0
4                 NaN                Angola -11.202700   17.873900  1/22/20             0
...               ...                   ...        ...         ...      ...           ...
311248            NaN    West Bank and Gaza  31.952200   35.233200   1/2/23        703228
311249            NaN  Winter Olympics 2022  39.904200  116.407400   1/2/23           535
311250            NaN                 Yemen  15.552727   48.516388   1/2/23         11945
311251            NaN                Zambia -13.133897   27.849332   1/2/23        334661
311252            NaN              Zimbabwe -19.015438   29.154857   1/2/23        259981

[311253 rows x 6 columns]
'''









# =============================================================================
# Why melt() is Useful
# =============================================================================
# After converting to long format:
# - Easy filtering
# - Easy groupby
# - Easy plotting
# - Easy time-series analysis
# - Easy merging datasets







# =============================================================================
# Interview Spoken Definition with Example
# =============================================================================


# =============================================================================
# lll melt()
# =============================================================================

# "Sir, melt() is a pandas reshaping method used to convert
# wide-format data into long-format data by transforming
# columns into rows."

# It has parameters:
#             (Indicate)
# id_vars         ->        Columns to keep fixed
# value_vars      ->        Columns to unpivot
# var_name        ->        Name of variable column
# value_name      ->        Name of value column
# ignore_index    ->        Reset index or not


import pandas as pd

df = pd.DataFrame({
    'Name':['John', 'Chris'],
    'Height':[160, 182],
    'Weight':[67, 78]
})

print(df)

'''
    Name  Height  Weight
0   John     160      67
1  Chris     182      78
'''


print(
    df.melt(
        id_vars='Name',
        value_vars=['Height', 'Weight'],
        var_name='Attribute',
        value_name='Value'
    )
)

'''
    Name Attribute  Value
0   John    Height    160
1  Chris    Height    182
2   John    Weight     67
3  Chris    Weight     78
'''



# =============================================================================
# lll pivot()
# =============================================================================

# "Sir, pivot() is a pandas reshaping method used to convert
# long-format data into wide-format data by transforming
# row values into columns."

# Important Parameters:
# index   -> Row labels
# columns -> New column names
# values  -> Fill values


long_df = pd.DataFrame({
    'Name':['John', 'Chris', 'John', 'Chris'],
    'Attribute':['Height', 'Height', 'Weight', 'Weight'],
    'Value':[160, 182, 67, 78]
})

print(long_df)

'''
    Name Attribute  Value
0   John    Height    160
1  Chris    Height    182
2   John    Weight     67
3  Chris    Weight     78
'''


print(
    long_df.pivot(
        index='Name',
        columns='Attribute',
        values='Value'
    )
)

'''
Attribute  Height  Weight
Name                     
Chris         182      78
John          160      67
'''



# =============================================================================
# Final One-Line Interview Answer
# =============================================================================

# melt()  -> Converts columns into rows
# pivot() -> Converts rows into columns
# =============================================================================



