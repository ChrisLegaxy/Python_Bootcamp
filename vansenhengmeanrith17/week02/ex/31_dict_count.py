"""
    Description :
        You will write a function that take a list in parameters and return a
    dictionary with the element of the list as key, and the number of
    occurrences as value.

    Requirements :
        ● Program must be named : 31_dict_count.py and saved into week02/ex
    folder

    Hint :
        ❖ function
        ❖ list
        ❖ dictionary
        ❖ occurrences
"""

# Declaring variables
A = ["a", "a", "a", "b", "c", "d", "c", "b", "c", "d", "c", "e", "e", "e"]

# Defining functions
def dict_count(a):
    # Declare dictionary and unique list
    dictCount = {}
    uniqueList = []
    # Iterate through each element in list(a)
    for x in a:
        # If the element in list (a) does not exist in unique list, append it, if not skip it
        if x not in uniqueList:
            uniqueList.append(x)
    
    # Iterate through each element in unique list
    for x in uniqueList:
        # Assign key in dictionary equal to the element in unique list then use that to count the number of occurence in list(a)
        dictCount[x] = a.count(x)
    
    # Return a dictionary
    return dictCount

# Display and function call
print("dict_count({})".format(A))
print(">> ",dict_count(A))