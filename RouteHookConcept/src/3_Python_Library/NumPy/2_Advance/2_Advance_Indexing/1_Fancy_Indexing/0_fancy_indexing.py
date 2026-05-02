import numpy as np


# Fancy Indexing
# ==============

# Fancy indexing allows us to access multiple specific
# rows or columns using a list of indexes.


a = np.arange(16).reshape(4, 4)

print(a)

# Output
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]



# Question 1: Find rows 1, 2, and 3
# ----------------------------------

# Normal indexing cannot select multiple non-consecutive rows easily.

# Fancy Indexing
print(a[[1, 2, 3]])

# Output
# [[ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]



# Question 2: Find all rows and columns 0, 2, and 3
# --------------------------------------------------

# Fancy Indexing
print(a[:, [0, 2, 3]])

# Output
# [[ 0  2  3]
#  [ 4  6  7]
#  [ 8 10 11]
#  [12 14 15]]