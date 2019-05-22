"""
    Description :
        You will write a function that take a list in parameters and return a
    sorted list with unique values only with non numeric values.

    Requirements :
        ● Program must be named : 29_list_sort_str.py and saved into week02/ex
    folder

    Hint :
        ❖ function
        ❖ list
        ❖ sort
"""

# Declaring variables
A = ["abc", "4", "2", "3", "dza", "def"]

# Defining functions
def list_sort_str(a):
    # Declaring a unique list
    uniqueList = []
    # Iterate through each elements in list (a)
    for x in a:
        # If the element in list (a) does not exist in unique list, append it, if not skip it
        if x not in uniqueList:
            # Check if the element is a character
            if x.isdigit() == False:
                uniqueList.append(x)
    # Sort the unique list with non numerical elements
    uniqueList.sort()
    # Return the unique list
    return uniqueList

# Display and function call
print("list_sort_str({})".format(A))
print(">> ",list_sort_str(A))