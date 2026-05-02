# NumPy Array vs Python List
# ==========================

# (1) Memory Occupied by Python List
# ==================================

import sys

# Create a Python list
a = [i for i in range(10000000)]

# Check memory size of list
print(sys.getsizeof(a))

# Example Output
# 89095160