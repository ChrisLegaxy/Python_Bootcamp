board = [
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

check_if_row_is_unique = True
unique_row = []
if check_if_the_board_is_correct:
    for x in range(len(board)):
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

check_if_column_is_unique = True
column_list = []
unique_column = []
if check_if_the_board_is_correct:
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

# check_if_bottom_rank_is_unique = True
# bottom_rank = board[6:9]
# temp = []
# each_bottom_region = []
# all_bottom_region = []
# each_unique_bottom_region = []
# start = 0
# stop = 3
# if check_if_the_board_is_correct:
#     for i in range(len(bottom_rank)):
#         for j in bottom_rank:
#             temp = j[start:stop]
#             for k in temp:
#                 each_bottom_region.append(k)
#         all_bottom_region.append(each_bottom_region)
#         each_bottom_region = []
#         start = stop
#         stop += 3

# for i in all_bottom_region:
#     for j in i:
#         if j not in each_unique_bottom_region:
#             each_unique_bottom_region.append(j)
#     if len(each_unique_bottom_region) != 9:
#         check_if_bottom_rank_is_unique = False

check_if_each_region_is_unique = True
rank = []
rank_start = 0
rank_stop = 3
temp = []
start = 0
stop = 3
each_region = []
all_region = []
for i in range(3):
    rank = board[rank_start:rank_stop]
    for j in range(len(rank)):
        for k in rank:
            temp = k[start:stop]
            for l in temp:
                each_region.append(l)
        all_region.append(each_region)
        each_region = []
        start = stop
        stop += 3
    start = 0
    stop = 3
    rank_start = rank_stop
    rank_stop += 3

unique_region = []
for i in all_region:
    for j in i:
        if j not in unique_region:
            unique_region.append(j)
    if len(unique_region) != 9:
        check_if_each_region_is_unique = False
        break 

print(all_region)
print(check_if_the_board_is_correct)
print(check_if_row_is_unique)
print(check_if_column_is_unique)
print(check_if_each_region_is_unique)