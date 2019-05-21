import random

# Computer think of a random number from (1 to 100)
magicNumber = random.randrange(1,100+1)

# Declare count for counting the number of times the player guess
count = 0

# Getting name input
nameInput = input("Hello, what is your name?\n>> ")

# Getting the first guessing number
guessTheNumberInput = input("Well " + nameInput + ", try to guess the number I have in mind!\n>> ")

# Forever loop until the player gets the number correct
while True:
    # Check if the number is equal to the magic number
    if int(guessTheNumberInput) == magicNumber :
        # When the player guess the count var will increment sequentially, same goes for the other count += 1
        count +=1
        # Check if it is 1 time
        if int(count) == 1:
            print("You won in 1 turn only, that’s amazing!")
        else:
            print("It took you " + str(count) + " turns to guess my number which was " + str(magicNumber) +"!")
            
        # Forever loop until the player enter the correct input
        while 1:
            choiceInput = input("Do you want to play again? [Y/N]\n>> ")

            if choiceInput == "Y":
                # Resetting the magic number and count variables
                magicNumber = random.randrange(1,100+1)
                count = 0
                guessTheNumberInput = input("Well " + nameInput + ", try to guess the number I have in mind!\n>> ")
                break
            elif choiceInput == "N":
                print("Ok, bye " + nameInput +"! See you later!")
                exit()
            else:
                print("Sorry, I did not understand. Let me repeat: ")

    # Check if the number is greater than the magic number
    elif int(guessTheNumberInput) > magicNumber :
        count +=1
        guessTheNumberInput = input("Too high, try again!\n>> ")
            
    # Check if the number is lesser than the magic number
    elif int(guessTheNumberInput) < magicNumber :
        count +=1
        guessTheNumberInput = input("Too low, try again!\n>> ")

    


