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
    # Declaring local variables
    vowelsCount = 0
    vowelsInput = ""
    notVowelsInput = ""
    
    # Iterate through each character in string input
    for char in stringInput :
        # Check if the character is vowel
        if char in listOfVowels :
            vowelsCount += 1
            vowelsInput += char
        # Ignore white space
        elif char != " " :
            notVowelsInput += char

    # If there's no vowel return 0
    if vowelsCount == 0 :
        return 0
    else:
        print(vowelsCount)
        print(vowelsInput)
        print(notVowelsInput.upper())
        return vowelsCount

numberOfVowels = vowels(stringInput)
if numberOfVowels == 0:
    print("NO VOWELS")
else:
    print(numberOfVowels)