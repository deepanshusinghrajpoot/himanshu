

# Question:- The current population of a town is 10000. The population of the town
#            is increases at the rate of 105 per year. You have to write a program 
#            to find out the population at end of each of the last 10 years.


# x + 0.1x = 10000

population = 10000

for i in range(10, 0, -1):
    
    print(i, population)

    population /= 1.1

else: print("last 10 year population!")



