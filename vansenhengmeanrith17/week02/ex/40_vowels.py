"""
    Description :
        You will write a function that take a list of string and return the
    number of vowels. Also it will display the number of vowels, then
    display a concatenate string with vowels only in lowercase. Finally
    display a concatenate string with all the characters that are not
    vowels in uppercase. If not vowels are given, you function will return
    0 and print “NO VOWELS”

    Requirements :
        ● Program must be named : 40_vowels.py and saved into week02/ex folder
"""

# Declaring variables
listOfVowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
stringInput = "what is that ?"

# Defining functions
def vowels(stringInput) :
    vowelsCount = 0
    vowelsInput = ""
    notVowelsInput = ""
    for char in stringInput :
        if char in listOfVowels :
            vowelsCount += 1
            vowelsInput += char
        elif char != " " :
            notVowelsInput += char

    if vowelsCount == 0 :
        return 0
    
    print(vowelsCount)
    print(vowelsInput)
    print(notVowelsInput.upper())

if vowels(stringInput) == 0:
    print("NO VOWELS")
