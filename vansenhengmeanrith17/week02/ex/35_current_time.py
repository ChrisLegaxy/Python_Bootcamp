"""
    Description :
        You will write a function that return the current time with the
    following format: hh:mm:ss
    The return value must be a string.

    Requirements :
        ● Program must be named : 35_current_time.py and saved into week02/ex
    folder

    Hint :
        ❖ function
        ❖ datetime
"""

# Imports
import datetime

# Declaring variables

# Defining functions
def current_time():
    return str(datetime.datetime.today().strftime("%H:%M:%S"))
    
# Display and function call
print("current_time()")
print(">> ",current_time())