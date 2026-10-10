

# API(Aplication programming interface)
#---------------------------------------
'''
API is data pipeline


eg:

Suppose that we want to book ticket 
we are book from multiple plateform like : IRTCE, MAKE MY TRIP, YATRA etc
We are know that each plateform has its won database which share own API to share data 
make consitency


Now we are want to fetch data from TMD
-----------------------------------------

genergate API key 


use API key in get API and see data in browser

copy all data and pest in :- online json site where see all about data





similary you go : rapid api site where there are so many free API exist
gpt give popular site to get data API
'''


import pandas as pd
import requests

API_KEY = "571c4e7841dc3690f41beccfaa9819db"

url = "https://api.themoviedb.org/3/tv/top_rated"

response = requests.get(
    url,
    params={"api_key": API_KEY},
    headers={"User-Agent": "Mozilla/5.0"}
)



print(pd.DataFrame(response.json()['results']).info())
'''
<class 'pandas.DataFrame'>
RangeIndex: 20 entries, 0 to 19
Data columns (total 14 columns):
 #   Column             Non-Null Count  Dtype
---  ------             --------------  -----
 0   adult              20 non-null     bool
 1   backdrop_path      20 non-null     str
 2   genre_ids          20 non-null     object
 3   id                 20 non-null     int64
 4   origin_country     20 non-null     object
 5   original_language  20 non-null     str
 6   original_name      20 non-null     str
 7   overview           20 non-null     str
 8   popularity         20 non-null     float64
 9   poster_path        20 non-null     str
 10  first_air_date     20 non-null     str
 11  name               20 non-null     str
 12  vote_average       20 non-null     float64
 13  vote_count         20 non-null     int64
dtypes: bool(1), float64(2), int64(2), object(2), str(7)
memory usage: 2.2+ KB
None
'''




print(pd.DataFrame(response.json()['results'])[['id', 'overview', 'origin_country', 'original_name', 'vote_count', 'popularity', 'original_language']])


df = pd.DataFrame()


for i in range(1, 121):   # pages 1 to 120
    
    response = requests.get(
        url,
        params={
            "api_key": API_KEY,
            "page": i
        },
        headers={"User-Agent": "Mozilla/5.0"}
    )
    
    temp_df = pd.DataFrame(response.json()['results'])[['id', 'overview', 'origin_country', 'original_name', 'vote_count', 'popularity', 'original_language']]
    
    df = pd.concat([df, temp_df], ignore_index=True)



print(df)