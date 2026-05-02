
import pandas as pd


import os 




path = os.path.dirname(__file__)

path_file_employee = os.path.join(path, '../../../../../Pandas/1_Dataset/employee.txt')

print(pd.read_csv(path_file_employee, sep='\t', names=['ID', 'Name', 'Department', 'Salary']))
'''
           ID  Name Department  Salary
1      Name_1    49    Finance  111560
2      Name_2    28  Marketing   55124
3      Name_3    31         IT   72036
4      Name_4    53    Finance   92290
5      Name_5    41         IT  108451
..        ...   ...        ...     ...
96    Name_96    24    Finance  106245
97    Name_97    55    Finance  102065
98    Name_98    40    Finance  114315
99    Name_99    36    Finance   67909
100  Name_100    22  Marketing   80681

[100 rows x 4 columns]
'''