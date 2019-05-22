"""
    Description :
        You will write a function that take a Tuple in parameters and return
    the second value

    Requirements :
        ● Program must be named : 25_tuple_second.py and saved into week02/ex
    folder

    Hint :
        ❖ function
        ❖ tuple
"""

# Declaring variable
A = ('abc',123) # Tuple

# Defining functions 
def tuple_second(a):
    # Return second element of tuple
    return a[1]
    
# Display and function call
print("tuple_second({})".format(A))
print(">> ",tuple_second(A))

