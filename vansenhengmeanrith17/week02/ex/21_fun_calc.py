"""
    Description :
        In this program you will create a function that take 2 parameters in
    value (A and B) and return the total value. It will print the result
    and also the calculation.

    Requirements :
        ● Program must be named : 21_fun_calc.py and saved into week02/ex folder
    
    Hint :
        ❖ function
        ❖ return
"""

# Declaring variables
A = 5
B = 15

# Defining functions
def fun_calc(a,b) :
    # Return a + b
    return a + b

# Display function
print("fun_calc({}, {})".format(A,B))
# Display result
print(">> {}".format(fun_calc(A,B)))
# Display calculation
print(">> {} + {} = {}".format(A,B,fun_calc(A,B)))
# print(">> %d" % (A) )
# print(">> "+A)
# print(">> ",A)
