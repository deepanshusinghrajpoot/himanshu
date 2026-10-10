import numpy as np
import sys


# Memory Occupied by NumPy Array
# ==============================

# Create a NumPy array with datatype int8
a = np.arange(10000000, dtype=np.int8)

# Check memory size
print(sys.getsizeof(a))

# Example Output
# 10000112



# Why NumPy Takes Less Memory
# ===========================

# 1. NumPy allows us to control the datatype of the array.
# -------------------------------------------------------
# We can choose the datatype according to our requirement,
# such as int8, int16, int32, or int64.


# 2. Python lists store integers as full Python objects.
# ------------------------------------------------------
# Each integer in a Python list uses more memory
# because it stores metadata and references.


# 3. NumPy arrays store elements in continuous memory.
# ----------------------------------------------------
# This reduces memory overhead and improves performance.



# Example Datatypes in NumPy
# ==========================

# int8   → 1 byte
# int16  → 2 bytes
# int32  → 4 bytes
# int64  → 8 bytes