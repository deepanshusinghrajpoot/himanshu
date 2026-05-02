# Dictionary Comprehension
#=========================

# Dictionary comprehension is a quick and readable way to create a dictionary.
# It lets us generate a new dictionary in a single line of code.


# Syntax
#-------
# new_dict = {expression for item in iterable if condition}


# Advantages of Dictionary Comprehension
#---------------------------------------
# 1. Faster and more efficient than normal loops
# 2. Reduces number of lines of code
# 3. Converts loop logic into a single readable expression



# Ques: Print first 10 numbers and their squares
#-----------------------------------------------

dic = {item: item**2 for item in range(1, 11)}
print(dic)  
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


# Ques: Convert existing dictionary distance from km to miles
#-----------------------------------------------------------

dic = {'delhi':1000, 'mumbai':2000, 'bangalore':3000}

temp_dic = {key: value*0.62 for (key, value) in dic.items()}
print(temp_dic)  
# {'delhi': 620.0, 'mumbai': 1240.0, 'bangalore': 1860.0}


# Ques: Create dictionary using zip
#-----------------------------------

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
temp_c = [30.5, 32.6, 31.8, 33.4, 29.8, 30.2, 29.9]

my_dic = {key: value for (key, value) in zip(days, temp_c)}
print(my_dic)  
# {'Sunday': 30.5, 'Monday': 32.6, 'Tuesday': 31.8, 'Wednesday': 33.4, 'Thursday': 29.8, 'Friday': 30.2, 'Saturday': 29.9}


# Using if condition
# Ques: Find products where stock is not zero
#--------------------------------------------

products = {'phone':10, 'laptop':0, 'charger':32, 'tablet':0}

my_product = {key: value for (key, value) in products.items() if value > 0}
print(my_product)  
# {'phone': 10, 'charger': 32}


# Nested Comprehension
# Print tables of numbers from 2 to 4
#--------------------------------------

my_table = {i: {j: i*j for j in range(1, 11)} for i in range(2, 5)}
print(my_table)
#{
# 2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20},
# 3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15, 6: 18, 7: 21, 8: 24, 9: 27, 10: 30},
# 4: {1: 4, 2: 8, 3: 12, 4: 16, 5: 20, 6: 24, 7: 28, 8: 32, 9: 36, 10: 40}
#}
