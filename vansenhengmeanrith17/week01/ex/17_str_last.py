#Getting Input
strInput = input('Enter a string: ')
strInputLength = len(strInput)
#Check if string is empty
if strInput == "":
    print('Empty')
else:
    print(strInput[strInputLength-1])