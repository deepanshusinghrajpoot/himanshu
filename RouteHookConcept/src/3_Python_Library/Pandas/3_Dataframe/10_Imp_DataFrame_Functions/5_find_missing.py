

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






# 9. isnull / notnull / hasnans (series and dataframe)
#=====================================================
# These pandas methods are used to detect and work with missing values (NaN) in data.


# isnull (series and dataframe) :- Perfect Interview Spoken Definition
#----------------------------------------------------------------------
# isnull() is a pandas method used to identify missing values (NaN) in a Series or DataFrame.
# It returns a boolean result where:
# True  -> value is NaN (missing)
# False -> value is present


print(students['name'].isnull())

# 0    False
# 1    False
# 2    False
# 3     True
# 4    False
# 5     True
# 6    False
# 7     True
# 8    False
# 9     True
# Name: name, dtype: bool


print(students['name'][students['name'].isnull()])

# 3    NaN
# 5    NaN
# 7    NaN
# 9    NaN
# Name: name, dtype: str



# notnull (series and dataframe) :- Perfect Interview Spoken Definition
#-----------------------------------------------------------------------
# notnull() is the opposite of isnull().
# It is used to identify non-missing (valid) values in a Series or DataFrame.
# It returns:
# True  -> value is present
# False -> value is NaN


print(students['name'].notnull())

# 0     True
# 1     True
# 2     True
# 3    False
# 4     True
# 5    False
# 6     True
# 7    False
# 8     True
# 9    False
# Name: name, dtype: bool


print(students['name'][students['name'].notnull()])

# 0        nitish
# 1         ankit
# 2        rupesh
# 4    mrityunjay
# 6       rishabh
# 8        aditya
# Name: name, dtype: str



# hasnans (series and dataframe) :- Perfect Interview Spoken Definition
#-----------------------------------------------------------------------
# hasnans is a pandas Series attribute used to quickly check
# whether a Series contains any missing values (NaN) or not.
# It returns:
# True  -> if at least one NaN exists
# False -> if no NaN exists


print(students['name'].hasnans)

# True



# On DataFrame
#=============


# isnull
#-------

print(students.isnull())

#     name  college   cgpa  package
# 0  False    False  False    False
# 1  False    False  False    False
# 2  False    False  False    False
# 3   True     True   True     True
# 4  False     True  False    False
# 5   True    False  False    False
# 6  False    False  False    False
# 7   True     True   True    False
# 8  False     True   True     True
# 9   True    False   True     True



# notnull
#--------

print(students.notnull())

#     name  college   cgpa  package
# 0   True     True   True     True
# 1   True     True   True     True
# 2   True     True   True     True
# 3  False    False  False    False
# 4   True    False   True     True
# 5  False     True   True     True
# 6   True     True   True     True
# 7  False    False  False     True
# 8   True    False  False    False
# 9  False     True  False    False