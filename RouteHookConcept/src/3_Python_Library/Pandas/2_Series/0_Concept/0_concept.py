# ==========================================
# Pandas: Introduction & Series
# ==========================================

# 1️⃣ What is Pandas
# ------------------
# lll Pandas is a fast, powerful, flexible, and easy-to-use
#     open-source Python library for data analysis and manipulation.
#     Built on top of Python, it is widely used for working with tabular data.

# ⚡ Quick Tip:
# -  Pandas is use for reading/writing data, cleaning, transforming, and analyzing datasets.

# ==========================================


# 2️⃣ Pandas Series
# -----------------
# lll A Pandas Series is a 1-dimensional labeled array capable of holding data of any type (integer, float, string, etc.)

# Think of it like a single column in an Excel sheet or SQL table.





import pandas as pd


# Creating a Series from a list
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print("Series:\n", series)
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64

# Accessing values and index
print("Values:", series.values)  # [10 20 30 40 50]
print("Index:", series.index)    # RangeIndex(start=0, stop=5, step=1)

# ⚡ Quick Tips:
# - Each column in a DataFrame is a Series.
# - Series has both values and an index (labels).
# - Ideal for single column operations like arithmetic, filtering, and aggregation.

# ==========================================
# 3️⃣ Series in Tabular Data
# --------------------------
# lll When we are working with tabular data (DataFrame):
#     - Each column is a Series
#     - Multiple Series combine to form a DataFrame