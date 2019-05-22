"""
    Description :
        You will write a function that take a Tuple in parameters and return
    the first value

    Requirements :
        ● Program must be named : 24_tuple_first.py and saved into week02/ex
    folder

    Hint :
        ❖ function
        ❖ tuple
"""

# Declaring variable
A = ('abc',123) # Tuple

# Defining functions 
def tuple_first(a):
    # Return first element of tuple
    return a[0]

# Display and function call
print("tuple_first({})".format(A))
print(">> ",tuple_first(A))

