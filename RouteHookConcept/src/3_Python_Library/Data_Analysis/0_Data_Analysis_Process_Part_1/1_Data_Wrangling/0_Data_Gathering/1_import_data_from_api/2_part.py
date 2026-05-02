

import pandas as pd


import os


path = os.path.dirname(__file__)

path_file_movies = os.path.join(path, '../4_save_export_file/movies.csv')


movies = pd.read_csv(path_file_movies)


print(movies.info())
'''
<class 'pandas.DataFrame'>
RangeIndex: 2389 entries, 0 to 2388
Data columns (total 8 columns):
 #   Column             Non-Null Count  Dtype
---  ------             --------------  -----
 0   Unnamed: 0         2389 non-null   int64
 1   id                 2389 non-null   int64
 2   overview           2367 non-null   str
 3   origin_country     2389 non-null   str
 4   original_name      2389 non-null   str
 5   vote_count         2389 non-null   int64
 6   popularity         2389 non-null   float64
 7   original_language  2389 non-null   str
dtypes: float64(1), int64(3), str(4)
memory usage: 149.4 KB
None
'''


print(movies)
'''
      Unnamed: 0      id                                           overview  ... vote_count popularity  original_language
0              0    1396  Walter White, a New Mexico chemistry teacher, ...  ...      17246   119.6668                 en
1              1  280945  After time traveling to the Joseon era, a tale...  ...        203    12.4107                 ko
2              2  209867  Decades after her party defeated the Demon Kin...  ...        713   103.9050                 ja
3              3     246  In a war-torn world of elemental magic, a youn...  ...       4711    22.7118                 en
4              4   94605  Amid the stark discord of twin cities Piltover...  ...       5734    33.7823                 en
...          ...     ...                                                ...  ...        ...        ...                ...
2384        2384  114471  After the events of Black Panther: Wakanda For...  ...        421    11.1422                 en
2385        2385  130392  From relative obscurity and a seemingly normal...  ...        684     3.5333                 en
2386        2386   10160  American version of the reality game show whic...  ...        257    45.1779                 en
2387        2387    1871  The everyday lives of working-class residents ...  ...        219   131.5033                 en
2388        2388  126725  Jinkies! This raucous reimagining of the Scoob...  ...        329     7.9553                 en

[2389 rows x 8 columns]
'''