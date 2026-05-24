




# List Comprehension
#------------------

# lll List comprehension is a shortest and readable way to create a list.
# It allows us to generate a new list in a single line of code.


# Syntax
#-------

# new_list = [expression for item in iterable if condition]


# Advantages of List Comprehension
#--------------------------------

# 1. It is faster and more efficient than traditional loops.
# 2. It reduces the number of lines of code.
# 3. It converts loop-based logic into a single readable expression.




# Ques:- Add numbers from 1 to 10 into a list
#--------------------------------------------

L = []

for i in range(1, 11):
    L.append(i)

print(L)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


L = [i for i in range(1, 11)]
print(L)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




# Ques :- Scalar multiplication on a vector
#------------------------------------------

# Multiply each element of the vector by a scalar value

v = [2, 3, 4]
s = -3

x = []
for i in v:
    x.append(i * s)

print(x)  # [-6, -9, -12]


Y = [s * i for i in v]
print(Y)  # [-6, -9, -12]




# Ques:- Add square of each element to itself
#--------------------------------------------

L = [1, 3, 5, 6]

L = [i + i*i for i in L]
print(L)  # [2, 12, 30, 42]




# Ques:- Print all numbers divisible by 5 from 1 to 50
#-----------------------------------------------------

L = [i for i in range(1, 51) if i % 5 == 0]
print(L)  # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]




# Ques:- Find languages that start with letter 'p'
#-------------------------------------------------

language = ["java", "python", "php", "c", "javaScript"]

language_start_with_p = [i for i in language if i[0] == 'p']
print(language_start_with_p)  # ['python', 'php']




# Ques:- Nested if with List Comprehension
#----------------------------------------

# Select fruits that exist in basket and also start with letter 'a'

basket = ['apple', 'guava', 'chery', 'banana']
my_fruits = ['apple', 'kiwi', 'grapes', 'banana']

my_fruits = [fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')]
print(my_fruits)  # ['apple']




# Ques:- Print a (3 x 3) matrix using nested list comprehension
#-------------------------------------------------------------

L = [[i * j for i in range(1, 4)] for j in range(1, 4)]
print(L)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]




# Ques:- Cartesian product using list comprehension
#--------------------------------------------------

# Combine two lists and multiply each pair of elements

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]

L = [i * j for i in L1 for j in L2]
print(L)
# [5, 6, 7, 8, 10, 12, 14, 16, 15, 18, 21, 24, 20, 24, 28, 32]
