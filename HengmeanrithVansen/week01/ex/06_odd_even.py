#Getting Input
number = input('Enter a number to check whether it is odd or even: ')

#Checking Condition
if number.isdigit():
    number = int(number)
    if number % 2 == 0:
        print(str(number) + ' is Even')
    else:
        print(str(number) + 'Is Odd')
elif number == 'EXIT' or number == 'exit':
    exit() #Exit Function
else:
    print('Invalid Input')

# number = int(input('Enter a number to check whether it is odd or even: '))
# if number % 2 == 0:
#         print(str(number) + ' is Even')
# else:
#     print(str(number) + ' is Odd')