"""
    Description :
        You will write a function that take a list in parameters and return a
    List with unique values only.

    Requirements :
        ● Program must be named : 26_list_set.py and saved into week02/ex folder

    Hint :
        ❖ function
        ❖ list
        ❖ set
"""

# Declaring variables
A = ['456', '123', '789', '123', 'abc', 'abc', 'def']

# Defining functions
def list_set(a):
    # Declaring a unique list
    uniqueList = []
    # Iterate through each elements in list (a)
    for x in a:
        # If the element in list (a) does not exist in unique list, append it, if not skip it
        if x not in uniqueList:
            uniqueList.append(x)
    # Return the unique list
    return uniqueList

# Display and function call
print("list_set({})".format(A))
print(">> ",list_set(A))