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

    # Iterate through each element in unique list
    for x in uniqueList:
        # Assign key in dictionary equal to the element in unique list then use that to count the number of occurence in list(a)
        dictCount[x] = A.count(x)
        countTotal += int(A.count(x))

    # key = lambda (k ,v) : k, since kv[0], 0 = key, 1 = value
    # The sorted elements will be in a list of tuples
    dictCountSortedByKey = sorted(dictCount.items(), key = lambda kv : kv[1], reverse=True)
    
    # Check if the list is empty or check the first key of the dictionary is empty
    if bool(dictCount) == True and uniqueList[0]!="": # list(dictCount.keys())[0]!=""
        return str(dictCountSortedByKey) + "\n>> TOTAL: " + str(countTotal)
    else:
        return []
    
# Display and function call
if not dict_count2(A):
    print("Your string is empty.")
else:
    print("dict_count2({})".format(A))
    print(">>",dict_count2(A))