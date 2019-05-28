'''
        USAGE:

        - Replace Sudoku function with your own code
        - Also, if you Sudoku function requires others functions that you've made
        - Don't forget to copy them ( upstairs )
'''

def sudoku(board):
    return "Nothing"

board_1 = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
res = sudoku(board_1)
if res != "Finished":
    print("KO - BOARD_1: should have 'Finished' but got '" + res + "' instead")
else:
    print("OK - BOARD_1")

#Finished

board_2 = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 3]
    ]
res = sudoku(board_2)
if res != "Not Finished":
    print("KO - BOARD_2: should have 'Not Finished' but got '" + res + "' instead")
else:
    print("OK - BOARD_2")

board_3 = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 1, 1, 1],
    [2, 8, 7, 4, 1, 9, 1, 1, 1],
    [3, 4, 5, 2, 8, 6, 1, 1, 1]
    ]
res = sudoku(board_3)
if res != "Not Finished":
    print("KO - BOARD_3: should have 'Not Finished' but got '" + res + "' instead")
else:
    print("OK - BOARD_3")

board_4 = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
res = sudoku(board_4)
if res != "Invalid Format":
    print("KO - BOARD_4: should have 'Invalid Format but got '" + res + "' instead")
else:
    print("OK - BOARD_4")

board_5 = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 1, 1, 1],
    [2, 8, 7, 4, 1, 9, 1, 1, 1],
    [3, 4, 5, 2, 8, 6, 1, 1, 1],
    [3, 4, 5, 2, 8, 6, 1, 1, 1]
    ]
res = sudoku(board_5)
if res != "Invalid Format":
    print("KO - BOARD_5: should have 'Invalid Format but got '" + res + "' instead")
else:
    print("OK - BOARD_5")


board_6 = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5]
    ]
res = sudoku(board_6)
if res != "Invalid Format":
    print("KO - BOARD_6: should have 'Invalid Format but got '" + res + "' instead")
else:
    print("OK - BOARD_6")
