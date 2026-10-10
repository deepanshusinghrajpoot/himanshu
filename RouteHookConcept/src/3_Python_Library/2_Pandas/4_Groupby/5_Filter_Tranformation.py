# filter()
# --------

# Interview Definition
#lll  filter() is a pandas GroupBy method used to keep or remove
#     entire groups based on a condition.

# Syntax
# dataframe.groupby(column).filter(function)

# Important Points
# 1. filter() works on groups.
# 2. It returns all rows of groups that satisfy the condition.
# 3. If a group fails the condition, the entire group is removed.

# Example

import pandas as pd

df = pd.DataFrame({
    "Dept": ["IT", "IT", "HR", "HR", "Sales"],
    "Salary": [50000, 60000, 30000, 35000, 25000]
})

result = df.groupby("Dept").filter(
    lambda x: x["Salary"].mean() > 40000
)

print(result)

# Output
#     Dept  Salary
# 0    IT   50000
# 1    IT   60000










# transform()
# -----------

# Interview Definition
# transform() is a pandas GroupBy method used to perform
# calculations on each group and return an output having
# the same size as the original DataFrame.

# Syntax
# dataframe.groupby(column)[target_column].transform(function)

# Important Points
# 1. Output size remains the same as the original DataFrame.
# 2. Used when we want a group-level calculation for every row.
# 3. Does not reduce rows.

# Example

import pandas as pd

df = pd.DataFrame({
    "Dept": ["IT", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 30000, 35000]
})

df["Dept_Avg"] = df.groupby("Dept")["Salary"].transform("mean")

print(df)

# Output
#     Dept  Salary  Dept_Avg
# 0    IT   50000   55000.0
# 1    IT   60000   55000.0
# 2    HR   30000   32500.0
# 3    HR   35000   32500.0








# filter() vs transform()
# -----------------------

# filter()
# --------
# Used to keep or remove entire groups based on a condition.
# Groups that fail the condition are completely discarded.

# transform()
# -----------
# Used to perform group-wise calculations and return a result
# with the same number of rows as the original DataFrame.

# Key Differences
#
# filter()   -> Can reduce the number of rows.
# transform() -> Never changes the number of rows.
#
# filter()   -> Returns a filtered DataFrame.
# transform() -> Returns a Series/DataFrame of same size.
#
# filter()   -> Works on entire groups.
# transform() -> Works row-wise using group calculations.
#
# Common Use:
# filter()   -> Remove unwanted groups.
# transform() -> Add group statistics like mean, max, min, rank.