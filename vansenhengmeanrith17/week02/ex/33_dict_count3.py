"""
    Description :
        You will write a function that take a List in parameters and return a
    list of tuples with the element of the List as Key, and the number of
    occurrences as value. The list output must be sorted by key. Then the
    function will display the sum of all the items. If the list is empty
    you will return an empty list and display “Your string is empty.”.
    Before returning the value you will also print the TOTAL.

    Requirements :
        ● Program must be named : 33_dict_count3.py and saved into week02/ex
    folder

    Hint :
        ❖ Function
        ❖ list
        ❖ dictionary
        ❖ Occurrences
        ❖ values
"""

# Declaring variables
A = ["a", "b", "b", "c", "c", "c", "c", "d", "d", "e", "e", "e"]
# A = [""]

# Defining functions
def dict_count3(a):
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
    # uniqueList.sort()

    # Iterate through each element in unique list
    for x in uniqueList:
        # Assign key in dictionary equal to the element in unique list then use that to count the number of occurence in list(a)
        dictCount[x] = a.count(x)
        countTotal += int(a.count(x))

    # key = lambda (k ,v) : k, since kv[0], 0 = key, 1 = value
    # The sorted elements will be in a list of tuples
    dictCountSortedByKey = sorted(dictCount.items(), key = lambda kv : kv[0])

    # Check if the list is empty or check the first key of the dictionary is empty
    if bool(dictCount) == True and uniqueList[0]!="": # list(dictCount.keys())[0]!=""
        print(">> TOTAL: " + str(countTotal))
        return dictCountSortedByKey
    else:
        print("Your string is empty.")
        return []
    
# Display and function call
print("dict_count3({})".format(A))
print(">>",dict_count3(A))