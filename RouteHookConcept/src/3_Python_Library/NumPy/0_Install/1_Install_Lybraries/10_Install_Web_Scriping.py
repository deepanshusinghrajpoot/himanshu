


"""
✅ ✅ Correct Way to Install BeautifulSoup (BS4) (Windows)


🔹 Step 1 — Check Python Version
---------------------------------

Open Command Prompt:

    python --version

Make sure it shows:
    Python 3.14.x


If multiple versions exist:

    py --list



🔹 Step 2 — Upgrade pip (Recommended)
--------------------------------------

    py -3.14 -m pip install --upgrade pip


Why update pip?
---------------

• Fixes old bugs  
• Supports latest packages  
• Prevents installation errors  



🔹 Step 3 — Install BeautifulSoup (BS4)
---------------------------------------

    py -3.14 -m pip install beautifulsoup4


👉 Always use:  py -3.14 -m pip  
👉 Do NOT use:  pip install beautifulsoup4  
   (It may install in the wrong Python environment)



🔹 Step 4 — Install Requests Library (Needed for Web Scraping)
---------------------------------------------------------------

    py -3.14 -m pip install requests



🔹 Step 5 — Verify Installation
--------------------------------

    py -3.14 -m pip show beautifulsoup4


Or open Python:

    py -3.14


Then inside Python:

    from bs4 import BeautifulSoup
    print("BeautifulSoup Installed Successfully")


If no error appears → BeautifulSoup installed correctly ✅

"""









"""
===========================================
BeautifulSoup (BS4) in Python
===========================================

Definition
----------
BeautifulSoup (BS4) is a Python library used for
web scraping. It parses HTML or XML documents
and allows developers to easily extract data
from web pages.

It converts raw HTML into a tree structure
so that specific elements can be searched
and accessed easily.

-------------------------------------------
Installation
-------------------------------------------

pip install beautifulsoup4
pip install requests

-------------------------------------------
Basic Workflow of Web Scraping
-------------------------------------------

Website
   ↓
Requests Library (fetch webpage)
   ↓
BeautifulSoup (parse HTML)
   ↓
Extract required data
   ↓
Store in CSV / Database / Pandas

-------------------------------------------
Example Code
-------------------------------------------


import requests
from bs4 import BeautifulSoup

# URL of webpage
url = "https://example.com"

# send request to website
response = requests.get(url)

# parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# extract page title
title = soup.title.text

print(title)



-------------------------------------------
Important BS4 Functions
-------------------------------------------

find()        → returns first matching tag
find_all()    → returns all matching tags
select()      → CSS selector based search
get_text()    → extracts text from HTML
prettify()    → formats HTML structure

Example:
soup.find("h1")
soup.find_all("p")

-------------------------------------------
Use Cases
-------------------------------------------

• Scraping company data
• Collecting product prices
• Extracting tables from websites
• Gathering datasets for analysis

-------------------------------------------
Interview Definition
-------------------------------------------

BeautifulSoup (BS4) is a Python library used
to parse HTML/XML documents and extract data
from websites for web scraping.
-------------------------------------------
"""