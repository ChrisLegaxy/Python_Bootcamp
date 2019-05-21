#Get Input
htmlText = []

while 1: 
    strInput = input('Enter a string: ')

    if strInput == 'Generate':
        for text in htmlText:
            print('<p>' + text + '</p>')
        break
    else:
        htmlText.append(strInput)
