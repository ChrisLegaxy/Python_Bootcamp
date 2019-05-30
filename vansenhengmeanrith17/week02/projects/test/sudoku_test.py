'''
        USAGE:

        - Replace Sudoku function with your own code
        - Also, if you Sudoku function requires others functions that you've made
        - Don't forget to copy them ( upstairs )
'''

def check_board(board):
    """ 
        This function is to check if the board is in correct format
        The length of the board must be 9 (Rows)
        Each row must have 9 elements (Columns)
        Each element must be between 1 - 9
    """
    check_if_the_board_is_correct = True

    if len(board) == 9:
        for i in board:
            if len(i) == 9 and check_if_the_board_is_correct == True:
                for j in i:
                    if j not in range(1,9+1):
                        check_if_the_board_is_correct = False
                        break
            else:
                check_if_the_board_is_correct = False
            if check_if_the_board_is_correct == False:
                break
    else:
        check_if_the_board_is_correct = False
    
    return check_if_the_board_is_correct
    
def check_unique_row(board):
    check_if_row_is_unique = True
    unique_row = []
    if check_board(board):
        for i in board:
            for j in i:
                if j not in unique_row:
                    unique_row.append(j)
            if len(unique_row) != 9:
                check_if_row_is_unique = False
                break
            unique_row = []
    else:
        check_if_row_is_unique = False

    return check_if_row_is_unique

def check_unique_column(board):
    check_if_column_is_unique = True
    column_list = []
    unique_column = []
    if check_unique_row(board):
        for x in range(len(board)):
            for i in board:
                column_list.append(i[x])
            for i in column_list:
                if i not in unique_column:
                    unique_column.append(i)
            if len(unique_column) != 9:
                check_if_column_is_unique = False
                break
            column_list = []
            unique_column = []
    else:
        check_if_column_is_unique = False
    
    return check_if_column_is_unique

def generate_region(board):
    rank = []
    rank_start = 0
    rank_stop = 3
    temp = []
    start = 0
    stop = 3
    each_region = []
    all_region = []
    i = 0
    j = 0

    if check_unique_column(board):
        while i < 3:
            rank = board[rank_start:rank_stop]
            while j < len(rank):
                for k in rank:
                    temp = k[start:stop]
                    for l in temp:
                        each_region.append(l)
                all_region.append(each_region)
                each_region = []
                start = stop
                stop += 3
                j += 1
            start = 0
            stop = 3
            rank_start = rank_stop
            rank_stop += 3
            i += 1
        return all_region
    else:
        return []
        
def check_unique_region(board):
    check_if_each_region_is_unique = True
    unique_region = []
    for i in generate_region(board):
        for j in i:
            if j not in unique_region:
                unique_region.append(j)
        if len(unique_region) != 9:
            check_if_each_region_is_unique = False
            break 
    return check_if_each_region_is_unique

def sudoku(board):
    if check_board(board):
        if check_unique_row(board) and check_unique_column(board) and check_unique_region(board):
            return "Finished"
        else:
            return "Not Finished"
    else:
        return "Invalid Format"

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
