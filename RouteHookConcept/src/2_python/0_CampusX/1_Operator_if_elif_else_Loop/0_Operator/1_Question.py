


# program - Find the sum of a 3 digit number entered by the user
#----------------------------------------------------------------


number = int(input("Enter a 3 digit number : ")) # 543

a = number%10
number = number//10

b = number%10
number = number//10

print(number + b + a)  # 5 + 4 + 3 = 12