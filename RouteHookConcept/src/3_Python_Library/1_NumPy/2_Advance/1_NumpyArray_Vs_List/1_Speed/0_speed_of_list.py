# NumPy Array vs Python List
# ==========================

# (1) Speed of Python List
# ========================

import time

# Create two Python lists
a = [i for i in range(10000000)]
b = [i for i in range(10000000, 20000000)]

c = []

# Start time
timeStart = time.time()

# Addition using loop
for i in range(len(a)):
    c.append(a[i] + b[i])

# End time
print(time.time() - timeStart)

# Example Output
# 5.007323980331421