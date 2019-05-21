# n = int(input('Enter the number of time you want to display Hello World!'))
# i = 0
##While Loop
# while i < n :
#     print('Hello World\n')
#     x += 1

n = input('Enter a number: ')

#Check if the input is empty
if n == "":
    print('Nothing to display')
else:
#For Loop
    for i in range(int(n)):
        print('Hello World!')