'''






## What is a Data Warehouse? ✅
===============================

"A Data Warehouse is a centralized storage system where all organizational data is stored for analysis and reporting."

lll A Data Warehouse is a centralized storage system.
    - It combines data from **multiple sources**
    - Used for **reporting, analytics, and business intelligence**

**Example:**

An organization stores:
- Transactions Data  
- Sales Data  
- Budget Data  
- Marketing Data  
- HR Data  



---

## Database vs Data Warehouse ✅
================================

"Database and Data Warehouse serve different purposes."

### 🔹 lll Database
           - Stores **real-time operational data**
           - Used by applications for daily operations

           
**Problem:**  
lll "When we Run heavy queries on a live database can slow down performance."



---

### 🔹 Data Warehouse
- Used for **analytics and reporting**
- Handles **large, complex queries efficiently**

**Solution:**  
"To avoid performance issues, we move data into a Data Warehouse."


---
## Flow ✅

Application → Database → ETL → Data Warehouse
---


## Explanation (Interview Style) ✅
-----------------------------------

"In real-world scenarios, data is not directly analyzed from the database."

- Data is **pulled in bulk** from the database  
- This happens at **scheduled intervals** (batch processing)  
- **No transformation at source**, raw data is extracted first  
- Data Warehouse checks for **new or updated data**  
- ETL is used to process and organize the data  

---

## ETL Process ✅
------------------

"We use ETL for moving and transforming data."

- **Extract** → Fetch data from database  
- **Transform** → Clean, filter, and structure data  
- **Load** → Store into Data Warehouse  

---

## Key Interview Points ✅
--------------------------

"To summarize:"

- Data Warehouse is used for **analytics, reporting, BI**
- It reduces **load on operational database**
- Supports **historical data storage**
- Uses **ETL process** for data movement










OLTP (Online Transaction Processing)
OLAP (Online Analytical Processing)



'''