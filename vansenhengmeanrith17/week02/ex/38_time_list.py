"""
    Description :
        You will write a function that take an integer as parameter that
    represent a number of second and return a list of time.
    For example: if the current time is 04:30:12 and the integer = 3
    ==> [04:30:12, 04:30:13, 04:30:14]
    If the integer is negative or not valid, you will return an empty list
    and display “Invalid integer.”

    Requirements :
        ● Program must be named : 38_time_list.py and saved into week02/ex folder

    Hint :
        ❖ loop
        ❖ list
        ❖ function
        ❖ datetime
        ❖ sleep
"""

# Imports
import datetime
import time

# Declaring variables
A = 5
# A = -20

# Defining functions
def time_list(a):
    timeList = []
    a = str(a)
    if a.isdigit():
        for i in range(int(a)): 
            timeList.append(str(datetime.datetime.today().strftime("%H:%M:%S")))
            time.sleep(1)
        return timeList
    else:
        return []
    
# Display
print("time_list({})".format(A))
if not time_list(A) :
    print(">>",time_list(A))
    print(">> Invalid integer.")
else:
    print(time_list(A))