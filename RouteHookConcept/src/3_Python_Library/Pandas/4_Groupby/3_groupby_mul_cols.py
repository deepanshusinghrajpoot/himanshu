


import numpy as np
import pandas as pd


import os



path_dir = os.path.dirname(__file__)

path_file_imdb_top_1000 = os.path.join(path_dir, '../1_Dataset/imdb-top-1000.csv')




movies = pd.read_csv(path_file_imdb_top_1000)

print(movies.columns)
# Index(['Series_Title', 'Released_Year', 'Runtime', 'Genre', 'IMDB_Rating',
#        'Director', 'Star1', 'No_of_Votes', 'Gross', 'Metascore'],
#       dtype='str')




# groupby on multiple columns
#=============================

# gpt give perfect interview spoken diffinition



print(movies.groupby(['Director', 'Star1'])) # 'Director' and 'Star1' 
# <pandas.api.typing.DataFrameGroupBy object at 0x00000265F8A68590>

# size
#......
print(movies.groupby(['Director', 'Star1']).size())

# Director             Star1
# Aamir Khan           Amole Gupte       1
# Aaron Sorkin         Eddie Redmayne    1
# Abdellatif Kechiche  Léa Seydoux       1
# Abhishek Chaubey     Shahid Kapoor     1
# Abhishek Kapoor      Amit Sadh         1
#                                       ..
# Zaza Urushadze       Lembit Ulfsak     1
# Zoya Akhtar          Hrithik Roshan    1
#                      Vijay Varma       1
# Çagan Irmak          Çetin Tekindor    1
# Ömer Faruk Sorak     Cem Yilmaz        1
# Length: 898, dtype: int64



# get_group
#...........

print(movies.groupby(['Director', 'Star1']).get_group(('Aamir Khan','Amole Gupte')))
#         Series_Title Released_Year  Runtime  Genre  IMDB_Rating    Director        Star1  No_of_Votes      Gross  Metascore
# 65  Taare Zameen Par          2007      165  Drama          8.4  Aamir Khan  Amole Gupte       168895  1223869.0        NaN



# Ques : Find the most earning actors and director combo
#--------------------------------------------------------

print(movies.groupby(['Director', 'Star1'])['Gross'].sum().sort_values(ascending=False).head(1))
# Director        Star1
# Akira Kurosawa  Toshirô Mifune    2.999877e+09
# Name: Gross, dtype: float64



# Ques : Find the best(in-term of metascore(avg)) actor and genre combo
#-----------------------------------------------------------------------

print(movies.groupby(['Star1', 'Genre'])['Metascore'].mean().sort_values(ascending=False).head(1))
# Star1          Genre
# Peter O'Toole  Adventure    100.0
# Name: Metascore, dtype: float64



print(movies.info())


# agg on multiple groupby
#-------------------------

print(movies.groupby(['Director', 'Star1'])[['Runtime', 'IMDB_Rating', 'No_of_Votes', 'Gross', 'Metascore']].agg(['min', 'max', 'mean']))

#                                    Runtime             IMDB_Rating            ...        Gross                           Metascore
#                                        min  max   mean         min  max mean  ...          min          max         mean       min   max  mean
# Director            Star1                                                     ...
# Aamir Khan          Amole Gupte        165  165  165.0         8.4  8.4  8.4  ...    1223869.0    1223869.0    1223869.0       NaN   NaN   NaN
# Aaron Sorkin        Eddie Redmayne     129  129  129.0         7.8  7.8  7.8  ...  853090410.0  853090410.0  853090410.0      77.0  77.0  77.0
# Abdellatif Kechiche Léa Seydoux        180  180  180.0         7.7  7.7  7.7  ...    2199675.0    2199675.0    2199675.0      89.0  89.0  89.0
# Abhishek Chaubey    Shahid Kapoor      148  148  148.0         7.8  7.8  7.8  ...  218428303.0  218428303.0  218428303.0       NaN   NaN   NaN
# Abhishek Kapoor     Amit Sadh          130  130  130.0         7.7  7.7  7.7  ...    1122527.0    1122527.0    1122527.0      40.0  40.0  40.0
# ...                                    ...  ...    ...         ...  ...  ...  ...          ...          ...          ...       ...   ...   ...
# Zaza Urushadze      Lembit Ulfsak       87   87   87.0         8.2  8.2  8.2  ...     144501.0     144501.0     144501.0      73.0  73.0  73.0
# Zoya Akhtar         Hrithik Roshan     155  155  155.0         8.1  8.1  8.1  ...    3108485.0    3108485.0    3108485.0       NaN   NaN   NaN
#                     Vijay Varma        154  154  154.0         8.0  8.0  8.0  ...    5566534.0    5566534.0    5566534.0      65.0  65.0  65.0
# Çagan Irmak         Çetin Tekindor     112  112  112.0         8.3  8.3  8.3  ...  461855363.0  461855363.0  461855363.0       NaN   NaN   NaN
# Ömer Faruk Sorak    Cem Yilmaz         127  127  127.0         8.0  8.0  8.0  ...  196206077.0  196206077.0  196206077.0       NaN   NaN   NaN
# 
# [898 rows x 15 columns]


# groupby perform similar to on single and multiple column