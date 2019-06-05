import os

def write_file(file_name,file_content):
    path = os.getcwd()
    check_current_item = path + "\\" + file_name

    if os.path.exists(check_current_item):
        replace_check = input("Are you sure you want to replace <{}>? [Y/N]\n>> ".format(file_name))
        while True:
            if replace_check == "Y" or replace_check == "y":
                f = open(check_current_item, 'w')
                f.write(file_content)
                f.close()
                return 1
            if replace_check == "N" or replace_check == "n":
                return 0
            else:
                print("Invalid Option")
                replace_check = input("Are you sure you want to replace <{}>? [Y/N]\n>> ".format(file_name))
    else:
        f = open(check_current_item, 'w')
        f.write(file_content)
        f.close()
        return 1