# ==========================================
# Pandas Series: From kohli_ipl.csv Dataset
# ==========================================

import pandas as pd
import os

# ✅ Definition:
# A Pandas Series can be created from a CSV file column.
# - read_csv() reads the CSV into a DataFrame.
# - squeeze("columns") converts a single-column DataFrame into a Series.
# - If an index column is specified, it becomes the Series index.

# ------------------------------------------------
# Step 1: Get the CSV file path
# ------------------------------------------------
path_dir = os.path.dirname(__file__)
file_path = os.path.join(path_dir, "../../../1_Dataset/kohli_ipl.csv")
print(file_path)
# Example Output:
# c:\path\to\your\project\1_Dataset\kohli_ipl.csv

# ------------------------------------------------
# Step 2: Read CSV and convert to Series
# ------------------------------------------------
# Set 'match_no' as the index
kohli_ipl = pd.read_csv(file_path, index_col='match_no').squeeze("columns")
print(type(kohli_ipl))
# Output: <class 'pandas.Series'>

# ------------------------------------------------
# Step 3: Inspect the Series
# ------------------------------------------------
print(kohli_ipl)
# Example Output:
# match_no
# 1       1
# 2      23
# 3      13
# 4      12
# 5       1
# ...
# 211     0
# 212    20
# 213    73
# 214    25
# 215     7
# Name: runs, Length: 215, dtype: int64

# ✅ Quick Notes:
# - The column name ('runs') becomes the Series name.
# - The index column ('match_no') becomes the Series index.
# - Useful when working with time-series or sequential data.
# - squeeze() ensures the object is a Series when single-column CSV is used.

# ⚡ Tip:
# Always check index_col parameter to properly label your Series index.