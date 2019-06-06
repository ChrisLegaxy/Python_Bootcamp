import os

def current_folder():
    # path = os.getcwd()
    items = os.listdir()
    file_list = []
    dir_list = []
    dir_file_list = []

    for i in items:
        # check_current_item = path + "\\" + i
        if os.path.isfile(i):
            file_list.append(i)
        elif os.path.isdir(i):
            dir_list.append(i)

    file_list.sort()
    dir_list.sort()

    for i in dir_list:
        dir_file_list.append((i, 'Folder'))

    for i in file_list:
        dir_file_list.append((i, 'File'))
    
    return dir_file_list
