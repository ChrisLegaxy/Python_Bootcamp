"""
    Description :
        In this program you will create a function take a string and return a
    list. The function must split the string at every space character. If
    the string is empty you will return an empty list.
    
    Requirements :
        ● Program must be named : 22_fun_split.py and saved into week02/ex folder
    Hint :
        ❖ Function
        ❖ list
        ❖ split
"""
# Declare variable
strInput = "Hello! It’s me again!"

# Defining functions
def fun_split(strInput) :
    # Check if the strInput is an empty string
    if strInput=="" :
        return list()
    else:
        # Return list
        return list(strInput.split(' '))

# Display and function call
print("fun_split({})".format(strInput))
print(">> ",fun_split(strInput))
# print(fun_split(""))