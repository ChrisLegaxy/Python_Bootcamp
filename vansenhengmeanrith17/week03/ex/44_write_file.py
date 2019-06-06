import os

def write_file(file_name,file_content):
    running = True
    if os.path.exists(file_name) and os.path.isfile(file_name):
        replace_check = input("Are you sure you want to replace <{}>? [Y/N]\n>> ".format(file_name))
        while running:
            if replace_check == "Y" or replace_check == "y":
                f = open(file_name, 'w')
                f.write(file_content)
                f.close()
                return 1
            if replace_check == "N" or replace_check == "n":
                return 0
            else:
                print("Invalid Option")
                replace_check = input("Are you sure you want to replace <{}>? [Y/N]\n>> ".format(file_name))
    else:
        f = open(file_name, 'w')
        f.write(file_content)
        f.close()
        return 1
