#Imports
import random

#Code
#Getting Input
n = int(input('Enter number time to display random numbers: '))
#For loop
for i in range(n):
    #Random function
    print(random.randrange(1,100))
    