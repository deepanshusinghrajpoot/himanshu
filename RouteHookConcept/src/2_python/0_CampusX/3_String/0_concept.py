# Strings in Python
#===================

# Strings are a sequence of characters.
# In Python, strings are specifically a sequence of Unicode characters.
# Strings are immutable (cannot be changed after creation).





# Topics to learn about Strings
#-------------------------------

# 1. Creating Strings
# 2. Accessing Strings
# 3. Adding Characters to Strings
# 4. Editing Strings
# 5. Deleting Strings
# 6. Operations on Strings
# 7. String Functions




# String - is immutable data type
#        - There for we can not perform adding, editing, and deleting operation on string
#        - We can only perform read operation





# Operation on string
#----------------------

# Arithmetic operation(+,*)
# Relational operation
# Logical operation
# Loop on string
# Membership operation


# Logical operation

# '' (empty string) - false
# 'dh' (non empty string) - true

print('' and 'world') # ''
print('' or 'world' ) # world

print('hellow' and 'world')  # 'world'
print('hellow' or 'world') # 'hellow'


# Common Function
#----------------

# len
# max
# min
# sorted



# capitalize/title/upper/lower/swapcase
#---------------------------------------

s = "hellow world"

print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.swapcase())

#Hellow world
#Hellow World
#HELLOW WORLD
#hellow world
#HELLOW WORLD



# count/find/index
#------------------

# count :- return the frequency of char
# find :- return index and 'no error' if not found (return -1)
# index :- return index and raise error if not found


print(s.count('h'))
print(s.find('z'))  
print(s.index('w'))


# 1
# -1
# 5



# endswith/startwith - give boolean
#-------------------

print(s.endswith('a')) # False
print(s.startswith('h')) # True





# format (order matter)
#--------

name = 'nitish'
gender = 'male'

print('Hi my name is {} and I am a {}.'.format(name, gender))

# Hi my name is nitish and I am a male.