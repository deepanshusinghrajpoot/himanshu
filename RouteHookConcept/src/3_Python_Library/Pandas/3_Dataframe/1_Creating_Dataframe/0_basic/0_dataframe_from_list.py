import numpy as np
import pandas as pd




# ==================================================
# Creating DataFrame
# ==================================================

# Definition (Interview Friendly)
# A DataFrame can be created from different data structures
# such as lists, dictionaries, NumPy arrays, CSV files, etc.



# ==================================================
# Creating DataFrame using List (2D List)
# ==================================================

# Definition (Interview Friendly)
# A DataFrame can be created using a 2D list where
# each inner list represents a row of the table.

# Important Points
# • Outer list represents multiple rows
# • Inner list represents values of columns
# • "columns" parameter is used to name the columns



student_data = [
    [100, 80, 10],
    [90, 70, 7],
    [120, 100, 14],
    [80, 50, 2]
]


print(pd.DataFrame(student_data, columns=['iq', 'marks', 'pakage']))

# Output
#     iq  marks  pakage
# 0  100     80      10
# 1   90     70       7
# 2  120    100      14
# 3   80     50       2



# ==================================================
# Explanation
# ==================================================

# Column iq     → Intelligence score
# Column marks  → Student marks
# Column pakage → Placement package

# Each row represents data of one student.



# ==================================================
# Quick Revision
# ==================================================

# DataFrame creation syntax
# pd.DataFrame(data, columns=[...])

# student_data → list of rows
# columns → column names