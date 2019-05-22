"""
        Description :
    You will write a function that take a timestamp string and convert to
    readable date and time with the following format: YYYY-MM-DD hh:mm:ss
    If the timestamp is not valid, you function will return 0 and display
    “Your timestamp is not valid.”
    
    Requirements :
        ● Program must be named : 37_timestamp_to_str.py and saved into week02/ex
    folder
    
    Hint :
        ❖ function
        ❖ datetime
        ❖ timestamp
"""

# Imports
import datetime

# Declaring variables
timeStamp = 1623646780

# timeStamp = "asdasd"

# Defining functions
def timestamp_to_str(timeStamp):
    timeStamp = str(timeStamp)
    if timeStamp.isdigit():
        return datetime.datetime.fromtimestamp(int(timeStamp))
    else:
        return 0

# Display
print("timestamp_to_str({})".format(timeStamp))
if timestamp_to_str(timeStamp) == 0:
    print("Your timestamp is not valid")
else:
    print(timestamp_to_str(timeStamp))
