"""
    Description :
        You will write a function that return the current date with the
    following format: YYYY-MM-DD. The return value must be a string.

    Requirements :
        ● Program must be named : 34_current_date.py and saved into week02/ex
    folder

    Hint :
        ❖ function
        ❖ datetime
"""

# Imports
import datetime

# Declaring variables

# Defining functions
def current_date():
    return str(datetime.date.today())
    # return str(datetime.datetime.today().strftime("%Y-%m-%d"))
    
# Display and function call
print("current_date()")
print(">> ",current_date())