""" 
    PROJECT 04  : Top Words
    Author      : Vansen Hengmeanrith AKA Chris
    Email       : vansenhengmeanrith17@kit.edu.kh
    Created     : 24 May 2019
    Instructor  : Kevin Sabbe
    Language    : Python
"""

#Declare variables
text = "Welcome to Kirirom: Kirirom Institute of Technology and Kirirom National Parc. To contact us, send a message to us!"
# text = "//can't cant Cant can't"
# text = ". ??? // ####### // // ???"
# text = ""

# Defining functions
def top_words(text):
    stringOfLowerText = ""
    listOfLowerText = []
    listOfUniqueLowerText = []
    listOfUniqueLowerTextWithNumberOfOccurence = []
    listOfTopWords = []
    listOfTop3Words = []

    # Convert all words in text list to lower case and ignore the special character
    for i in text:
        if i.isalpha() or i == " " or i == "'":
            stringOfLowerText += i.lower()
    
    # Split the string into list at space
    listOfLowerText = stringOfLowerText.split(" ")

    # Create a list of unique lower text words in the list
    for i in listOfLowerText:
        if i not in listOfUniqueLowerText:
            listOfUniqueLowerText.append(i)

    # Count the number of occurence of each lower case words also then
    # create a new list that contains lists of (words, number of occurence)
    for i in listOfUniqueLowerText:
        listOfUniqueLowerTextWithNumberOfOccurence.append([i,listOfLowerText.count(i)])
    
    # Iterate through each of list in list of uniqueLowerText
    for i in range(len(listOfUniqueLowerTextWithNumberOfOccurence)):
        # Set the a default value for top value
        topValue = listOfUniqueLowerTextWithNumberOfOccurence[i]
        # Use for comparision
        j = i + 1
        while j < len(listOfUniqueLowerTextWithNumberOfOccurence):
            # Compare each i to each j which is all the elements in the list
            # But compare only the second argument which is the value
            # If the value of another element is smaller, set another element as the top value then do the swapping
            if listOfUniqueLowerTextWithNumberOfOccurence[i][1] < listOfUniqueLowerTextWithNumberOfOccurence[j][1]:
                topValue = listOfUniqueLowerTextWithNumberOfOccurence[j]
                temp = listOfUniqueLowerTextWithNumberOfOccurence[i]
                listOfUniqueLowerTextWithNumberOfOccurence[i] = listOfUniqueLowerTextWithNumberOfOccurence[j]
                listOfUniqueLowerTextWithNumberOfOccurence[j] = temp
            j += 1
        # Append the topvalue argument 0 which is the words into another list of top occurence word
        listOfTopWords.append(topValue[0])
    
    # Fetch the first 3 words from the list of top words
    listOfTop3Words = listOfTopWords[:3]

    # print(listOfUniqueLowerTextWithNumberOfOccurence)
    # return listOfUniqueLowerTextWithNumberOfOccurence
    if listOfUniqueLowerText[0] == "":
        return []
    return listOfTop3Words
    
print(top_words(text))

# top_words(text)
# for i in range(len(text)):
#     for j in text[i]:
#         j.lower()

# print(text)