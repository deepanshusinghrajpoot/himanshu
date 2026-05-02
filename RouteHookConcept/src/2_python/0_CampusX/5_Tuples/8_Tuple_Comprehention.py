# Tuple Comprehension
#-------------------

# lll Python does not support tuple comprehension.
#     It creates a generator, which must be converted using tuple() (type conversion).



# Syntax
#-------

# new_tuple = tuple(expression for item in iterable if condition)


# Advantages of Tuple Comprehension
#-----------------------------------

# 1. It is concise and readable.
# 2. It creates immutable sequences.
# 3. It reduces multiple lines of code to a single expression.
# 4. Useful when you don’t want data to be modified accidentally.



# Ques:- Add numbers from 1 to 10 into a tuple
#---------------------------------------------

t = tuple(i for i in range(1, 11))
print(t)  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)



# Ques :- Scalar multiplication on a vector
#------------------------------------------

v = (2, 3, 4)
s = -3

t = tuple(s * i for i in v)
print(t)  # (-6, -9, -12)



# Ques:- Add square of each element to itself
#--------------------------------------------

t = (1, 3, 5, 6)

t = tuple(i + i*i for i in t)
print(t)  # (2, 12, 30, 42)



# Ques:- Print all numbers divisible by 5 from 1 to 50
#------------------------------------------------------

t = tuple(i for i in range(1, 51) if i % 5 == 0)
print(t)  # (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)



# Ques:- Find languages that start with letter 'p'
#-------------------------------------------------

language = ("java", "python", "php", "c", "javaScript")

t = tuple(i for i in language if i[0] == 'p')
print(t)  # ('python', 'php')



# Ques:- Nested if with Tuple Comprehension
#------------------------------------------

# Select fruits that exist in basket and also start with letter 'a'

basket = ('apple', 'guava', 'chery', 'banana')
my_fruits = ('apple', 'kiwi', 'grapes', 'banana')

t = tuple(fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a'))
print(t)  # ('apple',)



# Ques:- Cartesian product using Tuple Comprehension
#---------------------------------------------------

# Combine two tuples and multiply each pair of elements

t1 = (1, 2, 3, 4)
t2 = (5, 6, 7, 8)

t = tuple(i * j for i in t1 for j in t2)
print(t)
# (5, 6, 7, 8, 10, 12, 14, 16, 15, 18, 21, 24, 20, 24, 28, 32)



# Ques:- Convert all strings in a tuple to uppercase
#---------------------------------------------------

words = ('apple', 'banana', 'apple', 'cherry')

t = tuple(word.upper() for word in words)
print(t)  # ('APPLE', 'BANANA', 'APPLE', 'CHERRY')



# Ques:- Flatten a nested tuple into a single tuple
#--------------------------------------------------

nested_tuple = ((1, 2), (2, 3), (3, 4))

t = tuple(i for sub in nested_tuple for i in sub)
print(t)  # (1, 2, 2, 3, 3, 4)
