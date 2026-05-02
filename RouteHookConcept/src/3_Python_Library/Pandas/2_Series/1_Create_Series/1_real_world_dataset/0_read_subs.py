# ==========================================
# Pandas Series: Using Real-World Dataset
# ==========================================

import pandas as pd
import os

# ✅ Definition:
# A Pandas Series can be created directly from a CSV file.

# - lll read_csv() reads the CSV file as a DataFrame by default.
# - lll squeeze() converts a single-column DataFrame into a Series.

# ------------------------------------------------
# Step 1: Get the CSV file path
# ------------------------------------------------
# Get current file directory
base_dir = os.path.dirname(__file__)
print(base_dir)
# Example Output:
# c:\path\to\your\project\Python_Library\Pandas\2_Series\1_Create_Series

# Build correct path to dataset
file_path = os.path.join(base_dir, '../../../1_Dataset/subs.csv')
print(file_path)
# Example Output:
# c:\path\to\your\project\1_Dataset\subs.csv

# ------------------------------------------------
# Step 2: Read CSV
# ------------------------------------------------
# By default, read_csv returns a DataFrame
df = pd.read_csv(file_path)
print(type(df))
# Output: <class 'pandas.DataFrame'>

# Convert single-column DataFrame into Series using squeeze()
subs = pd.read_csv(file_path).squeeze("columns")
print(type(subs))
# Output: <class 'pandas.Series'>

# ------------------------------------------------
# Step 3: Inspect the Series
# ------------------------------------------------
print(subs)
# Output (example):
# 0       48
# 1       57
# 2       40
# ...
# 364    172
# Name: Subscribers gained, Length: 365, dtype: int64

# ✅ Quick Notes:
# - The Series name comes from the column name of the CSV.
# - squeeze() removes unnecessary dimensions:
#   | Method                | Removes     | Condition     |
#   | --------------------- | ----------- | ------------- |
#   | `.squeeze("columns")` | Column axis | Only 1 column |
#   | `.squeeze("index")`   | Row axis    | Only 1 row    |
#   | `.squeeze()`          | Any axis    | If size = 1   |

# ⚡ Tip:
# Use squeeze() when you know the CSV has a single column.