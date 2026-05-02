

'''

Data Accessing
==============

In this step, the data is to be understood more deeply. Before implementing methods to clean it, 
you will definitely need to have a better idea about what the data is about.


Types of Unclean Data
---------------------

There are 2 kinds of unclean data

1. Dirty Data (Data with Quality issues): Dirty data, also known as low quality data. Low quality data has content issues.
   
      (i). Duplicated Data
      (ii). Missing Data
      (iii). Corrupt Data : mean data is not load
      (iv). Inaccurate Data : suppose that height column and this column has negative value

2. Messy Data (Data with tidiess issues): Messy data, also known as untidy data. Untidy data has structural issues. Tidy data has the following properties:
      
      (i). Each variable forms a column
            eg 
               Table 1 : Messy Data

               | year | china | india | pakistan |
               -----------------------------------
               | 1950 | 635   | 7235  | 24       |
               | 1960 | 3684  | 7237  | 7236     |
            
  
               Table 2 : Tidy Data

               | year | country | population |
               -------------------------------
               | 1950 | india   | 2164245    |  
               | 1960 | china   | 63521      |


      (ii). Each observation forms a row
      (iii). Each observational unit forms a table


'''





'''
# =========================================================
# lll In Data Assessing step our goal are
# =========================================================
# • Understand the structure of the dataset
# • Identify data quality issues
# • Identify structural (tidiness) issues


# Important
# ---------
# Before cleaning data, we must first understand what
# problems exist in the dataset.


# =========================================================
# Types of Unclean Data
# =========================================================

# We are know that there are two main kinds of unclean data:

# 1. Dirty Data
# 2. Messy Data


# ---------------------------------------------------------
# 1. lll Dirty Data (Data with Quality Issues)
# ---------------------------------------------------------

# Dirty data refers to low-quality data that contains
# incorrect, incomplete, or inconsistent values.

# In simple words:
# Dirty data has problems with the "content" of data.

# lll Common Types of Dirty Data
# ------------------------------

# (i) Duplicated Data
# -------------------
# When the same record appears multiple times
# in the dataset.

# Example
# -------
# | ID | Name |
# |----|------|
# | 1  | Ram  |
# | 1  | Ram  |   ← duplicate row


# (ii) Missing Data
# -----------------
# When some values are not present in the dataset.

# Example
# -------
# | Name | Age |
# |------|-----|
# | Ram  | 25  |
# | Shyam| NaN |   ← missing value


# (iii) Corrupt Data(not loaded properly)
# ---------------------------------------
# Corrupt data means data that is damaged, unreadable,
# or not loaded properly.

# Example
# -------
# • File cannot be opened
# • Encoding errors
# • Data not loaded correctly


# (iv) Inaccurate Data
# --------------------
# When data values are logically incorrect.

# Example
# -------
# Suppose there is a "Height" column:

# | Name | Height |
# |------|--------|
# | Ram  | 170    |
# | Amit | -165   |   ← impossible value


# =========================================================
# 2. Messy Data (Data with Tidiness Issues)
# =========================================================

# Messy data is also called "Untidy Data".

# In simple words:
# Messy data has problems with the "structure" of data.

# Tidy data follows specific rules.


# ---------------------------------------------------------
# lll we know that Properties of Tidy Data
# ---------------------------------------------------------


# (i) Each Variable Forms a Column
# --------------------------------

# Messy Data Example

# Table 1 : Messy Data
#
# | year | china | india | pakistan |
# -----------------------------------
# | 1950 | 635   | 7235  | 24       |
# | 1960 | 3684  | 7237  | 7236     |


# Tidy Data Example

# Table 2 : Tidy Data
#
# | year | country | population |
# -------------------------------
# | 1950 | india   | 2164245    |
# | 1960 | china   | 63521      |


# (ii) Each Observation Forms a Row
# ---------------------------------
# Each row should represent one observation or record.

# Example

# | Name | Age | City |
# |------|-----|------|
# | Ram  | 25  | Delhi|
# | Amit | 30  | Noida|


# (iii) Each Observational Unit Forms a Table
# -------------------------------------------
# Different types of data should be stored in
# separate tables.

# Example

# Table 1 → Customer Information
# Table 2 → Orders
# Table 3 → Payments


# =========================================================
# Important Points for Quick Revision
# =========================================================

# ✔ Dirty Data → Content problems
# ✔ Messy Data → Structural problems
# ✔ Data assessing is done before data cleaning
# ✔ Goal is to identify issues in the dataset


# =========================================================
# One-Line Interview Answer
# =========================================================

# Data Assessing is the process of examining the dataset
# to identify data quality issues (dirty data) and
# structural issues (messy data) before cleaning.
'''







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


print(patients.info())
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
 4   address       491 non-null    str
 5   city          491 non-null    str
 6   state         491 non-null    str
 7   zip_code      491 non-null    float64
 8   country       491 non-null    str
 9   contact       491 non-null    str
 10  birthdate     503 non-null    str
 11  weight        503 non-null    float64
 12  height        503 non-null    int64
 13  bmi           503 non-null    float64
dtypes: float64(3), int64(2), str(9)
memory usage: 55.1 KB
None
'''


print(treatments.info())
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
 6   hba1c_change  171 non-null    float64
dtypes: float64(3), str(4)
memory usage: 15.4 KB
None
'''


print(adverse_reactions.info())
'''
<class 'pandas.DataFrame'>
RangeIndex: 34 entries, 0 to 33
Data columns (total 3 columns):
 #   Column            Non-Null Count  Dtype
---  ------            --------------  -----
 0   given_name        34 non-null     str
 1   surname           34 non-null     str
 2   adverse_reaction  34 non-null     str
dtypes: str(3)
memory usage: 948.0 bytes
None
'''

print(treatments_cut.info())
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
 6   hba1c_change  42 non-null     float64
dtypes: float64(3), str(4)
memory usage: 4.0 KB
None
'''




'''

Step 1
========

Here we are get information about dataset by manager or teammate.

Dataset Description
-------------------

This dataset is about clinical dataset 

















Step 2
=======

We are need to write summary for our data.

Summary
-------

This is a dataset about 500 patients of which 350 patients participated in a clinical trial. None of the patients were using Novodra (a popular injectable insulin) 
or Auralin (the oral insulin being researched) as their primary source of insulin before. All were experiencing elevated HbA1c levels.

All 350 patients were treated with Novodra to establish a baseline HbA1c level and insulin dose. After 4 weeks, which isn’t enough time to capture all the change in HbA1c 
that can be attributed by the switch to Auralin or Novodra:

175 patients switched to Auralin for 24 weeks
175 patients continued using Novodra for 24 weeks
Data about patients feeling some adverse effects is also recorded.













Step 3
=======

We are need to write a proper column descriptions

Column Descriptions
-------------------

Table -> patients:
..................

patient_id: the unique identifier for each patient in the Master Patient Index (i.e. patient database) 
            of the pharmaceutical company that is producing Auralin

assigned_sex: the assigned sex of each patient at birth (male or female)

given_name: the given name (i.e. first name) of each patient

surname: the surname (i.e. last name) of each patient

address: the main address for each patient

city: the corresponding city for the main address of each patient

state: the corresponding state for the main address of each patient

zip_code: the corresponding zip code for the main address of each patient

country: the corresponding country for the main address of each patient (all United states for this clinical trial)

contact: phone number and email information for each patient

birthdate: the date of birth of each patient (month/day/year). The inclusion criteria for this clinical trial is age >= 18 
           (there is no maximum age because diabetes is a growing problem among the elderly population)

weight: the weight of each patient in pounds (lbs)

height: the height of each patient in inches (in)

bmi: the Body Mass Index (BMI) of each patient. BMI is a simple calculation using a person's height and weight. The formula is BMI = kg/m2 where kg is a person's weight in kilograms and m2 is their height in metres squared. A BMI of 25.0 or more is overweight, while the healthy range is 18.5 to 24.9. The inclusion criteria for this clinical trial is 16 >= BMI >= 38.








Table -> treatments and treatment_cut:
......................................

given_name: the given name of each patient in the Master Patient Index that took part in the clinical trial

surname: the surname of each patient in the Master Patient Index that took part in the clinical trial

auralin: the baseline median daily dose of insulin from the week prior to switching to Auralin (the number before the dash) 
         and the ending median daily dose of insulin at the end of the 24 weeks of treatment measured over the 24th week of 
         treatment (the number after the dash). Both are measured in units (shortform 'u'), which is the international unit of measurement and the standard measurement for insulin.

novodra: same as above, except for patients that continued treatment with Novodra

hba1c_start: the patient's HbA1c level at the beginning of the first week of treatment. HbA1c stands for Hemoglobin A1c. 
             The HbA1c test measures what the average blood sugar has been over the past three months. It is thus a powerful way to get an 
             overall sense of how well diabetes has been controlled. Everyone with diabetes should have this test 2 to 4 times per year. Measured in %.

hba1c_end: the patient's HbA1c level at the end of the last week of treatment

hba1c_change: the change in the patient's HbA1c level from the start of treatment to the end, i.e., hba1c_start - hba1c_end. For Auralin to be deemed effective, 
              it must be "noninferior" to Novodra, the current standard for insulin. This "noninferiority" is statistically defined as the upper bound of the 95% confidence 
              interval being less than 0.4% for the difference between the mean HbA1c changes for Novodra and Auralin (i.e. Novodra minus Auralin).

              





              

Table -> adverse_reactions
..........................

given_name: the given name of each patient in the Master Patient Index that took part in the clinical trial 
            and had an adverse reaction (includes both patients treated Auralin and Novodra)

surname: the surname of each patient in the Master Patient Index that took part in the clinical 
         trial and had an adverse reaction (includes both patients treated Auralin and Novodra)

adverse_reaction: the adverse reaction reported by the patient










Step 4
======

if we are get any additional information then add it

Additional information:
------------------------

Insulin resistance varies person to person, which is why both starting median daily dose and ending median daily dose are required, i.e., to calculate change in dose.

It is important to test drugs and medical products in the people they are meant to help. People of different age, race, sex, and ethnic group must be included in clinical trials. 
This diversity is reflected in the patients table.






Step 5
========

Now start the Assessment
-------------------------

Type of Assessment
...................

There are 2 types of assessment styles

. Manual - Looking through the data manually in google sheets or excel sheets
. Programmatic - By using pandas functions such as info(), describe() or sample()


Step in Assessment
...................

There are 2 steps involved in Assessment

. Discover
. Document

'''



# export data for manual assessment

path_fol_0_DataSet = os.path.join(path, './0_DataSet/clinical_trials.xlsx')
'''
with pd.ExcelWriter(path_fol_0_DataSet) as writer:
    patients.to_excel(writer, sheet_name='patients')
    treatments.to_excel(writer, sheet_name='treatments')
    treatments_cut.to_excel(writer, sheet_name='treatment_cut')
    adverse_reactions.to_excel(writer, sheet_name='adverse_reactions')
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
   - patient_id = 9 has misspelled name 'Dsvid' intead of David
   - state col sometimes contain full name and some times abbrivietation
   - zip col has entries with 4 digit
   - There are 12 missing value in address, city, state,  zip_code, country, contact cols
   - incorrect data type assign to sex, zip, birthdate
   - duplicate entries by the name of John Doe 
   - One patient has weight = 48 pound
   - One patient has height = 27 inches
   

   Table - 'Treatments' & 'Treatment_cut'
   - given_name and surname col is all lower case
   - remove u from auralin and novodra cols
   - - in auralin and novodra col treated as nan
   - missing values in hba1c_change col
   - 1 duplicate entry by the name joseph day
   - in hba1c_change 9 instead of 4
   

   Table - 'Adverse_reactions'
   - given_name and surname col is all lower case

2. Messy Data

   Table - 'Patients'
   - contact col contains both phone and email

   
   Table - 'Treatments' & 'Treatment_cut'
   - auralin and novodra cols should be split into 2 cols start and end dose
   - merge both table
   

   Table - 'Adverse_reactions'
   - This table should not exist independently
   
'''



# Extract information about missing and data type for programmatic assessment using info
#---------------------------------------------------------------------------------------

# (i) patients
#...............

print(patients.info())
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
 4   address       491 non-null    str
 5   city          491 non-null    str
 6   state         491 non-null    str
 7   zip_code      491 non-null    float64
 8   country       491 non-null    str
 9   contact       491 non-null    str
 10  birthdate     503 non-null    str
 11  weight        503 non-null    float64
 12  height        503 non-null    int64
 13  bmi           503 non-null    float64
dtypes: float64(3), int64(2), str(9)
memory usage: 55.1 KB
None
'''


print(patients[patients['address'].isnull()])
'''
     patient_id assigned_sex given_name      surname address city state  zip_code country contact   birthdate  weight  height   bmi
209         210       female     Lalita  Eldarkhanov     NaN  NaN   NaN       NaN     NaN     NaN   8/14/1950   143.4      62  26.2
219         220         male         Mỹ        Quynh     NaN  NaN   NaN       NaN     NaN     NaN    4/9/1978   237.8      69  35.1
230         231       female  Elisabeth      Knudsen     NaN  NaN   NaN       NaN     NaN     NaN   9/23/1976   165.9      63  29.4
234         235       female    Martina    Tománková     NaN  NaN   NaN       NaN     NaN     NaN    4/7/1936   199.5      65  33.2
242         243         male       John      O'Brian     NaN  NaN   NaN       NaN     NaN     NaN   2/25/1957   205.3      74  26.4
249         250         male   Benjamin       Mehler     NaN  NaN   NaN       NaN     NaN     NaN  10/30/1951   146.5      69  21.6
257         258         male        Jin         Kung     NaN  NaN   NaN       NaN     NaN     NaN   5/17/1995   231.7      69  34.2
264         265       female   Wafiyyah       Asfour     NaN  NaN   NaN       NaN     NaN     NaN   11/3/1989   158.6      63  28.1
269         270       female     Flavia   Fiorentino     NaN  NaN   NaN       NaN     NaN     NaN   10/9/1937   175.2      61  33.1
278         279       female   Generosa        Cabán     NaN  NaN   NaN       NaN     NaN     NaN  12/16/1962   124.3      69  18.4
286         287         male      Lewis         Webb     NaN  NaN   NaN       NaN     NaN     NaN    4/1/1979   155.3      68  23.6
296         297       female        Chỉ          Lâm     NaN  NaN   NaN       NaN     NaN     NaN   5/14/1990   181.1      63  32.1
'''


# (ii) treatments
#.................

print(treatments.info())
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
 6   hba1c_change  171 non-null    float64
dtypes: float64(3), str(4)
memory usage: 15.4 KB
None
'''


# (iii) treatments_cut
#.....................

print(treatments_cut.info())
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
 6   hba1c_change  42 non-null     float64
dtypes: float64(3), str(4)
memory usage: 4.0 KB
None
'''



# (iv) adverse_reactions
#.......................

print(adverse_reactions.info())
'''
<class 'pandas.DataFrame'>
RangeIndex: 34 entries, 0 to 33
Data columns (total 3 columns):
 #   Column            Non-Null Count  Dtype
---  ------            --------------  -----
 0   given_name        34 non-null     str
 1   surname           34 non-null     str
 2   adverse_reaction  34 non-null     str
dtypes: str(3)
memory usage: 948.0 bytes
None
'''





# Extract information about duplicate value for programmatic assessment using duplicated
#----------------------------------------------------------------------------------------


# (i) patients
#...............
print(patients.duplicated().sum()) # 0

print(patients['patient_id'].duplicated().sum()) # 0

print(patients.duplicated(subset=['given_name','surname']).sum()) # 5

print(patients[patients.duplicated(subset=['given_name','surname'])])
'''
     patient_id assigned_sex given_name surname          address      city  ...        country                      contact birthdate weight height   bmi
229         230         male       John     Doe  123 Main Street  New York  ...  United States  johndoe@email.com1234567890  1/1/1975  180.0     72  24.4    
237         238         male       John     Doe  123 Main Street  New York  ...  United States  johndoe@email.com1234567890  1/1/1975  180.0     72  24.4    
244         245         male       John     Doe  123 Main Street  New York  ...  United States  johndoe@email.com1234567890  1/1/1975  180.0     72  24.4    
251         252         male       John     Doe  123 Main Street  New York  ...  United States  johndoe@email.com1234567890  1/1/1975  180.0     72  24.4    
277         278         male       John     Doe  123 Main Street  New York  ...  United States  johndoe@email.com1234567890  1/1/1975  180.0     72  24.4    

[5 rows x 14 columns]
'''




# (ii) treatments
#.................

print(treatments.duplicated().sum()) # 1

print(treatments[treatments.duplicated()])
'''
    given_name surname    auralin novodra  hba1c_start  hba1c_end  hba1c_change
136     joseph     day  29u - 36u       -          7.7       7.19           NaN
'''

print(treatments[treatments.duplicated(subset=['given_name','surname'])])
'''
    given_name surname    auralin novodra  hba1c_start  hba1c_end  hba1c_change
136     joseph     day  29u - 36u       -          7.7       7.19           NaN
'''



# (iii) treatments_cut
#.....................

print(treatments_cut.duplicated().sum()) # 0

print(treatments_cut.duplicated(subset=['given_name','surname']).sum()) # 0



# (iv) adverse_reactions
#.......................

print(adverse_reactions.duplicated().sum()) # 0

print(adverse_reactions.duplicated(subset=['given_name','surname']).sum()) # 0





# Extract information form programmatic assessment using describe
#-----------------------------------------------------------------


# (i) patients
#...............

print(patients.describe())
'''
       patient_id      zip_code      weight      height         bmi
count  503.000000    491.000000  503.000000  503.000000  503.000000  
mean   252.000000  49084.118126  173.434990   66.634195   27.483897  
std    145.347859  30265.807442   33.916741    4.411297    5.276438  
min      1.000000   1002.000000   48.800000   27.000000   17.100000  
25%    126.500000  21920.500000  149.300000   63.000000   23.300000  
50%    252.000000  48057.000000  175.300000   67.000000   27.200000  
75%    377.500000  75679.000000  199.500000   70.000000   31.750000  
max    503.000000  99701.000000  255.900000   79.000000   37.700000 
'''


# weight :-  48.800000 pound == 21 kg
# height :- 63 inches = 5.2 foot
# So, issu in the data
print(patients[patients['weight'] == 48.800000])
'''
     patient_id assigned_sex given_name   surname              address  ...                                    contact   birthdate  weight height   bmi
210         211       female    Camilla  Zaitseva  4689 Briarhill Lane  ...  330-202-2145CamillaZaitseva@superrito.com  11/26/1938    48.8     63  19.1      

[1 rows x 14 columns]
'''




# height :- 27 inches = 2.25 foot
# weight :- 192.3 pound = 89.947367 kg
# So, issu in the data
print(patients[patients['height'] == 27])
'''
   patient_id assigned_sex given_name  surname               address  ...                          contact  birthdate  weight height   bmi
4           5         male        Tim  Neudorf  1428 Turkey Pen Lane  ...  334-515-7487TimNeudorf@cuvox.de  2/18/1928   192.3     27  26.1

[1 rows x 14 columns]
'''




# (ii) treatments
#.................

print(treatments.describe())
'''
       hba1c_start   hba1c_end  hba1c_change
count   280.000000  280.000000    171.000000
mean      7.985929    7.589286      0.546023
std       0.568638    0.569672      0.279555
min       7.500000    7.010000      0.200000
25%       7.660000    7.270000      0.340000
50%       7.800000    7.420000      0.380000
75%       7.970000    7.570000      0.920000
max       9.950000    9.580000      0.990000
'''

# I thigs here is problem hba1c_start sudden chage 75% (7.970000) to max (9.950000) let check
print(treatments.sort_values('hba1c_start'))
'''
    given_name      surname    auralin    novodra  hba1c_start  hba1c_end  hba1c_change
113       kari  laatikainen  39u - 43u          -         7.50       7.11           NaN
126     jowita   wiśniewska          -  22u - 23u         7.50       7.08          0.92
270       mika   martinsson  34u - 43u          -         7.50       7.17          0.33
53      nasser      mansour          -  33u - 31u         7.51       7.06          0.95
105     finlay     sheppard          -  31u - 30u         7.51       7.17          0.34
..         ...          ...        ...        ...          ...        ...           ...
25      benoît       bonami          -  44u - 43u         9.82       9.40          0.92
171    justyna    kowalczyk  24u - 34u          -         9.84       9.44           NaN
81      robert       wagner  43u - 49u          -         9.84       9.52          0.32
75   mackenzie        mckay          -  44u - 43u         9.87       9.48          0.39
166      annie        allen  36u - 42u          -         9.95       9.58          0.37

[280 rows x 7 columns]
'''
# here is no problem because there are no any oulyer



# I thigs here is problem hba1c_change sudden chage 50% (0.380000) to 75% (0.920000) let check
print(treatments.sort_values('hba1c_change', na_position='first'))
'''
    given_name      surname    auralin    novodra  hba1c_start  hba1c_end  hba1c_change
0     veronika     jindrová  41u - 48u          -         7.63       7.20           NaN
2     yukitaka     takenaka          -  39u - 36u         7.68       7.25           NaN
8        saber       ménard          -  54u - 54u         8.08       7.70           NaN
9         asia      woźniak  30u - 36u          -         7.76       7.37           NaN
10      joseph          day  29u - 36u          -         7.70       7.19           NaN
..         ...          ...        ...        ...          ...        ...           ...
49     jackson      addison          -  42u - 42u         7.99       7.51          0.98
17        gina         cain          -  36u - 36u         7.88       7.40          0.98
138    giovana        rocha          -  23u - 21u         7.87       7.38          0.99
32       laura  ehrlichmann          -  43u - 40u         7.95       7.46          0.99
245         wu         sung          -  47u - 48u         7.61       7.12          0.99

[280 rows x 7 columns]
'''

# 7.99 - 7.51 = 0.48   | given : 0.98     this is wrong 
# 7.88 - 7.40 = 0.48   | given : 0.98     this is wrong
# 7.95 - 7.46 = 0.49   | given : 0.99     this is wrong
# So, in hba1c_change 9 instead of 4





# (iii) treatments_cut
#.....................


print(treatments_cut.describe())
'''
       hba1c_start  hba1c_end  hba1c_change
count    70.000000  70.000000     42.000000
mean      7.838000   7.443143      0.518810
std       0.423007   0.418706      0.270719
min       7.510000   7.020000      0.280000
25%       7.640000   7.232500      0.340000
50%       7.730000   7.345000      0.370000
75%       7.860000   7.467500      0.907500
max       9.910000   9.460000      0.970000
'''

# same problem like treatments table





#==================================================
# Note - Assessing Data is an Iterative Process
#==================================================
