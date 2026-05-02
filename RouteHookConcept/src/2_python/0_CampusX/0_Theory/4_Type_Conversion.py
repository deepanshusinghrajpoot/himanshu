

# Diff between Type Conversion and Type Casting
#===============================================

#lll In Type Conversion means: Automatic change of data type by Python
#lll In Type Casting means: Manual change of data type by programmer





l = int(input("Enter integer l: "))
r = int(input("Enter integer r: "))

print("l + r:", l + r)





# Type Conversion
#=================

# Two types of Type Conversion:
# (1). Implicit
# (2). Explicit





# (1). Implicit : Python automatically converts the data type
# -----------------------------------------------------------------

a = 4
b = 4.5

print(a + b)  # 8.5  (int -> float automatically)





# (2). Explicit : Manual type conversion by programmer
# --------------------------------------------------





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
