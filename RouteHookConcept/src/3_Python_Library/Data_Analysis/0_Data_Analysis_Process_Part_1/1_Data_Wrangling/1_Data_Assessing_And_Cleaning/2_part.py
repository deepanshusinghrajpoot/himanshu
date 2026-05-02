'''

# Data Quality Dimensions (Dirty Data Types)
# =========================================

## Definition
-------------
**Data Quality Dimensions** are criteria used to identify problems in data (dirty data).  
They help in **cleaning, validating, and preparing data for analysis (EDA / ETL).**

---

## lll There are four types of Dirty Data
-----------------------------------------

### (1) Completeness
--------------------
**Definition:** Checks whether **data is missing or not**.

🔹 Important Points:
- Missing values → NULL, NaN, empty fields
- Affects analysis and model performance

🔹 Example:
- Age = NULL  
- Salary column has empty values

---

lll (2) Validity
  ----------------
    **Definition:** Checks whether **data follows correct rules or constraints**.

🔹 Important Points:
- Data must follow **data type, range, format rules**
- Invalid data is logically incorrect

🔹 Example:
- Height = -170 cm ❌  
- Duplicate Patient ID ❌  
- Email without “@” ❌  

---

### (3) Accuracy
----------------
**Definition:** Data is **valid in format but incorrect in real-world sense**.

🔹 Important Points:
- Hard to detect (needs domain knowledge)
- Data looks correct but is unrealistic

🔹 Example:
- Adult weight = 1 kg ❌  
- Salary = 1 crore for fresher ❌  

---

### (4) Consistency
-------------------
**Definition:** Same data is **represented differently in different places**.

🔹 Important Points:
- Causes confusion during analysis
- Needs standardization

🔹 Example:
- "New York", "NY", "New Yourk" ❌  
- "Male", "M", "male"  

---

## Important Concepts
---------------------
- Dirty data affects:
  - ❗ Data Analysis (EDA)
  - ❗ Machine Learning models
  - ❗ Business decisions

- Data Cleaning steps:
  - Handle missing values
  - Remove/validate incorrect data
  - Standardize formats
  - Remove duplicates

---

## Final Step (Very Important)
------------------------------
After identifying issues:

👉 **Label / Tag the data problems**  
👉 Then perform **Data Cleaning (Preprocessing)**

---

## Interview Quick Points
-------------------------
✔ Data Quality Dimensions = Completeness, Validity, Accuracy, Consistency  
✔ Completeness → Missing data  
✔ Validity → Rule violation  
✔ Accuracy → Real-world correctness  
✔ Consistency → Same data, different formats  
✔ Important in **EDA, ETL pipelines, DataOps**
'''


'''
Manual Assessment
-----------------
Looking through the data manually in google sheets or excel sheets


Programmatic Assessment
-----------------------

1. head and tail
2. sample
3. info
4. isnull
5. duplicated
6. describe



Issues with the dataset
-----------------------

1. Dirty Data

   Table - 'Patients'
   - patient_id = 9 has misspelled name 'Dsvid' intead of David                             "Accuracy"     
   - state col sometimes contain full name and some times abbrivietation                    "Consistency"
   - zip col has entries with 4 digit                                                       "Validity"
   - There are 12 missing value in address, city, state,  zip_code, country, contact cols   "Completeness"
   - incorrect data type assign to sex, zip, birthdate                                      "Validity"
   - duplicate entries by the name of John Doe                                              "Accuracy"
   - One patient has weight = 48 pound                                                      "Accuracy"
   - One patient has height = 27 inches                                                     "Accuracy"
   

   Table - 'Treatments' & 'Treatment_cut'
   - given_name and surname col is all lower case    "Consistency"
   - remove u from auralin and novodra cols          "Validity"
   - - in auralin and novodra col treated as nan     "Validity"
   - missing values in hba1c_change col              "Completeness"
   - 1 duplicate entry by the name joseph day        "Accuracy"
   - in hba1c_change 9 instead of 4                  "Accuracy"
   

   Table - 'Adverse_reactions'
   - given_name and surname col is all lower case    "Consistency"

   
2. Messy Data

   Table - 'Patients'
   - contact col contains both phone and email

   
   Table - 'Treatments' & 'Treatment_cut'
   - auralin and novodra cols should be split into 2 cols start and end dose
   - merge both table

   Table - 'Adverse_reactions'
   - This table should not exist independently

'''








# Order of severity
#==================

# Completeness <- Validity <- Accuracy <- Consistency







# Data Cleaning Order
#=====================

# 1. Quality -> Completeness
# 2. Tidiness(Messy Data)
# 3. Quality -> Validity
# 4. Quality -> Accuracy
# 5. Quality -> Consistency




# Steps involved in Data cleaning
#=================================

# Define
# Code
# Test




#=====================================================================================================
# Always make sure to create a copy of your pandas dataframe before you start the cleaning process
#=====================================================================================================




import pandas as pd
import numpy as np

import os



path = os.path.dirname(__file__)

path_file_patients = os.path.join(path, './0_DataSet/patients.csv')
path_file_treatments = os.path.join(path, './0_DataSet/treatments.csv')
path_file_adverse_reactions = os.path.join(path, './0_DataSet/adverse_reactions.csv')
path_file_treatments_cut = os.path.join(path, './0_DataSet/treatments_cut.csv')



patients = pd.read_csv(path_file_patients)
treatments = pd.read_csv(path_file_treatments)
adverse_reactions = pd.read_csv(path_file_adverse_reactions)
treatments_cut = pd.read_csv(path_file_treatments_cut)





patients_df = patients.copy()
treatments_df = treatments.copy()
treatments_cut_df = treatments_cut.copy()
adverse_reactions_df = adverse_reactions.copy()


#------------------------------------------------------------------

# Define
'''
replace all missing values of patients df 
columns address, city, state, country, contact with no data 
and column zip_code with 0
'''

# code
patients_df.fillna({
    'address': 'No data',
    'city': 'No data',
    'state': 'No data',
    'zip_code': 0,
    'country':'No data',
    'contact':'No data'
}, inplace=True)


# test
print(patients_df.info())
'''
<class 'pandas.DataFrame'>
RangeIndex: 503 entries, 0 to 502
Data columns (total 14 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   patient_id    503 non-null    int64
 1   assigned_sex  503 non-null    str
 2   given_name    503 non-null    str
 3   surname       503 non-null    str
 4   address       503 non-null    str
 5   city          503 non-null    str
 6   state         503 non-null    str
 7   zip_code      503 non-null    float64
 8   country       503 non-null    str
 9   contact       503 non-null    str
 10  birthdate     503 non-null    str
 11  weight        503 non-null    float64
 12  height        503 non-null    int64
 13  bmi           503 non-null    float64
dtypes: float64(3), int64(2), str(9)
memory usage: 55.1 KB
None
'''

#------------------------------------------------------------------

# Define 
'''
subtract hba1c_start and hba1c_end to get all hba1c_change
'''

# Code
treatments_df['hba1c_change'] = treatments_df['hba1c_start'] - treatments_df['hba1c_end']
treatments_cut_df['hba1c_change'] = treatments_cut_df['hba1c_start'] - treatments_cut_df['hba1c_end']

# Test
print(treatments_df.info())
'''
<class 'pandas.DataFrame'>
RangeIndex: 280 entries, 0 to 279
Data columns (total 7 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   given_name    280 non-null    str
 1   surname       280 non-null    str
 2   auralin       280 non-null    str
 3   novodra       280 non-null    str
 4   hba1c_start   280 non-null    float64
 5   hba1c_end     280 non-null    float64
 6   hba1c_change  280 non-null    float64
dtypes: float64(3), str(4)
memory usage: 15.4 KB
None
'''
print(treatments_cut_df.info())
'''
<class 'pandas.DataFrame'>
RangeIndex: 70 entries, 0 to 69
Data columns (total 7 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   given_name    70 non-null     str
 1   surname       70 non-null     str
 2   auralin       70 non-null     str
 3   novodra       70 non-null     str
 4   hba1c_start   70 non-null     float64
 5   hba1c_end     70 non-null     float64
 6   hba1c_change  70 non-null     float64
dtypes: float64(3), str(4)
memory usage: 4.0 KB
None
'''



#----------------------------------------------------------------------------------

# Define
'''
in patients table we will use regex to separate email and phone
'''

# Code 
# extract email
patients_df['email'] = patients_df['contact'].str.extract(r'([A-Za-z]+[A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,})')

# extract phone
patients_df['phone'] = patients_df['contact'].str.extract(r'(\+?\d[\d\s\-\(\)]{7,}\d)')

# drop original column
patients_df.drop(columns='contact', inplace=True)

# replace NaN values
patients_df['phone'] = patients_df['phone'].fillna('No data')
patients_df['email'] = patients_df['email'].fillna('No data')

print(patients_df.info())
'''
<class 'pandas.DataFrame'>
RangeIndex: 503 entries, 0 to 502
Data columns (total 15 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   patient_id    503 non-null    int64
 1   assigned_sex  503 non-null    str
 2   given_name    503 non-null    str
 3   surname       503 non-null    str
 4   address       503 non-null    str
 5   city          503 non-null    str
 6   state         503 non-null    str
 7   zip_code      503 non-null    float64
 8   country       503 non-null    str
 9   birthdate     503 non-null    str
 10  weight        503 non-null    float64
 11  height        503 non-null    int64
 12  bmi           503 non-null    float64
 13  email         503 non-null    str
 14  phone         503 non-null    str
dtypes: float64(3), int64(2), str(10)
memory usage: 59.1 KB
None
'''

#---------------------------------------------------------------------------------------------

# Define
'''
concate treatments and treatment_cut
'''

# Code
treatments_df = pd.concat([treatments_df, treatments_cut_df])

print(treatments_df.info())