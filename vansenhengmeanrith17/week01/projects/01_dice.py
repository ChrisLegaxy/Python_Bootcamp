import random

# Constant
INTRO_MESSAGE = "Welcome to the dices games!"

# Variable Declaration
diceResult = 0
i = 0

print(INTRO_MESSAGE)

# The loop will go on until the desire input is given
while True:
    getInput = input("Enter the number of dices you want to roll: ")
    # Check if the input is empty or a character
    if getInput == "" or getInput.isdigit() == False:
        print("USAGE: The number must be between 1 and 8")
    # Check if the number is between 1-8
    elif int(getInput) > 8 or int(getInput) < 1:
        print("USAGE: The number must be between 1 and 8")
    # If none of the conditions meet the loop will break and go to the next statement
    else:
        break

# While loop
while i < int(getInput):
    # Temporary variable to store the rolled dice
    tempDice = random.randrange(1,6+1)
    # Check if the input is more than 1
    if int(getInput) > 1 :
        print("Dice " + str(i+1) + " : " + str(tempDice))
    # Adding the rolled dice as the loop goes on
    diceResult += tempDice
    # For the while
    i += 1
    
if i == 1:
    print("RESULT: " + str(diceResult))
else:
    print("==========")
    print("RESULT: " + str(diceResult))
    print("==========")
