strInput = input('Enter a string: ')
strInputLength = len(strInput)
strOutput = ""

if strInput == "":
    print('Nothing to decode.')
    exit()

for i in range(strInputLength):
    asciiChar = ord(strInput[i])

    if strInput[i].isalpha():
        strAscii = asciiChar - 13
        if strInput[i].isupper():
            if strAscii < 65:
                for i in range(13, 0, -1):
                    if asciiChar == (ord('A')-1):
                        asciiChar = ord('Z')
                    asciiChar -= 1
                strAscii = asciiChar
        elif strInput[i].islower():
            if strAscii < 97:
                for i in range(13):
                    if asciiChar == (ord('a')-1):
                        asciiChar = ord('z')
                    asciiChar -= 1
                strAscii = asciiChar
    else:
        strAscii = asciiChar
    
    print(strAscii)
    strOutput = strOutput + chr(strAscii)
print(strOutput)