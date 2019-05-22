"""
    Description :
        You will write a function that take a list in parameters and return a
    sorted list with unique values only.

    Requirements :
        ● Program must be named: 28_list_sort_set.py and saved into week02/ex
    folder

    Hint :
        ❖ function
        ❖ list
        ❖ sort
"""

# Declaring variables
A = [4, 2, 19, 50, 49, 48, 1, 2, 3, 4, 5]

# Defining functions
def list_sort_set(a):
    # Declaring a unique list
    uniqueList = []
    # Iterate through each elements in list (a)
    for x in a:
        # If the element in list (a) does not exist in unique list, append it, if not skip it
        if x not in uniqueList:
            uniqueList.append(x)
    # Sort the unique list
    uniqueList.sort()
    # Return the unique list
    return uniqueList

# Display and function call
print("list_sort_set({})".format(A))
print(">> ",list_sort_set(A))