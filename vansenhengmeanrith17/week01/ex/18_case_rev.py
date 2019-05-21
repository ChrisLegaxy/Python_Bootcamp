#Getting Input
strInput = input('Enter a string: ')
strInputLength = len(strInput)
strOutput = ""

if strInput == "":
    print("Empty")

for i in range(strInputLength):
    if strInput[i].isupper():
        strOutput = strOutput + strInput[i].lower()
    elif strInput[i].islower():
        strInput[i].upper()
        strOutput = strOutput + strInput[i].upper()
print(strOutput)
