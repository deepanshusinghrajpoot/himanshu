


# Nested loop
#============


'''

*
**
***
****

'''

n = int(input("Enter the number n : "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
else: print("loop end 1!")





"""

1
121
12321
1234321

"""

m = int(input("Enter a number m : "))

for i in range(1, m+1):
    for j in range(1, i+1):
        print(j, end="")
    for k in range(i-1, 0, -1):
        print(k, end="")
    print()
else: print("End loop 2!")