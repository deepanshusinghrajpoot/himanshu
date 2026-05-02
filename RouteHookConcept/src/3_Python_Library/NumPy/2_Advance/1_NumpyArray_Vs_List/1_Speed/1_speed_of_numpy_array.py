import numpy as np
import time


# Speed of NumPy Array
# ====================

# Create two NumPy arrays
a = np.arange(10000000)
b = np.arange(10000000, 20000000)

# Start time
timeStart = time.time()

# Vectorized addition
c = a + b

# End time
print(time.time() - timeStart)

# Example Output
# 0.042000532150268555



# Why NumPy Array is Faster
# =========================

# 1. NumPy uses C language implementation internally
# ---------------------------------------------------
# Most NumPy operations are executed in optimized C code,
# which makes them much faster than Python loops.


# 2. Static Array
# ----------------
# NumPy arrays are fixed-size (static).
# Once created, their size cannot change.


# 3. Continuous Memory Allocation
# --------------------------------
# NumPy stores elements in a continuous block of memory.


# 4. Non-Referential Storage
# ---------------------------
# Python lists store references (addresses) to objects.
# NumPy arrays store actual values directly in memory.


# 5. Vectorized Operations
# -------------------------
# NumPy performs operations on entire arrays at once
# without using explicit Python loops.