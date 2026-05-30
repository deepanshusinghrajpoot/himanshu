# Dictionary Functions
#======================

# len    -> gives total number of items in dictionary
# sorted -> returns a sorted list of keys (works for any data type)


d = {'name':'Deepanshu', 'age':22}

print(len(d))                 # 2

print(sorted(d))              # ['age', 'name']
print(sorted(d, reverse=True))# ['name', 'age']



# lll items / keys / values (V.V.V. Important)
#=========================================

# items :- returns key-value pairs as tuple inside a list
# keys :- returns all keys inside a list
# values :- returns all values inside a list



d = {'name':'Deepanshu', 'age':22, 'gender':'male'}

# items :- returns key-value pairs as tuple inside a list
#---------------------------------------------------------

print(d.items())  
# dict_items([('name', 'Deepanshu'), ('age', 22), ('gender', 'male')])


# keys :- returns all keys
#--------------------------

print(d.keys())  
# dict_keys(['name', 'age', 'gender'])


# values :- returns all values
#------------------------------

print(d.values())  
# dict_values(['Deepanshu', 22, 'male'])



# update :- adds new key-value pair if not present, updates value if key exists
#-------------------------------------------------------------------------------

d1 = {1:2, 3:4, 4:5}
d2 = {4:7, 6:9}

d1.update(d2)
print(d1)  # {1: 2, 3: 4, 4: 7, 6: 9}
