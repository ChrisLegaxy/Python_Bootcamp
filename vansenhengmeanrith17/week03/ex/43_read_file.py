import os

def read_file(file_name):
    path = os.getcwd()
    check_current_item = path + "\\" + file_name
    if os.path.isfile(check_current_item):
        f = open(check_current_item, 'r')
        data = f.read()
        f.close
        return data
    else: 
        print("Invalid FILENAME")
        return []