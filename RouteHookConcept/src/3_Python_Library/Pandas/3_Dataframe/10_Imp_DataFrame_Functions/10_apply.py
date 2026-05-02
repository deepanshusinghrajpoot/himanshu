

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

import os

marks = pd.DataFrame([
    [100, 80, 10],
    [90, 70, 7],
    [120, 100, 14],
    [80, 70, 14],
    [80, 70, 14]
], columns=['iq', 'marks', 'package'])


print(marks)

#     iq  marks  package
# 0  100     80       10
# 1   90     70        7
# 2  120    100       14
# 3   80     70       14
# 4   80     70       14







# 14. apply (series and dataframe) :- Perfect Interview Spoken Definition
#============================================================================
# apply() is a pandas method used to apply a custom function to each element
# of a Series or to rows/columns of a DataFrame.

# Interview Friendly Definition
#------------------------------
# apply() allows us to run a user-defined function on pandas data
# to perform custom transformations or calculations.

# Important Parameter
#--------------------
# axis = 0  -> apply function on columns
# axis = 1  -> apply function on rows



# Example on Series
#==================

temp = pd.Series([10, 20, 30, 40, 50])

print(temp)

# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64


# Example Function
#-----------------

def sigmoid(value):
    return 1 / (1 + np.exp(-value))   # Correct sigmoid formula


print(temp.apply(sigmoid))

# 0    0.999955
# 1    1.000000
# 2    1.000000
# 3    1.000000
# 4    1.000000
# dtype: float64




# Example on DataFrame
#=====================

points_df = pd.DataFrame(
    {
        '1st point':[(3, 4), (-6, 5), (0, 0), (-10, 1), (4, 5)],
        '2nd point':[(-3, 4), (0, 0), (2, 2), (10, 10), (1, 1)]
    }
)


print(points_df)

#   1st point 2nd point
# 0    (3, 4)   (-3, 4)
# 1   (-6, 5)    (0, 0)
# 2    (0, 0)    (2, 2)
# 3  (-10, 1)  (10, 10)
# 4    (4, 5)    (1, 1)



# Add new column as Euclidean distance
#-------------------------------------

# Euclidean Distance Formula
# √((x1 - x2)^2 + (y1 - y2)^2)

def euclidean(row):

    pt_A = row['1st point']
    pt_B = row['2nd point']

    return ((pt_A[0] - pt_B[0])**2 + (pt_A[1] - pt_B[1])**2) ** 0.5


print(points_df.apply(euclidean, axis=1))

# 0     6.000000
# 1     7.810250
# 2     2.828427
# 3    21.931712
# 4     5.000000
# dtype: float64



# Add result as new column
#-------------------------

points_df['distance'] = points_df.apply(euclidean, axis=1)

print(points_df)

#   1st point 2nd point   distance
# 0    (3, 4)   (-3, 4)   6.000000
# 1   (-6, 5)    (0, 0)   7.810250
# 2    (0, 0)    (2, 2)   2.828427
# 3  (-10, 1)  (10, 10)  21.931712
# 4    (4, 5)    (1, 1)   5.000000



# Key Points for Quick Revision
#==============================
# • apply() executes a custom function on pandas data
# • Works on both Series and DataFrame
# • axis=0 → column-wise operation
# • axis=1 → row-wise operation
# • Commonly used for custom calculations and feature engineering