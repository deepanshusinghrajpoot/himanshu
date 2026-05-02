# Remaining List Functions
#-------------------------

# Some functions are universal
#-----------------------------

# These functions work on most iterables, including lists.

# len, min, max, sorted, sum are built-in functions in Python
#------------------------------------------------------------
# len    -> returns total number of elements
# min    -> returns smallest element
# max    -> returns largest element
# sorted -> returns a new sorted list and it has parameter reverse
# sum    -> return total sum of elements




L = [1, 2, 7, 3, 6, 5, 4]

print(len(L))      # 7
print(min(L))      # 1
print(max(L))      # 7
print(sum(L))      # 28

print(sorted(L))                # [1, 2, 3, 4, 5, 6, 7]
print(sorted(L, reverse=True))  # [7, 6, 5, 4, 3, 2, 1]




# count :- used to find frequency of an element
#----------------------------------------------

L = [1, 4, 4, 4, 5, 7]

print(L.count(4))  # 3
print(L.count(7))  # 1




# index :- used to find index of an element
#------------------------------------------

# Returns the first occurrence of the element

L = [11, 22, 55, 33, 44, 33]

print(L.index(33))  # 3
print(L.index(44))  # 4




# reverse :- used to reverse the list permanently
#------------------------------------------------

L = [111, 333, 555, 777]

L.reverse()
print(L)  # [777, 555, 333, 111]




# sort :- used to sort the list permanently
#------------------------------------------

L = [2, 1, 4, 3, 6, 5, 9, 8]

L.sort()
print(L)  # [1, 2, 3, 4, 5, 6, 8, 9]




# copy :- used to create a shallow copy of the list
#--------------------------------------------------

# Shallow copy means a new list is created,
# but nested objects are still shared.

L = [2222, 3333, 5555, 4444, [5555]]

print(L)
print(id(L))

L1 = L.copy()

print(L1)
print(id(L1))


L1[0] = 99999999
L1[-1][-1] = 1111111111

print(L)   # [2222, 3333, 5555, 4444, [1111111111]]
print(L1)  # [99999999, 3333, 5555, 4444, [1111111111]]
