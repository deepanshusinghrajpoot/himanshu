# Set Comprehension
#------------------

# lll Set comprehension is a shortest and readable way to create a set.




# Set comprehension is a concise and readable way to create a set.
# It allows us to generate a new set in a single line of code.  
# Unlike lists, sets do not allow duplicate elements and are unordered.

# Syntax
#-------

# new_set = {expression for item in iterable if condition}


# Advantages of Set Comprehension
#--------------------------------

# 1. It automatically removes duplicate elements.
# 2. It is faster and more efficient than traditional loops for sets.
# 3. It reduces the number of lines of code.
# 4. It converts loop-based logic into a single readable expression.



# Ques:- Add numbers from 1 to 10 into a set
#--------------------------------------------

S = set()

for i in range(1, 11):
    S.add(i)

print(S)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


S = {i for i in range(1, 11)}
print(S)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}



# Ques:- Add square of each number from 1 to 5
#---------------------------------------------

S = set()
for i in range(1, 6):
    S.add(i*i)

print(S)  # {1, 4, 9, 16, 25}


S = {i*i for i in range(1, 6)}
print(S)  # {1, 4, 9, 16, 25}



# Ques:- Add numbers divisible by 3 from 1 to 20
#-----------------------------------------------

S = {i for i in range(1, 21) if i % 3 == 0}
print(S)  # {3, 6, 9, 12, 15, 18}



# Ques:- Remove duplicates from a list using set comprehension
#-------------------------------------------------------------

L = [1, 2, 3, 2, 4, 1, 5]

S = {i for i in L}
print(S)  # {1, 2, 3, 4, 5}



# Ques:- Convert all strings in a list to uppercase
#--------------------------------------------------

words = ["apple", "banana", "apple", "cherry"]

S = {word.upper() for word in words}
print(S)  # {'APPLE', 'BANANA', 'CHERRY'}



# Ques:- Nested if with Set Comprehension
#---------------------------------------

# Select numbers divisible by 2 and greater than 5

numbers = range(1, 11)

S = {n for n in numbers if n % 2 == 0 if n > 5}
print(S)  # {6, 8, 10}



# Ques:- Cartesian product using Set Comprehension
#-------------------------------------------------

# Combine two sets and multiply each pair of elements

S1 = {1, 2, 3}
S2 = {4, 5}

S = {i*j for i in S1 for j in S2}
print(S)  # {4, 5, 8, 10, 12, 15}



# Ques:- Create a set of tuples from two lists
#----------------------------------------------

names = ["Alice", "Bob"]
scores = [85, 90]

S = {(name, score) for name in names for score in scores}
print(S)  
# {('Alice', 85), ('Alice', 90), ('Bob', 85), ('Bob', 90)}



# Ques:- Set comprehension with string filtering
#-----------------------------------------------

fruits = ["apple", "banana", "avocado", "cherry"]

S = {fruit for fruit in fruits if fruit.startswith('a')}
print(S)  # {'apple', 'avocado'}



# Ques:- Flatten a nested list into a set
#----------------------------------------

nested_list = [[1, 2], [2, 3], [3, 4]]

S = {i for sublist in nested_list for i in sublist}
print(S)  # {1, 2, 3, 4}
