

#####################################################################

# 1. astype

# 2. value_counts (series and dataframe) :- gpt give perfect interview spoken diffinition

# 3. rank (series) :- gpt give perfect interview spoken diffinition

# 4. sort index (series and dataframe) :- gpt give perfect interview spoken diffinition

# 5. set index (dataframe) :- gpt give perfect interview spoken diffinition

# 6. rename index -> rename (dataframe) :- gpt give perfect interview spoken diffinition

# 7. reset index (series and dataframe) :- gpt give perfect interview spoken diffinition

# 8. unique (series) :- gpt give perfect interview spoken diffinition
# 8. nunique (series + dataframe) :- gpt give perfect interview spoken diffinition

# 9. isnull/notnull/hasnans (series and dataframe) :- gpt give perfect interview spoken diffinition

# 10. dropna (series and dataframe) :- gpt give perfect interview spoken diffinition

# 11. fillna (series and dataframe) :- gpt give perfect interview spoken diffinition

# 12. drop_duplicates (series and dataframe) :- gpt give perfect interview spoken diffinition

# 13. drop (series and dataframe) :- gpt give perfect interview spoken diffinition

# 14. apply (series and dataframe) :- gpt give perfect interview spoken diffinition

# 15. isin (series and dataframe) :- gpt give perfect interview spoken diffinition

# 16. corr (series and dataframe) :- gpt give perfect interview spoken diffinition

# 17. nlargest -> nsmallest (series and dataframe) :- gpt give perfect interview spoken diffinition

# 18. insert (series and dataframe) :- gpt give perfect interview spoken diffinition

# 19. copy (series and dataframe) :- gpt give perfect interview spoken diffinition


################################################################




import numpy as np
import pandas as pd



students = pd.DataFrame(
    {
        'name':['nitish', 'ankit', 'rupesh', np.nan, 'mrityunjay', np.nan, 'rishabh', np.nan, 'aditya', np.nan],
        'college':['bit', 'iit', 'vit', np.nan, np.nan, 'vlsi', 'ssit', np.nan, np.nan, 'git'],
        'cgpa':[6.66, 8.25, 6.41, np.nan, 5.6, 9.0, 7.4, np.nan, np.nan, np.nan],
        'package':[4, 5, 6, np.nan, 6, 7, 8, 9, np.nan, np.nan]
    }
)

print(students)

#          name college  cgpa  package
# 0      nitish     bit  6.66      4.0
# 1       ankit     iit  8.25      5.0
# 2      rupesh     vit  6.41      6.0
# 3         NaN     NaN   NaN      NaN
# 4  mrityunjay     NaN  5.60      6.0
# 5         NaN    vlsi  9.00      7.0
# 6     rishabh    ssit  7.40      8.0
# 7         NaN     NaN   NaN      9.0
# 8      aditya     NaN   NaN      NaN
# 9         NaN     git   NaN      NaN



# 11. fillna (series and dataframe) :- Perfect Interview Spoken Definition
#============================================================================
# fillna() is a pandas method used to replace missing values (NaN)
# in a Series or DataFrame with a specified value.


#     Important Parameters
#                value   -> value used to replace NaN (scalar, dict, Series)
#                method  -> 'ffill' : forward fill (previous value)
#                           'bfill' : backward fill (next value)
#                axis    -> 0 : fill column-wise (default)
#                           1 : fill row-wise
#                inplace -> True  : modifies original data
#                inplace -> False : returns new object (default)



# On Series
#==========

print(students['name'].fillna('unknown'))

# 0        nitish
# 1         ankit
# 2        rupesh
# 3       unknown
# 4    mrityunjay
# 5       unknown
# 6       rishabh
# 7       unknown
# 8        aditya
# 9       unknown
# Name: name, dtype: str



# On DataFrame
#=============

print(students.fillna(0))

#          name college  cgpa  package
# 0      nitish     bit  6.66      4.0
# 1       ankit     iit  8.25      5.0
# 2      rupesh     vit  6.41      6.0
# 3           0       0  0.00      0.0
# 4  mrityunjay       0  5.60      6.0
# 5           0    vlsi  9.00      7.0
# 6     rishabh    ssit  7.40      8.0
# 7           0       0  0.00      9.0
# 8      aditya       0  0.00      0.0
# 9           0     git  0.00      0.0



# Filling NaN using statistical value (Mean)
#-------------------------------------------

print(students['package'].fillna(students['package'].mean()))

# 0    4.000000
# 1    5.000000
# 2    6.000000
# 3    6.428571
# 4    6.000000
# 5    7.000000
# 6    8.000000
# 7    9.000000
# 8    6.428571
# 9    6.428571
# Name: package, dtype: float64



# 12. ffill (series and dataframe) :- Perfect Interview Spoken Definition
#============================================================================
# ffill() stands for Forward Fill.
# It replaces missing values (NaN) with the previous valid value
# present above it in the Series or DataFrame.

print(students['name'].ffill())  # Forward Fill

# 0        nitish
# 1         ankit
# 2        rupesh
# 3        rupesh
# 4    mrityunjay
# 5    mrityunjay
# 6       rishabh
# 7       rishabh
# 8        aditya
# 9        aditya
# Name: name, dtype: str



# 13. bfill (series and dataframe) :- Perfect Interview Spoken Definition
#============================================================================
# bfill() stands for Backward Fill.
# It replaces missing values (NaN) with the next valid value
# present below it in the Series or DataFrame.

print(students['name'].bfill())  # Backward Fill

# 0        nitish
# 1         ankit
# 2        rupesh
# 3    mrityunjay
# 4    mrityunjay
# 5       rishabh
# 6       rishabh
# 7        aditya
# 8        aditya
# 9           NaN
# Name: name, dtype: str