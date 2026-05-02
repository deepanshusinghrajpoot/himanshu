

# Question : find the minimumm element from tree number which given by user
#---------------------------------------------------------------------------

a = int(input("Enter a number a : ")) 
b = int(input("Enter a number b : "))
c = int(input("Enter a number c : "))


if a < b and a < c:
    print("a is minimum!")
elif b < a and b < c:
    print("b is minimum!")
else:
    print("c is minimum!")
