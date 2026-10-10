# ==========================================
# Pandas Series: Creation from Dictionary
# ==========================================

import pandas as pd

# ✅ Definition:
# lll A Series can also be created from a dictionary.
#     - Keys → become the index
#     - Values → become the corresponding data

# Example: Student Marks
marks = {
    'math': 91,
    'science': 85,
    'hindi': 95,
    'social science': 82,
    'art': 86
}

marks_series = pd.Series(marks)
print(marks_series)
# Output:
# math              91
# science           85
# hindi             95
# social science    82
# art               86
# dtype: int64

# ⚡ Quick Tips:
# - Dictionary keys automatically become index labels.
# - Series from dict is useful for labeled, unordered data.
# - You can also provide a custom order of indices if needed:
#   pd.Series(marks, index=['hindi','math','science','art','social science'])