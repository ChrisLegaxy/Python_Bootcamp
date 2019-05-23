"""
    Description :
        You will write a function that take a list in parameters and return a
    sorted list.

    Requirements :
        ● Program must be named : 27_list_sort.py and saved into week02/ex folder

    Hint :
        ❖ function
        ❖ list
        ❖ sort
"""

# Declaring variables
A = [4, 2, 19, 50, 49, 48, 1, 2, 3, 4, 5]

# Defining functions
def list_sort(a):
    # Sorting functions
    a.sort()
    # sorted(a)
    return a

# Display and function call
print("list_sort({})".format(A))
print(">> ",list_sort(A))