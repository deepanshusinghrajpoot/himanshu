"""
===========================================
AmbitionBox Scraper using Your List Style
===========================================
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import os


data = []

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}


for page in range(1, 50):

    url = f"https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page={page}"

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    company = soup.find_all('div', class_='companyCardWrapper__metaInformation')


    # Your list comprehension style
    name1 = [i.find('h2').text.strip() for i in company]

    rating1 = [i.find('div', class_='rating_star_container').text.strip() for i in company]

    review_count1 = [
        i.find('span', class_='companyCardWrapper__companyRatingCount')
        .text.strip().strip('()')
        for i in company
    ]

    company_work_domain1_location1 = [
        i.find('span', class_='companyCardWrapper__interLinking')
        .text.strip().split('|')
        for i in company
    ]

    company_work_domain1 = [i[0] for i in company_work_domain1_location1]

    location1 = [i[1] if len(i) > 1 else None for i in company_work_domain1_location1]

    # Combine lists into rows
    for n, r, rev, dom, loc in zip(name1, rating1, review_count1, company_work_domain1, location1):

        data.append({
            "name": n,
            "rating": r,
            "reviews": rev,
            "company_type": dom,
            "location": loc
        })


    print(f"Page {page} scraped")

    time.sleep(2)


df = pd.DataFrame(data)

path = os.path.dirname(__file__)
path_file_movies = os.path.join(path, '../../4_save_export_file/company.csv')
df.to_csv(path_file_movies, index=False)

print("Data saved successfully")