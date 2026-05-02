# Special Syntax
#================


# Tuple Unpacking
#-----------------

# Tuple unpacking allows assigning tuple elements
# directly to multiple variables in a single statement.

a, b, c = (1, 2, 3)
print(a)  # 1
print(b)  # 2
print(c)  # 3

p,q,r = [9,8,7]
print(p) # 9
print(q) # 8
print(r) # 7



# Swapping values using tuple unpacking
#--------------------------------------

# No temporary variable is required

p = 5   
q = 6

p, q = q, p
print("p :- ", p)  # p :- 6
print("q :- ", q)  # q :- 5





# Extracting only limited values using unpacking
#-----------------------------------------------

# * is used to collect remaining values into a list

m, n, *others = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

print("m :- ", m)         # 1
print("n :- ", n)         # 2
print("others :- ", others)
# [3, 4, 5, 6, 7, 8, 9, 0]
