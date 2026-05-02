# How to delete items from a List
#================================

# lll There are four common ways to delete elements from a list:
# 1. del :- deletes elements using index or slice
# 2. remove() :- deletes element by value
# 3. pop() :- deletes and returns an element
# 4. clear() :- deletes all elements from a list




# 1. del :- deletes elements using index or slice
#------------------------------------------------

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

del L[1]
print(L)  # [1, 3, 4, 5, 6, 7, 8, 9]

del L[-1]
print(L)  # [1, 3, 4, 5, 6, 7, 8]

del L[-2:]
print(L)  # [1, 3, 4, 5, 6]

del L    # deletes the entire list




# 2. remove() :- deletes element by value
#----------------------------------------

# It searches for the element and removes its first occurrence

L = [22, 33, 44, 55, 66, 77]

L.remove(66)
print(L)  # [22, 33, 44, 55, 77]




# 3. pop() :- deletes and returns an element
#-------------------------------------------

# lll If we don't provide index then, it delete the last element
#     If index is given, it delete the element at that index


L = ["himanshu", "shudhanshu", "divyanshu"]

L.pop(1)
print(L)  # ["himanshu", "divyanshu"]

L.pop()
print(L)  # ["himanshu"]




# 4. clear() :- deletes all elements from the list
#-------------------------------------------------

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

L.clear()
print(L)  # []
