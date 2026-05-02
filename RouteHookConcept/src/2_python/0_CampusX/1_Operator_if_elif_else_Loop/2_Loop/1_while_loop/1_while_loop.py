
# Question : Guess a number between 1 to 100 and we suggest until you are not get correct number
#===================================================================================================



import random


random_num = random.randint(1, 100)
jacpot_num = int(input("Guess a number between 1 to 100 : "))

while random_num != jacpot_num :
    if jacpot_num < random_num :
        print("Guess! more higher!")
    else :
        print("Guess! lower number!")

    jacpot_num = int(input("Now guess according to suggestion : "))

else :
    print("Your are guess correct number!")

    