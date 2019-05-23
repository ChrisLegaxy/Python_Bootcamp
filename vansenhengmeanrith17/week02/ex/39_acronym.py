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
    # Declaring an empty acronym list
    listOfAcronym = []
    # Check if the list of words is empty
    if not listOfWords:
        return []

    # Iterate through each element, get the first letter of every words then covert to upper case then append it 
    for i in listOfWords:
        listOfAcronym.append(str(i[0]).upper())
    # Return the list of acronyms
    return listOfAcronym

# Display and function call
print("acronym({})".format(listOfWords))
print(">>",acronym(listOfWords))