""" 
    PROJECT 03  : Tax Calculator
    Author      : Vansen Hengmeanrith AKA Chris
    Email       : vansenhengmeanrith17@kit.edu.kh
    Created     : 21 May 2019
    Instructor  : Kevin Sabbe
    Language    : Python
"""

# Declare forever loop(s) and other loop(s)
foreverLoop_One = True
foreverLoop_Two = True

while foreverLoop_One :

    # Getting amount input
    inputAmount = input("Please enter your amount:\n>> ")

    # Check if the input is a digit and a positive number
    if inputAmount.isdigit() and int(inputAmount) > 0:
        while foreverLoop_Two :
            
            # Getting tax rate input
            inputTaxRate = input("Please enter tax rate:\n>> ")
            
            # Check if the tax rate is digit and between 1 and 100
            if inputTaxRate.isdigit() and (int(inputTaxRate) > 0 and int(inputTaxRate) < 100) :

                # Type Casting
                inputAmount = int(inputAmount)
                inputTaxRate = int(inputTaxRate)

                # Basic Math Operation
                tax = inputAmount * (inputTaxRate/100)
                net = inputAmount - tax

                print("\n===== ===== ===== ===== =====")
                print("AMOUNT: "+ str(inputAmount) +"$")
                print("RATE: "+ str(inputTaxRate) +"%")
                print("===== ===== ===== ===== =====")
                print("TAX: "+ '{:.2f}'.format(tax) +"$")
                print("NET: "+ '{:.2f}'.format(net) +"$")
                print("===== ===== ===== ===== =====")
                
                # Exit from both loops
                foreverLoop_One = False
                foreverLoop_Two = False
            else:
                print("Rate is incorrect, try again.")
            
    # elif inputAmount.isdigit() == False or int(inputAmount) < 0 :
    else :
        print("Number is incorrect, try again.")



