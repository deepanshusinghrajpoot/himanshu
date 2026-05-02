



# Question :- 1/1! + 2/2! + 3/3! +...

import math

n = int(input("Enter a number n : "))

sum = 0
for i in range(1, n+1):
     sum += i/math.factorial(i)

else: print("loop end!")
print("sum", sum)




m = int(input("Enter the number m : "))

result = 0
fact = 1
for i in range(1, m+1):
     fact *= i
     result += i/fact

print("result : ", result)