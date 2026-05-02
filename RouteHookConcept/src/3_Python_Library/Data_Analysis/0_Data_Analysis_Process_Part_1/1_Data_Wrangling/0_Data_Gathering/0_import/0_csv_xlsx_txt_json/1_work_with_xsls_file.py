

import pandas as pd

import os


'''
📦 Role of openpyxl in Python

openpyxl is a Python library used to read, write, and modify Excel .xlsx files.

When you work with Excel files in pandas, pandas uses 
openpyxl as the engine to handle .xlsx files.
'''


path = os.path.dirname(__file__)

path_file_sales_target = os.path.join(path, '../../../../../Pandas/1_Dataset/sales-target.xlsx')


data = pd.read_excel(path_file_sales_target)

print(data)
'''
   Month of Order Date     Category  Target
0           2023-04-18    Furniture   10400
1           2023-05-18    Furniture   10500
2           2023-06-18    Furniture   10600
3           2023-07-18    Furniture   10800
4           2023-08-18    Furniture   10900
5           2023-09-18    Furniture   11000
6           2023-10-18    Furniture   11100
7           2023-11-18    Furniture   11300
8           2023-12-18    Furniture   11400
9           2023-01-19    Furniture   11500
10          2023-02-19    Furniture   11600
11          2023-03-19    Furniture   11800
12          2023-04-18     Clothing   12000
13          2023-05-18     Clothing   12000
14          2023-06-18     Clothing   12000
15          2023-07-18     Clothing   14000
16          2023-08-18     Clothing   14000
17          2023-09-18     Clothing   14000
18          2023-10-18     Clothing   16000
19          2023-11-18     Clothing   16000
20          2023-12-18     Clothing   16000
21          2023-01-19     Clothing   16000
22          2023-02-19     Clothing   16000
23          2023-03-19     Clothing   16000
24          2023-04-18  Electronics    9000
25          2023-05-18  Electronics    9000
26          2023-06-18  Electronics    9000
27          2023-07-18  Electronics    9000
28          2023-08-18  Electronics    9000
29          2023-09-18  Electronics    9000
30          2023-10-18  Electronics    9000
31          2023-11-18  Electronics    9000
32          2023-12-18  Electronics    9000
33          2023-01-19  Electronics   16000
34          2023-02-19  Electronics   16000
35          2023-03-19  Electronics   16000
'''




'''

# sheet_name
#============



# 1️⃣ Read default sheet (first sheet)
#-------------------------------------
data_1 = pd.read_excel(path_file_sales_target)
print(data_1)



# 2️⃣ Read sheet by name
#-----------------------
data_2 = pd.read_excel(path_file_sales_target, sheet_name='Sheet1')
print(data_2)



# 3️⃣ Read sheet by index
#-----------------------
data_3 = pd.read_excel(path_file_sales_target, sheet_name=0)
print(data_3)



# 4️⃣ Read multiple sheets
#-------------------------
data_4 = pd.read_excel(path_file_sales_target, sheet_name=['Sheet1','Sheet2'])
print(data_4)



# 5️⃣ Read all sheets
#--------------------
data_5 = pd.read_excel(path_file_sales_target, sheet_name=None)

print(data_5.keys())   # show sheet names


'''