#Set a default value for Total
total = 0

#While forever loop
while True: 
    #Getting Input
    getInput = input('Enter a number: ')
    
    #Checking condition

    #Check if the input is empty
    if getInput == "":
        print(total)
    #Check if the input is equals for exit
    elif getInput == 'exit':
        exit()
    #The default operation if none of the conditions above meet
    else:
        getInput = int(getInput)
        total = total + getInput
        print('TOTAL: '+str(total))