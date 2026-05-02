import numpy as np
import pandas as pd



# ==================================================
# Creating DataFrame using Dictionary
# ==================================================

# Definition (Interview Friendly)
# A DataFrame can be created using a dictionary where
# keys represent column names and values represent
# the data of that column.

# Important Points
# • Dictionary keys → column names
# • Dictionary values → column data (list, array, etc.)
# • Each list should have the same number of elements
# • Very commonly used method in real projects



# Creating DataFrame using dictionary
#=====================================

student_dict = {
    'iq':[100, 90, 120, 80],
    'marks':[80, 70, 100, 50],
    'package':[10, 7, 14, 2]
}

print(pd.DataFrame(student_dict))

# Output
#     iq  marks  pakage
# 0  100     80      10
# 1   90     70       7
# 2  120    100      14
# 3   80     50       2



# ==================================================
# Explanation
# ==================================================

# 'iq'      → column containing IQ scores
# 'marks'   → column containing student marks
# 'package' → column containing placement package

# Each list forms a column in the DataFrame.



# ==================================================
# Quick Revision
# ==================================================

# Syntax
# pd.DataFrame(dictionary)

# Dictionary Keys   → Columns
# Dictionary Values → Column data