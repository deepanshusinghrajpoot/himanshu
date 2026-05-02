# Adding item (add key-value pair)
#================================

d = {'name':'Deepanshu', 'age':22}

d['gender'] = 'male'
print(d)  # {'name': 'Deepanshu', 'age': 22, 'gender': 'male'}





# Delete item (remove key-value pair)
#====================================

# lll There are four common ways to delete elements from a dictionary:
#---------------------------------------------------------------------

# 1. del       :- deletes an element using a key (or deletes the whole dictionary)
# 2. pop()     :- deletes and returns an element using a key
# 3. popitem() :- deletes and returns the last inserted element
# 4. clear()   :- deletes all elements from a dictionary



# pop() :- delete item using key
#---------

d = {'name':'Deepanshu', 'age':22}

d.pop('age')
print(d)  # {'name': 'Deepanshu'}


# popitem() :- delete last item from dictionary
#------------

d = {'name':'Deepanshu', 'age':22, 'gender':'male', 'roll':'77777777777', 'weight':58}

d.popitem()
print(d)  # {'name': 'Deepanshu', 'age': 22, 'gender': 'male', 'roll': '77777777777'}


# del :- delete a specific item or the entire dictionary
#-------------------------------------------------------

d = {'name':'Deepanshu', 'age':22, 'gender':'male', 'roll':'77777777777', 'weight':58}

del d['gender']
print(d)  # {'name': 'Deepanshu', 'age': 22, 'roll': '77777777777', 'weight':58}

del d


# clear() :- delete all items from dictionary
#--------------------------------------------

d = {'name':'Deepanshu', 'age':22, 'gender':'male', 'roll':'77777777777', 'weight':58}

d.clear()
print(d)  # {}






# Edit dictionary
#================

d = {'name':'Deepanshu', 'age':22}

d['age'] = 20
print(d)  # {'name': 'Deepanshu', 'age': 20}
