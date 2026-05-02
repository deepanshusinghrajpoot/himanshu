


# map
#=====

# Diffinition : map is HOF which perform operation on each item of iterable

# syntax
#--------

# map(arg1, arg2)
# arg1 :- is lambda function
# arg2 :- iterable



# Ques:- find square items of a list
#...................................

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(lambda x:x**2, L))) 

# [1, 4, 9, 16, 25, 36, 49, 64, 81]

print(map(lambda x: x*2, L))
# <map object at 0x0000014BE2933C70>


# Ques:- odd/even labelling of list items
#........................................

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(lambda x: 'even' if x%2 == 0 else 'odd', L)))

# ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']  




# Ques:- find only name form list of dictionary
#...............................................

users = [
    {
        "name":"Deepanshu",
        "age":22,
        "gender":"male"
    },
    {
        "name":"Himanshu",
        "age":24,
        "gender":"male"
    },
    {
        "name":"Shudhanshu",
        "age":24,
        "gender":"male"
    }
]


print(list(map(lambda x:x["name"], users)))

# ['Deepanshu', 'Himanshu', 'Shudhanshu']











# filter
#=======

# Diffinition : filter is HOF which filter element base on condition

# syntax
#--------

# filter(arg1, arg2)
# arg1 :- is lambda function
# arg2 :- iterable



# Ques:- find those items of a list which greater then 5
#.......................................................

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(lambda x:x>=5, L))) 

# [5, 6, 7, 8, 9]




# Ques:- find those items of a list which are even
#..................................................

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(lambda x: x%2 == 0 , L)))

# [2, 4, 6, 8]  




# Ques:- find only those user form list of dictionary where age = 24
#...................................................................

users = [
    {
        "name":"Deepanshu",
        "age":22,
        "gender":"male"
    },
    {
        "name":"Himanshu",
        "age":24,
        "gender":"male"
    },
    {
        "name":"Shudhanshu",
        "age":24,
        "gender":"male"
    }
]


print(list(filter(lambda x:x['age']==24, users)))

# [{'name': 'Himanshu', 'age': 24, 'gender': 'male'}, {'name': 'Shudhanshu', 'age': 24, 'gender': 'male'}]









# Reduce
#=======

# Note : reduce function does not available by default
# first import :- functools
# In functool has reduce

# functools.reduce(function, iterable, initializer)


# Diffinition : aggregate item of iterable

# syntax
#--------

# reduce(arg1, arg2, arg3)

# arg1 :- is lambda function
#...........................
       # lambda function has also two argument
       # argg1 :- accumulator
       # argg2 :- current

# arg2 :- iterable
#..................

# args3 :- Initial Value
#.......................





# Ques:- find the sum of all list item
#......................................

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

import functools

print(functools.reduce(lambda acc, curr : acc + curr, L))

# 45



# Ques:- find minimum item from list
#...................................

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(functools.reduce(lambda acc, curr: acc if acc < curr else curr, L))

# 1