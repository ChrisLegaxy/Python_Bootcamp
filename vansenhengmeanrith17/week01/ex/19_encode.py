strInput = input('Enter a string: ')
strInputLength = len(strInput)
strOutput = ""

if strInput == "":
    print('Nothing to decode.')
    exit()

for i in range(strInputLength):
    asciiChar = ord(strInput[i])
    
    if strInput[i].isalpha():
        strAscii = asciiChar + 13
        if strInput[i].isupper():
            if strAscii > 90:
                for i in range(13):
                    if asciiChar == (ord('Z')+1):
                        asciiChar = ord('A')
                    asciiChar += 1
                strAscii = asciiChar
        elif strInput[i].islower():
            if strAscii > 122:
                for i in range(13):
                    if asciiChar == (ord('z')+1):
                        asciiChar = ord('a')
                    asciiChar += 1
                strAscii = asciiChar
    else:
        strAscii = asciiChar
    
    print(asciiChar)
    print(strAscii)
    strOutput = strOutput + chr(strAscii)
print(strOutput)