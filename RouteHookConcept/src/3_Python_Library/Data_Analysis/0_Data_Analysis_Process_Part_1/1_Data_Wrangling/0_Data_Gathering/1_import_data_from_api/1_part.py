
import numpy as np
import pandas as pd
import requests
import time
import os

API_KEY = "571c4e7841dc3690f41beccfaa9819db"
url = "https://api.themoviedb.org/3/tv/top_rated"

data = []

for page in range(1,121):

    while True:   # keep trying until success
        
        try:
            response = requests.get(
                url,
                params={"api_key": API_KEY, "page": page},
                headers={"User-Agent": "Mozilla/5.0"},
                timeout=10
            )

            response.raise_for_status()

            results = response.json()['results']
            data.extend(results)

            print(f"Page {page} loaded")

            break   # exit loop when success

        except requests.exceptions.RequestException as e:

            print(f"Retrying page {page} after error:", e)

            time.sleep(3)   # wait before retry


df = pd.DataFrame(data)



path = os.path.dirname(__file__)
path_file_movies = os.path.join(path, '../4_save_export_file/movies.csv')
df[['id', 'overview', 'origin_country', 'original_name', 'vote_count', 'popularity', 'original_language']].to_csv(path_file_movies)