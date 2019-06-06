import os

list_of_folder_names = ["a","b"]

def auto_folder(list_of_folder_names):
    path = os.getcwd()
    new_folder_count = 0
    running = True
    for i in list_of_folder_names:
        check_current_item = path + "\\" + i
        if os.path.exists(check_current_item) and os.path.isdir(check_current_item):
            replace_check = input("Are you sure you want to replace <{}>? [Y/N]\n>> ".format(i))
            while running:
                if replace_check == "Y" or replace_check == "y":
                    os.rmdir(check_current_item)
                    os.mkdir(check_current_item)
                    new_folder_count += 1
                    break
                if replace_check == "N" or replace_check == "n":
                    break
                else:
                    print("Invalid Option")
                    replace_check = input("Are you sure you want to replace <{}>? [Y/N]\n>> ".format(i))
        else:
            os.mkdir(check_current_item)
            new_folder_count += 1
    
    if new_folder_count > 0:
        return 1
    else:
        return 0 

print(auto_folder(list_of_folder_names))