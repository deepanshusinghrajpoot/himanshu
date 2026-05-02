# Difference between Lists and Tuples
#------------------------------------

# Syntax
# List   → []
# Tuple  → ()

# Mutability
# List   → Mutable (can be changed)
# Tuple  → Immutable (cannot be changed)

# Speed
# List   → Slower
# Tuple  → Faster (because immutable)

# Memory
# List   → Takes more memory
# Tuple  → Takes less memory

# Built-in Functionality
# List   → More built-in methods
# Tuple  → Fewer built-in methods

# Error Prone
# List   → More chances of accidental changes
# Tuple  → Safer, less error-prone

# Usability
# List   → Used when data needs to be modified
# Tuple  → Used when data should remain fixed






# Speed Comparison
#------------------

import time

L = list(range(1000000))
T = tuple(range(1000000))

start = time.time()
for i in L:
    i * 5
print("List time :- ", time.time() - start)

start = time.time()
for i in T:
    i * 5
print("Tuple time :- ", time.time() - start)

# Observation:
# Tuple iteration is slightly faster than list iteration






# Memory Comparison
#-------------------

import sys

L = list(range(10000))
T = tuple(range(10000))

print("List size :- ", sys.getsizeof(L))
print("Tuple size :- ", sys.getsizeof(T))

# Observation:
# Tuple consumes less memory than list
