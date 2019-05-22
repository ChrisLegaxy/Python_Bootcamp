"""
    Description :
        You will write a function that take a List in parameters and return a
    dictionary with the element of the List as Key, and the number of
    occurrences as value. The dictionary output must be sorted by value.
    Then the function will display the sum of all the items. If the list is
    empty you will return an empty dictionary and display “Your string is
    empty.”.

    Requirements :
        ● Program must be named : 32_dict_count2.py and saved into week02/ex
    folder

    Hint :
        ❖ Function
        ❖ list
        ❖ dictionary
        ❖ Occurrences
        ❖ values
"""

# Declaring variables
A = ["z", "z", "z", "z", "b", "b", "b", "b", "a", "a", "a", "a", "a", "a"]
# A = [""]

# Defining functions
def dict_count2(a):
    # Declare dictionary and unique list
    dictCount = {}
    uniqueList = []
    countTotal = 0
    # Iterate through each element in list(a)
    for x in a:
        # If the element in list (a) does not exist in unique list, append it, if not skip it
        if x not in uniqueList:
            uniqueList.append(x)
    
    # Sort the unique list
    uniqueList.sort()

    # Iterate through each element in unique list
    for x in uniqueList:
        # Assign key in dictionary equal to the element in unique list then use that to count the number of occurence in list(a)
        dictCount[x] = A.count(x)
        countTotal += int(A.count(x))
    
    # Check if the list is empty or check the first key of the dictionary is empty
    if bool(dictCount) == True and uniqueList[0]!="": # list(dictCount.keys())[0]!=""
        return str(dictCount) + "\n>> TOTAL: " + str(countTotal)
    else:
        return str({}) + " Your string is empty."
    
# Display and function call
print("dict_count2({})".format(A))
print(">>",dict_count2(A))