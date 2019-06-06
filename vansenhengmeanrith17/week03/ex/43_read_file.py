import os

def read_file(file_name):
    if os.path.exists(file_name) and os.path.isfile(file_name):
        f = open(file_name, 'r')
        data = f.read()
        f.close
        return str(data)
    else: 
        print("Invalid FILENAME")
        return []