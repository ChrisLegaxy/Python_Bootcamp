"""
    Description :
        You will write a function that return the current date and time with
    the following format: YYYY-MM-DD hh:mm:ss
    The return value must be a string.

    Requirements :
        ● Program must be named : 36_date_time.py and saved into week02/ex folder

    Hint :
        ❖ function
        ❖ datetime
"""

# Imports
import datetime

# Declaring variables

# Defining functions
def date_time():
    return str(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
    
# Display and function call
print("date_time()")
print(">> ",date_time())