"""
    Description :
        You will write a function that take 2 parameters and return a Tuple.
    
    Requirements :
        ● Program must be named : 23_fun_tuple.py and saved into week02/ex folder
    
    Hint :
        ❖ function
        ❖ tuple
"""

# Declaring variables
A = "abc"
B = 123

# Defining functions
def fun_tuple(a,b) :
    # Return tuple
    return (a,b)

# Display and function call
print("fun_tuple({}, {})".format(A,B))
print(">> ",fun_tuple(A,B))

