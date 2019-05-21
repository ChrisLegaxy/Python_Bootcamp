#Getting Input
firstNum = int(input('Enter a number: '))
secondNum = int(input('Enter a second number: '))

#Condition
if firstNum == secondNum:
    print('Result : ' + str(firstNum) + ' == ' + str(secondNum))
elif firstNum < secondNum:
    print('Result : ' + str(firstNum) + ' < ' + str(secondNum))
else:
    print('Result : ' + str(secondNum) + ' < ' + str(firstNum))
