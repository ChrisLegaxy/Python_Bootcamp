"""
    Description :
        You will write a function that take a List in parameters and return a
    sorted List with unique values only that are valid numbers. also the
    returned list elements must be INTEGER (not string)

    Requirements :
        ● Program must be named : 30_list_sort_int.py and saved into week02/ex
    folder

    Hint :
        ❖ function
        ❖ list
        ❖ sort
"""

# Declaring variables
A = ["abc", "4", "4", "4", "4", "2", "3", "dza", "def"]

# Defining functions
def list_sort_int(a):
    # Declaring a unique list
    uniqueList = []
    # Iterate through each elements in list (a)
    for x in a:
        # If the element in list (a) is a digit
        if x.isdigit():
            # Type cast it to int
            x = int(x)
            # Check if the number exist in the unique list
            if x not in uniqueList:
                uniqueList.append(x)
    # Sort the unique list with non numerical elements
    uniqueList.sort()
    # Return the unique list
    return uniqueList

# Display and function call
print("list_sort_int({})".format(A))
print(">> ",list_sort_int(A))