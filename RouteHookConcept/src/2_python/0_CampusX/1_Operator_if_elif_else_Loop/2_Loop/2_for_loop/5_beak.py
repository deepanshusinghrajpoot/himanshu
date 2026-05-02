


# Break
#---------






# Take two number check prime number between them


lower = int(input("Enler a lower number : "))
upper = int(input("Enter a upper number : "))


for i in range(lower, upper+1):
    for j in range(2, i):

        if i%j == 0 :
            break
    else:
        print(i)

        