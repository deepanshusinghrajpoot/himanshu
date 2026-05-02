# Dictionary Operations
#=========================

# Dictionary support the following operations:
#---------------------------------------
# There are two ways to perform operations on a dictionary:
# 2. Membership operations (in, not in)
# 3. Looping operations



# Membership operation
#----------------------

dic = {'name':'Deepanshu', 'age':20}

print('name' in dic)      # True
print('age' not in dic)   # False


# Iteration
#-----------

dic = {'name':'Deepanshu', 'age':20}

for key in dic:
    print(dic[key], end=" ")   # Deepanshu 20
