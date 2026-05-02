
'''

When site not give api to get data then we get data from site using webscriping
--------------------------------------------------------------------------------

eg: from :- AmbitionBox



What is Web Scraping?
---------------------

Web scraping is a technique used to extract or collect data from websites automatically.

Instead of copying data manually from a website,
a program sends a request to the website, downloads the HTML content,
and extracts the required information.

Workflow
--------

Website
   ↓
Send Request (requests library)
   ↓
Get HTML Content
   ↓
Parse HTML (BeautifulSoup / bs4)
   ↓
Extract Data
   ↓
Store in CSV / Database / Pandas

Example Tools Used
------------------

requests        → send request to website
BeautifulSoup   → parse HTML and extract data
Selenium        → scrape dynamic websites
Pandas          → store and analyze scraped data

Example Use Cases
-----------------

• Collect product prices from e-commerce websites
• Extract company information
• Gather news headlines
• Collect datasets for analysis

Interview Definition
--------------------

Web scraping is the process of automatically extracting data
from websites using programs or scripts.







Header
--------

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

| Part                    | Meaning                                                                                   |
| ----------------------- | ----------------------------------------------------------------------------------------- |
| **Mozilla/5.0**         | Old browser compatibility identifier. Almost all browsers include this for compatibility. |
| **Windows NT 10.0**     | Operating system → Windows 10                                                             |
| **Win64; x64**          | 64-bit system architecture                                                                |
| **AppleWebKit/537.36**  | Browser engine used to render webpages                                                    |
| **(KHTML, like Gecko)** | Indicates compatibility with the Gecko rendering engine                                   |
| **Chrome/122.0.0.0**    | Browser name and version (Google Chrome)                                                  |
| **Safari/537.36**       | WebKit-based browser compatibility                                                        |




BeautifulSoup
-------------

"""
===========================================
BeautifulSoup HTML Parsing
===========================================

Code
----

soup = BeautifulSoup(response.text, "html.parser")


Meaning
-------

This line converts the raw HTML of a webpage into a structured format
so Python can easily search and extract elements from the page.


Explanation
-----------

response.text
    • Contains the HTML source code of the webpage
    • It is returned by the requests library

BeautifulSoup()
    • Parses the HTML document
    • Converts it into a tree-like structure
    • Allows easy navigation and searching of tags

"html.parser"
    • Built-in Python parser
    • Reads and interprets the HTML structure


Workflow
--------

Website
   ↓
requests.get()
   ↓
response.text  (raw HTML)
   ↓
BeautifulSoup(response.text, "html.parser")
   ↓
Structured HTML tree
   ↓
Extract data (title, links, tables, etc.)


Example
-------

import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)


Output
------

Example Domain


Interview Definition
--------------------

BeautifulSoup parses HTML content and converts it into a structured
object so we can easily extract data from a webpage.
"""




'''


import pandas as pd
import requests
import time
from bs4 import BeautifulSoup
import os


url = "https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page=1"

# Browser headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

# Send request with header
response = requests.get(url, headers=headers)

print(response)        # Should show <Response [200]>
print(response.text)   # HTML content


# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")


print(soup.prettify())

print(soup.find_all('h1'))
'''
[<h1 class="companyListing__collectionTopHeadingCont" data-v-507d085f=""><div class="companyListing__collectionTopHeading" data-v-507d085f="">
                                        Top Companies in
                                </div> <div class="companyListing__collectionIndiaHeading" data-v-507d085f=""><img data-v-507d085f="" height="12" src="https://static.ambitionbox.com/static/loc/loc-star.png" width="12"/>
                                        INDIA
                                        <img data-v-507d085f="" height="12" src="https://static.ambitionbox.com/static/loc/loc-star.png" width="12"/></div></h1>]
'''


print(soup.find_all('h1')[0].text)
'''

                                        Top Companies in

                                        INDIA
'''


for i in soup.find_all('h2'):
    print(i.text.strip())

'''
Companies in India
TCS
Accenture
Wipro
Cognizant
Capgemini
HDFC Bank
Infosys
ICICI Bank
HCLTech
Tech Mahindra
Genpact
Teleperformance
Jio
Axis Bank
Concentrix Corporation
Amazon
iEnergizer
Reliance Retail
LTIMindtree
IBM
Popular Collections by Industries
Popular Collections by Cities
Popular Collections by Roles
'''


for i in soup.find_all('h2', class_='companyCardWrapper__companyName'):
    print(i.text.strip())
'''
TCS
Accenture
Wipro
Cognizant
Capgemini
HDFC Bank
Infosys
ICICI Bank
HCLTech
Tech Mahindra
Genpact
Teleperformance
Jio
Axis Bank
Concentrix Corporation
Amazon
iEnergizer
Reliance Retail
LTIMindtree
IBM
'''


# Now we go to each parent div
# -----------------------------


print("======================================")
company = soup.find_all('div', class_='companyCardWrapper__metaInformation')

print(len(company))

for i in company:
    print(i.find('h2').text.strip())
'''
TCS
Accenture
Wipro
Cognizant
Capgemini
HDFC Bank
Infosys
ICICI Bank
HCLTech
Tech Mahindra
Genpact
Teleperformance
Jio
Axis Bank
Concentrix Corporation
Amazon
iEnergizer
Reliance Retail
LTIMindtree
IBM
'''


name = []
rating = []
review_count = []
company_work_domain = []
location = []


for i in company:
    name.append(i.find('h2').text.strip())
    rating.append(i.find('div', class_='rating_star_container').text.strip())
    review_count.append(i.find('span', class_='companyCardWrapper__companyRatingCount').text.strip().strip().strip('()'))

    company_work_domain_and_location = i.find('span', class_='companyCardWrapper__interLinking').text.strip().split('|')
    company_work_domain.append(company_work_domain_and_location[0])
    location.append(company_work_domain_and_location[1])


print(name)
'''
['TCS', 'Accenture', 'Wipro', 'Cognizant', 'Capgemini', 'HDFC Bank', 'Infosys', 'ICICI Bank', 'HCLTech', 'Tech Mahindra',
 'Genpact', 'Teleperformance', 'Jio', 'Axis Bank', 'Concentrix Corporation', 'Amazon', 'iEnergizer', 'Reliance Retail',
 'LTIMindtree', 'IBM']
'''

print(rating)
'''
['3.3', '3.7', '3.6', '3.6', '3.7', '3.8', '3.5', '3.9', '3.4', '3.4', '3.6', '3.8', '4.4', '3.6', '3.6', 
 '3.9', '4.6', '3.9', '3.6', '3.9']
'''


print(review_count)
'''
['1.1L', '72.2k', '64.2k', '60.5k', '52.2k', '51.3k', '47.9k', '45.3k', '45.1k', '42.8k', '41.4k', '37.3k', 
 '33.4k', '32.6k', '31.7k', '31k', '27.3k', '27.2k', '26.1k', '25.5k']
'''


print(company_work_domain)
'''
['IT Services & Consulting ', 'IT Services & Consulting ', 'IT Services & Consulting ', 'IT Services & Consulting ', 
 'IT Services & Consulting ', 'Banking ', 'IT Services & Consulting ', 'Banking ', 'IT Services & Consulting ', 'IT Services & Consulting ', 'Analytics & KPO ', 'BPO ', 'Telecom ', 'Banking ', 'BPO ', 'Internet ', 'BPO ', 'Retail ', 'IT Services & Consulting ', 'IT Services & Consulting ']
'''


print(location)
'''
[' Bengaluru +439 other locations', ' Bengaluru +255 other locations', ' Hyderabad +371 other locations', 
' Hyderabad +232 other locations', ' Bengaluru +182 other locations', ' Mumbai +1837 other locations', 
' Bengaluru +248 other locations', ' Mumbai +1440 other locations', ' Chennai +231 other locations', 
' Hyderabad +330 other locations', ' Hyderabad +181 other locations', ' Mumbai +255 other locations', 
' Mumbai +1967 other locations', ' Mumbai +1510 other locations', ' Bengaluru +178 other locations', 
' Bengaluru +521 other locations', ' Noida +52 other locations', ' Mumbai +1157 other locations', 
' Bengaluru +145 other locations', ' Bengaluru +161 other locations']
'''


name1 = [i.find('h2').text.strip() for i in company]
rating1 = [i.find('div', class_='rating_star_container').text.strip()for i in company]
review_count1 = [i.find('span', class_='companyCardWrapper__companyRatingCount').text.strip().strip().strip('()') for i in company]
company_work_domain1 = [i.find('span', class_='companyCardWrapper__interLinking').text.strip().split('|')[0] for i in company]
location1 = [i.find('span', class_='companyCardWrapper__interLinking').text.strip().split('|')[1] for i in company]


print(name1)
'''
['TCS', 'Accenture', 'Wipro', 'Cognizant', 'Capgemini', 'HDFC Bank', 'Infosys', 'ICICI Bank', 'HCLTech', 'Tech Mahindra',
 'Genpact', 'Teleperformance', 'Jio', 'Axis Bank', 'Concentrix Corporation', 'Amazon', 'iEnergizer', 'Reliance Retail',
 'LTIMindtree', 'IBM']
'''

print(rating1)
'''
['3.3', '3.7', '3.6', '3.6', '3.7', '3.8', '3.5', '3.9', '3.4', '3.4', '3.6', '3.8', '4.4', '3.6', '3.6', 
 '3.9', '4.6', '3.9', '3.6', '3.9']
'''

print(review_count1)
'''
['1.1L', '72.2k', '64.2k', '60.5k', '52.2k', '51.3k', '47.9k', '45.3k', '45.1k', '42.8k', '41.4k', '37.3k', 
 '33.4k', '32.6k', '31.7k', '31k', '27.3k', '27.2k', '26.1k', '25.5k']
'''

print(company_work_domain1)
'''
['IT Services & Consulting ', 'IT Services & Consulting ', 'IT Services & Consulting ', 'IT Services & Consulting ', 
 'IT Services & Consulting ', 'Banking ', 'IT Services & Consulting ', 'Banking ', 'IT Services & Consulting ', 'IT Services & Consulting ', 'Analytics & KPO ', 'BPO ', 'Telecom ', 'Banking ', 'BPO ', 'Internet ', 'BPO ', 'Retail ', 'IT Services & Consulting ', 'IT Services & Consulting ']
'''

print(location1)
'''
[' Bengaluru +439 other locations', ' Bengaluru +255 other locations', ' Hyderabad +371 other locations', 
' Hyderabad +232 other locations', ' Bengaluru +182 other locations', ' Mumbai +1837 other locations', 
' Bengaluru +248 other locations', ' Mumbai +1440 other locations', ' Chennai +231 other locations', 
' Hyderabad +330 other locations', ' Hyderabad +181 other locations', ' Mumbai +255 other locations', 
' Mumbai +1967 other locations', ' Mumbai +1510 other locations', ' Bengaluru +178 other locations', 
' Bengaluru +521 other locations', ' Noida +52 other locations', ' Mumbai +1157 other locations', 
' Bengaluru +145 other locations', ' Bengaluru +161 other locations']
'''


d = {'name': name1, 'rating': rating1, 'reviews': review_count1,
     'company_type': company_work_domain1, 'location': location1}


print(pd.DataFrame(d))
'''
                      name rating reviews               company_type                         location
0                      TCS    3.3    1.1L  IT Services & Consulting    Bengaluru +439 other locations
1                Accenture    3.7   72.2k  IT Services & Consulting    Bengaluru +255 other locations
2                    Wipro    3.6   64.2k  IT Services & Consulting    Hyderabad +371 other locations
3                Cognizant    3.6   60.5k  IT Services & Consulting    Hyderabad +232 other locations
4                Capgemini    3.7   52.2k  IT Services & Consulting    Bengaluru +182 other locations
5                HDFC Bank    3.8   51.3k                   Banking      Mumbai +1837 other locations
6                  Infosys    3.5   47.9k  IT Services & Consulting    Bengaluru +248 other locations
7               ICICI Bank    3.9   45.3k                   Banking      Mumbai +1440 other locations
8                  HCLTech    3.4   45.1k  IT Services & Consulting      Chennai +231 other locations
9            Tech Mahindra    3.4   42.8k  IT Services & Consulting    Hyderabad +330 other locations
10                 Genpact    3.6   41.4k           Analytics & KPO    Hyderabad +181 other locations
11         Teleperformance    3.8   37.3k                       BPO       Mumbai +255 other locations
12                     Jio    4.4   33.4k                   Telecom      Mumbai +1967 other locations
13               Axis Bank    3.6   32.6k                   Banking      Mumbai +1510 other locations
14  Concentrix Corporation    3.6   31.7k                       BPO    Bengaluru +178 other locations
15                  Amazon    3.9     31k                  Internet    Bengaluru +521 other locations
16              iEnergizer    4.6   27.3k                       BPO         Noida +52 other locations
17         Reliance Retail    3.9   27.2k                    Retail      Mumbai +1157 other locations
18             LTIMindtree    3.6   26.1k  IT Services & Consulting    Bengaluru +145 other locations
19                     IBM    3.9   25.5k  IT Services & Consulting    Bengaluru +161 other locations
'''


print(pd.DataFrame(d).info())
'''
<class 'pandas.DataFrame'>
RangeIndex: 20 entries, 0 to 19
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   name          20 non-null     str
 1   rating        20 non-null     str
 2   reviews       20 non-null     str
 3   company_type  20 non-null     str
 4   location      20 non-null     str
dtypes: str(5)
memory usage: 932.0 bytes
None
'''

