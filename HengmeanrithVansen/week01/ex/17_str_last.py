#Getting Input
strInput = input('Enter a string: ')
strInputLenght = len(strInput)
#Check if string is empty
if strInput == "":
    print('Empty')
else:
    print(strInput[strInputLenght-1])