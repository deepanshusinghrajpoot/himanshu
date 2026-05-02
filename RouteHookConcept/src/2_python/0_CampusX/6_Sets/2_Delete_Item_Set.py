# How to delete items from a Set
#===============================

# lll There are four common ways to delete elements from a set:
#---------------------------------------------------------------
# 1. remove()  :- Removes a specific element; raises error if not found
# 2. discard() :- Removes a specific element; no error if not found
# 3. pop()     :- Removes and returns a random element
# 4. clear()   :- Removes all elements from the set



# Note:
# del cannot delete individual elements from a set
# 5. del :- can only delete the entire set








# del
#-----

s = {1, 2, 3, 4, 5}
del s                 # deletes the whole set





# discard() :- delete item from set
#---------------------------------

s = {1, 2, 3, 4, 5}
s.discard(5)
print(s)              # {1, 2, 3, 4}

s.discard(999)        # no error

# Note :- discard() does NOT throw error if item not found





# remove() :- delete item from set
#--------------------------------

s = {1, 2, 3, 4, 5}
s.remove(5)
print(s)              # {1, 2, 3, 4}

# s.remove(999)       # throws error

# Note :- remove() throws error if item not found





# pop() :- delete random item
#----------------------------

s = {1, 2, 3, 4, 5}
s.pop()
print(s)              # random item removed

s.pop()
print(s)              # another random item removed





# clear() :- delete all items from set
#------------------------------------

s = {1, 2, 3, 4, 5}
s.clear()
print(s)              # set()
