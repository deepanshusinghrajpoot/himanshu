

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


# 10. dropna (series and dataframe) :- Perfect Interview Spoken Definition
#============================================================================
# dropna() is a pandas method used to remove missing values (NaN) from a
# Series or DataFrame. It deletes rows or columns that contain null values.

# Important Parameters
#---------------------

# axis -> 0 : drop rows (default)
# axis -> 1 : drop columns

# how -> 'any' : drop if at least one NaN is present
#        'all' : drop only if all values are NaN

# subset -> specify column(s) to check for NaN (only for rows)

# inplace -> True  : modifies original data
# inplace -> False : returns new object (default)



# On Series
#==========

print(students['name'].dropna())

# 0        nitish
# 1         ankit
# 2        rupesh
# 4    mrityunjay
# 6       rishabh
# 8        aditya
# Name: name, dtype: str



# On DataFrame
#=============


# In DataFrame dropna() removes all rows which contain at least one NaN
#-----------------------------------------------------------------------

print(students.dropna())

#       name college  cgpa  package
# 0   nitish     bit  6.66      4.0
# 1    ankit     iit  8.25      5.0
# 2   rupesh     vit  6.41      6.0
# 6  rishabh    ssit  7.40      8.0



print(students.dropna(how='any'))

#       name college  cgpa  package
# 0   nitish     bit  6.66      4.0
# 1    ankit     iit  8.25      5.0
# 2   rupesh     vit  6.41      6.0
# 6  rishabh    ssit  7.40      8.0



# Remove row only if all column values are NaN
#---------------------------------------------

print(students.dropna(how='all'))

#          name college  cgpa  package
# 0      nitish     bit  6.66      4.0
# 1       ankit     iit  8.25      5.0
# 2      rupesh     vit  6.41      6.0
# 4  mrityunjay     NaN  5.60      6.0
# 5         NaN    vlsi  9.00      7.0
# 6     rishabh    ssit  7.40      8.0
# 7         NaN     NaN   NaN      9.0
# 8      aditya     NaN   NaN      NaN
# 9         NaN     git   NaN      NaN



# Remove rows based on one column or multiple columns
#----------------------------------------------------

print(students.dropna(subset=['name']))

#          name college  cgpa  package
# 0      nitish     bit  6.66      4.0
# 1       ankit     iit  8.25      5.0
# 2      rupesh     vit  6.41      6.0
# 4  mrityunjay     NaN  5.60      6.0
# 6     rishabh    ssit  7.40      8.0
# 8      aditya     NaN   NaN      NaN


print(students.dropna(subset=['name','college']))  # 'name' OR 'college'

#       name college  cgpa  package
# 0   nitish     bit  6.66      4.0
# 1    ankit     iit  8.25      5.0
# 2   rupesh     vit  6.41      6.0
# 6  rishabh    ssit  7.40      8.0



# If we want permanent changes
#-----------------------------

# students.dropna(inplace=True)