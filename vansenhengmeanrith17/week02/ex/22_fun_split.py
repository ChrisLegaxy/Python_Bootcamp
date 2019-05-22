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

# Defining functions
def fun_split(strInput) :
    # Return list
    if strInput=="" :
        return list()
    else:
        return list(strInput.split(' '))

# Display and function call
# print(fun_split("Hello! It’s me again!"))
print(fun_split(""))