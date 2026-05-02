


# Lambda Function
#================

#lll A lambda function is a small anonymous function.
#    A lambda function can take any number of arguments, but can only have one expression.


# syntax
#-------

# variable = lambda args : operation on args


# Ques :- create function to find square of a number
#....................................................

a = lambda x : x**2
print(a(3))# 9


# Ques :- create function to check a is persent in string or not
#...............................................................

b = lambda x: 'a' in x
print(b("Deepanshu")) # True


# Ques :- create function to check given number is odd or even
#.............................................................

c = lambda x:( print(x, " is even!") if x%2 == 0 else print(x, " is odd!") )if type(x) == int else print("Give only integer")
c("Deepanshu") # Give only integer
c(4)           # 4  is even!
c(9)           # 9  is odd!



check_sum = lambda a, b, c: "Even" if (a + b + c) % 2 == 0 else "Odd"
print(check_sum(4, 5, 6)) # odd


# Difference b/w lambda function Vs regular function
#...................................................

# 1. lambda function is a anonymous function
# 2. lambda function has no return value
# 3. lambda function is written in 1 line
# 4. not reusable



# Why use lambda function?
#.........................

# They are use with HOF







# Higher Order Function (HOF)
#============================

# When a function hold another function as argument
# or
# return another function is called HOF


# Ques:- create function to perform square operation on each list item
#.....................................................................

def transform(fn, L):
    output_list = []
    for i in L:
        output_list.append(fn(i))

    return output_list

L = [1, 2, 3, 4, 5]

print(transform(lambda x:x**2 , L)) # [1, 4, 9, 16, 25]
    
    
