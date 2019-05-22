"""
    Description :
        You will write a function that take a list and return a list with
    uppercase format. If the list is empty, your function will return an
    empty list.

    Requirements :
        ● Program must be named : 39_acronym.py and saved into week02/ex folder
        
    Hint :
        ❖ list
        ❖ string
        ❖ loop
"""

# Declaring variables
listOfWords = ["world", "wide", "web"]

# listOfWords = []

# Defining functions
def acronym(listOfWords) :
    listOfAcronym = []
    if not listOfWords:
        return []
    for i in listOfWords:
        listOfAcronym.append(str(i[0]).upper())
    return listOfAcronym

print("acronym({})".format(listOfWords))
print(acronym(listOfWords))