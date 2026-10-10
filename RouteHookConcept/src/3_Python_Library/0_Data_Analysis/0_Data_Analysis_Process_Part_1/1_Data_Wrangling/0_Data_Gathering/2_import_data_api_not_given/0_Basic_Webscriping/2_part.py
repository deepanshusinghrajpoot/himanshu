
import numpy as np
import pandas as pd
import os 




path = os.path.dirname(__file__)

path_file_4_save_export_file = os.path.join(path, '../../4_save_export_file/company.csv')


company = pd.read_csv(path_file_4_save_export_file)


print(company)