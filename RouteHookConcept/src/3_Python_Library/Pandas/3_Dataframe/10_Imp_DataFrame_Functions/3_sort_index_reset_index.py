#####################################################################

# 1. astype

# 2. value_counts (series and dataframe) :- gpt give perfect interview spoken diffinition

# 3. rank (series) :- gpt give perfect interview spoken diffinition

# 4. sort index (series and dataframe) :- gpt give perfect interview spoken diffinition

# 5. set index (dataframe) :- gpt give perfect interview spoken diffinition

# 6. rename index -> rename (series and dataframe) :- gpt give perfect interview spoken diffinition

# 7. reset index (series and dataframe) :- gpt give perfect interview spoken diffinition

# 8. unique & nunique (series and dataframe) :- gpt give perfect interview spoken diffinition

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




path_dir = os.path.dirname(__file__)
bastman_run_ipl = os.path.join(path_dir, '../../1_Dataset/batsman_runs_ipl.csv')


bastman_run = pd.read_csv(bastman_run_ipl)

print(bastman_run)

#              batter  batsman_run
# 0    A Ashish Reddy          280
# 1          A Badoni          161
# 2        A Chandila            4
# 3          A Chopra           53
# 4       A Choudhary           25
# ..              ...          ...
# 600      Yash Dayal            0
# 601   Yashpal Singh           47
# 602     Younis Khan            3
# 603    Yuvraj Singh         2754
# 604          Z Khan          117
#
# [605 rows x 2 columns]








# 4. sort_index(series and dataframe) :- Perfect Interview Spoken Definition
#================================================================================
# sort_index() is a pandas method used to sort a Series or DataFrame based on its index labels
# instead of the data values. It rearranges the data according to the index order.

# Important Parameter
#--------------------
# ascending -> True  : sort index in ascending order
# ascending -> False : sort index in descending order



marks = pd.Series(
    {
        'math':93,
        'english':88,
        'science':89,
        'hindi':100
    }
)

print(marks.sort_index())

# english     88
# hindi      100
# math        93
# science     89
# dtype: int64



print(bastman_run.sort_index(ascending=False))

#              batter  batsman_run   rank
# 604          Z Khan          117  256.0
# 603    Yuvraj Singh         2754   27.0
# 602     Younis Khan            3  547.5
# 601   Yashpal Singh           47  343.0
# 600      Yash Dayal            0  594.0
# ..              ...          ...    ...
# 4       A Choudhary           25  402.5
# 3          A Chopra           53  329.0
# 2        A Chandila            4  535.0
# 1          A Badoni          161  226.0
# 0    A Ashish Reddy          280  166.5
#
# [605 rows x 3 columns]



# 5. set_index(dataframe) :- Perfect Interview Spoken Definition
#================================================================
# set_index() is a pandas DataFrame method used to convert an existing column
# into the index of the DataFrame.

# Note : set_index() is a temporary operation
# To make the change permanent we use -> inplace=True



print(bastman_run.set_index('batter'))

# batter          batsman_run
# A Ashish Reddy          280
# A Badoni                161
# A Chandila                4
# A Chopra                 53
# A Choudhary              25
# ...                     ...
# Yash Dayal                0
# Yashpal Singh            47
# Younis Khan               3
# Yuvraj Singh           2754
# Z Khan                  117
#
# [605 rows x 1 columns]



bastman_run.set_index('batter', inplace=True)
print(bastman_run)

# batter          batsman_run
# A Ashish Reddy          280
# A Badoni                161
# A Chandila                4
# A Chopra                 53
# A Choudhary              25
# ...                     ...
# Yash Dayal                0
# Yashpal Singh            47
# Younis Khan               3
# Yuvraj Singh           2754
# Z Khan                  117
#
# [605 rows x 1 columns]



# 6. reset_index(series + dataframe) :- Perfect Interview Spoken Definition
#============================================================================
# reset_index() is a pandas method used to convert the current index
# back into a normal column and replace it with a default integer index.

# Important Parameter
#--------------------
# drop -> True  : removes the old index instead of converting it into a column



print(bastman_run.reset_index())

#              batter  batsman_run
# 0    A Ashish Reddy          280
# 1          A Badoni          161
# 2        A Chandila            4
# 3          A Chopra           53
# 4       A Choudhary           25
# ..              ...          ...
# 600      Yash Dayal            0
# 601   Yashpal Singh           47
# 602     Younis Khan            3
# 603    Yuvraj Singh         2754
# 604          Z Khan          117
#
# [605 rows x 2 columns]



# How to replace existing index without losing column
#----------------------------------------------------

print(bastman_run.reset_index().set_index('batsman_run'))

# batsman_run          batter
# 280          A Ashish Reddy
# 161                A Badoni
# 4                A Chandila
# 53                 A Chopra
# 25              A Choudhary
# ...                     ...
# 0                Yash Dayal
# 47            Yashpal Singh
# 3               Younis Khan
# 2754           Yuvraj Singh
# 117                  Z Khan
#
# [605 rows x 1 columns]



# When we apply reset_index() on a Series it becomes a DataFrame (Important)
#--------------------------------------------------------------------------

print(marks.reset_index())

#      index    0
# 0     math   93
# 1  english   88
# 2  science   89
# 3    hindi  100