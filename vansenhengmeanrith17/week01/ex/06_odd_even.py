#Getting Input

#Checking Condition
while True:
    getInput = input('Enter a number: ')
    if getInput.isdigit():
        getInput = int(getInput)
        if getInput % 2 == 0:
            print(str(getInput) + ' is EVEN')
            getInput = str(getInput)
        else:
            print(str(getInput) + ' is ODD')
    elif getInput == 'EXIT':
        exit() #Exit Function
    else:
        print(getInput+" is not a valid number.")

# getInput = int(input('Enter a getInput to check whether it is odd or even: '))
# if getInput % 2 == 0:
#         print(str(getInput) + ' is Even')
# else:
#     print(str(getInput) + ' is Odd')