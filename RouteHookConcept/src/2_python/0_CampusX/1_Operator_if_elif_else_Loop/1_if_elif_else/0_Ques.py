

# Question
# login program and indentation
# email -> nitish.camusx@gmail.com
# password -> 1234


email = input("Enter the valid email : ")
password = input("Enter valid password : ")

if email == "nitish.camusx@gmail.com" and password == "1234" :
    print("You are allow to access all course!") 

elif email == "nitish.camusx@gmail.com" and password != "1234" :
    password = input("Enter only valid password : ") 
    if password == "1234" :
        print("You are allow to access all course!") 
    else :
        print("Beta tumse na ho payega!")

elif email != "nitish.camusx@gmail.com" and password == "1234" :
    email = input("Enter only valid email : ")
    if email == "nitish.camusx@gmail.com" :
        print("You are allow to access all course!") 
    else :
        print("beta tumse na ho payega!")

elif email != "nitish.camusx@gmail.com" and password != "1234" :
    print("Your both credential are wrong please correct it!")

else: 
    print("You are not allow because your credential wrong!")