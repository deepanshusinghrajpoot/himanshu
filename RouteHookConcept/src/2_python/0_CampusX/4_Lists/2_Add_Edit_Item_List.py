# Adding Items to a List
#======================


#lll There are three common ways to add elements to a list:
#----------------------------------------------------------
# 1. append() :- adds a single element at the end of the list
# 2. extend() :- adds multiple elements at the end of the list
# 3. insert() :- adds an element at a specific position




# 1. append() :- adds a single element at the end of the list
#------------------------------------------------------------

L = [1, 2, 3, 4, 5]

L.append(True)
print(L)  # [1, 2, 3, 4, 5, True]




# 2. extend() :- adds multiple elements at the end of the list
#-------------------------------------------------------------

# extend() adds each element of the iterable separately

L.extend([6, 7])
print(L)  # [1, 2, 3, 4, 5, True, 6, 7]

L.extend("delhi")
print(L)
# [1, 2, 3, 4, 5, True, 6, 7, 'd', 'e', 'l', 'h', 'i']




# 3. insert() :- adds an element at a specific position
#------------------------------------------------------

L.insert(0, 1000000)
print(L)
# [1000000, 1, 2, 3, 4, 5, True, 6, 7, 'd', 'e', 'l', 'h', 'i']





# How to edit items in a List
#============================

# lll There are two ways to edit element of a list
#-------------------------------------------------
# using indexing
# using slicing [included:excluded:jum] = [ _ , _ , _ , _ ]   :- same no of lement on bothside


# List elements can be updated using index or slicing

M = ["Deepanshu", 23, 4, 56, 78, 90]

M[0] = "Himanshu"
print(M)
# ['Himanshu', 23, 4, 56, 78, 90]

M[3:] = ["Ram", "Sayam", "Mohan"]
print(M)
# ['Himanshu', 23, 4, 'Ram', 'Sayam', 'Mohan']
