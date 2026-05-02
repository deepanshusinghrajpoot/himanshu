# Python Literals
#================

# Literals are fixed values assigned to variables.

# Python supports multiple types of literals:
#............................................




# Binary Literal
#---------------

a = 0b1010
print("a:", a)  # a: 10





# Decimal Literal
#----------------

b = 100
print("b:", b)  # b: 100





# Octal Literal
#---------------

c = 0o310
print("c:", c)  # c: 200





# Hexadecimal Literal
#--------------------

d = 0x12c
print("d:", d)  # d: 300





# Float Literal
#---------------

float_1 = 10.5
float_2 = 1.5e2    # 1.5 * 10^2
float_3 = 1.5e-3   # 1.5 * 10^-3





# Complex Literal
#-----------------

x = 3.14j
print("x:", x)               # 3.14j
print("x imag:", x.imag)     # 3.14
print("x real:", x.real)     # 0.0





# String Literal
#-----------------

string = 'This is python'
strings = "This is python"
char = "C"
multiline_str = """This is multiline string with more than one line code."""
unicode = u"\U0001f600\U0001F606\U0001F923"
row_str = r"raw \n string"

print("string:", string)
print("strings:", strings)
print("char:", char)
print("multiline_str:", multiline_str)
print("unicode:", unicode)
print("row_str:", row_str)

# Output:
# string: This is python
# strings: This is python
# char: C
# multiline_str: This is multiline string with more than one line code.
# unicode: 😀😆🤣
# row_str: raw \n string





# Boolean Literal
#-----------------

p = True + 4
q = False + 10

print("p:", p)  # 5
print("q:", q)  # 10





# None Literal
#---------------

# None represents 'no value' or 'null'

k = None
print(k)  # None
