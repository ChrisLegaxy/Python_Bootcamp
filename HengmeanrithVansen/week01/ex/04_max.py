#Getting Input
firstNum = input('Enter First Number: ')
secondNum = input('Enter Second Number: ')

#Condition
if firstNum == secondNum:
    print('Result ' + str(firstNum) + ' == ' + str(secondNum))
elif firstNum > secondNum:
    print('Result ' + str(firstNum) + ' > ' + str(secondNum))
else:
    print('Result ' + str(secondNum) + ' > ' + str(firstNum))
