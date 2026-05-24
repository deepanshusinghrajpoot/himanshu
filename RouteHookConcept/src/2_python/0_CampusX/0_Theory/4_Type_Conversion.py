

# Diff between Type Conversion and Type Casting
#===============================================

#lll In Type Conversion means: Automatic change of data type by Python
#lll In Type Casting means: Manual change of data type by programmer





l = int(input("Enter integer l: "))
r = int(input("Enter integer r: "))

print("l + r:", l + r)



a = 4
b = 4.5

print(a + b)  # 8.5  (int -> float automatically)



# int()
#-------

p = 4.5
print(type(p))  # <class 'float'>

q = int(p)
print(type(q))  # <class 'int'>





# str()
#-------

m = 4
print(type(m))  # <class 'int'>

n = str(m)
print(type(n))  # <class 'str'>





# float()
#---------

s = float(m)
print(type(s))  # <class 'float'>







"""

1️⃣ Type Conversion (Automatic)
--------------------------------
Python automatically converts one data type into another.

Example
a = 10      # int
b = 2.5     # float

c = a + b

print(c)
print(type(c))

Output
12.5
<class 'float'>


Explanation
a is integer
b is float
Python automatically converts a into float
Result becomes float

👉 This is called Type Conversion.



2️⃣ Type Casting (Manual)
-------------------------

Programmer manually changes the data type.

Example

x = "100"

y = int(x)

print(y)
print(type(y))

Output
100
<class 'int'>

Explanation
"100" is string
int(x) converts string into integer manually

👉 This is called Type Casting.


More Type Casting Examples
...........................

String → Float

a = "45.7"

b = float(a)

print(b)
print(type(b))




"""








l = int(input("Enter integer l: "))
r = int(input("Enter integer r: "))

print("l + r:", l + r)



a = 4
b = 4.5

print(a + b)  # 8.5  (int -> float automatically)



# int()
#-------

p = 4.5
print(type(p))  # <class 'float'>

q = int(p)
print(type(q))  # <class 'int'>





# str()
#-------

m = 4
print(type(m))  # <class 'int'>

n = str(m)
print(type(n))  # <class 'str'>





# float()
#---------

s = float(m)
print(type(s))  # <class 'float'>


