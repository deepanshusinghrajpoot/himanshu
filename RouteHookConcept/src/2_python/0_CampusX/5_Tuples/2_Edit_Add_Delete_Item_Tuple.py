# Editing items
#================

t1 = (1, 2, 3, True, (4, 5))

# t1[0] = 10   ❌ gives error

# Note :
# Editing items in a tuple is NOT possible
# because tuple is immutable (just like string).





# Adding items
#================

t2 = (1, 2, 3, True, (4, 5))

# Note :
# We cannot add new items to a tuple
# because tuple does not allow modification
# after creation (immutable).





# Deleting items
#====================

t3 = (1, 2, 3, True, (4, 5))

# Note :
# Deleting individual items from a tuple is NOT allowed

# del t3[-1]   ❌ gives error


# But deleting the entire tuple is allowed

del t3   # ✅ whole tuple deleted
