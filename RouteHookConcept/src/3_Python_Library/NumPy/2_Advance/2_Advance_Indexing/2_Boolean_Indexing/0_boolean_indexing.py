import numpy as np


# Boolean Indexing (Very Useful)
# ==============================

# Boolean indexing is used to filter elements based on conditions.

# Note:
# 1. It returns a 1D NumPy array.
# 2. When working with boolean conditions in NumPy,
#    we use bitwise operators (&, |, ~) instead of
#    Python logical operators (and, or, not).


# Create a random NumPy array
a = np.random.randint(1, 100, 24).reshape(6, 4)

print(a)

# Example Output
# [[95 29 93 37]
#  [35  7  5 48]
#  [26  4 50 43]
#  [48 33 56 47]
#  [34  7 20 94]
#  [17 16 29 15]]



# Question 1: Find all numbers greater than 50
# --------------------------------------------

print(a > 50)

# Output (Boolean array)
# [[ True False  True False]
#  [False False False False]
#  [False False False False]
#  [False False  True False]
#  [False False False  True]
#  [False False False False]]

# Filter values
print(a[a > 50])

# [95 93 56 94]



# Question 2: Find all even numbers
# ---------------------------------

print(a[a % 2 == 0])

# Example Output
# [48 26  4 50 48 56 34 20 94 16]



# Question 3: Find numbers greater than 50 AND even
# -------------------------------------------------

print(a[(a > 50) & (a % 2 == 0)])

# [56 94]



# Question 4: Find numbers divisible by 7
# ---------------------------------------

print(a[a % 7 == 0])

# [35  7 56  7]



# Question 5: Find numbers NOT divisible by 7
# -------------------------------------------

print(a[~(a % 7 == 0)])

# [95 29 93 37  5 48 26  4 50 43 48 33 47 34 20 94 17 16 29 15]