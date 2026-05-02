# ==========================================
# Pandas Series Attributes
# ==========================================

import pandas as pd

# Sample Series
marks = {
    "math": 91,
    "science": 85,
    "social science": 82,
    "hindi": 82,
    "art": 82
}

marks_series = pd.Series(marks, name="Deepanshu ka marks")
print(marks_series)
# Output:
# math              91
# science           85
# social science    82
# hindi             82
# art               82
# Name: Deepanshu ka marks, dtype: int64

# ------------------------------------------------
# 1️⃣ size
# ------------------------------------------------
# Spoken Interview Definition:
# lll "Returns the total number of elements in the Series."
print(marks_series.size)
marks_series.index.name = "Subject_ID"
# Output: 5

# ------------------------------------------------
# 2️⃣ dtype
# ------------------------------------------------
# Spoken Interview Definition:
# lll "Shows the data type of the values stored in the Series."
print(marks_series.dtype)
# Output: int64

# ------------------------------------------------
# 3️⃣ name
# ------------------------------------------------
# Spoken Interview Definition:
# lll "Return name of the Series."
print(marks_series.name)
# Output: Deepanshu ka marks

# ------------------------------------------------
# 4️⃣ is_unique
# ------------------------------------------------
# Spoken Interview Definition:
# lll "Returns True if all the values in the Series are unique; otherwise False."
print(marks_series.is_unique)
# Output: False

# ------------------------------------------------
# 5️⃣ index
# ------------------------------------------------
# Spoken Interview Definition:
# lll "Represents the labels of the Series. Acts like row identifiers."
print(marks_series.index)
# Output: Index(['math', 'science', 'social science', 'hindi', 'art'], dtype='object')

# ------------------------------------------------
# 6️⃣ values
# ------------------------------------------------
# Spoken Interview Definition:
# lll "Returns the underlying data of the Series as a NumPy array."
print(marks_series.values)
# Output: [91 85 82 82 82]

# ------------------------------------------------
# Quick Tips:
# - Use these attributes to quickly inspect the structure and metadata of a Series.
# - size and dtype help in understanding the shape and type of data.
# - index and values are commonly used for iteration, slicing, or mapping.