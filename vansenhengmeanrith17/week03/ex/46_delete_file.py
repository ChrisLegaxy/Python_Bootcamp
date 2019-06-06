import os

def delete_file(file_to_be_deleted):
    running = True
    if os.path.exists(file_to_be_deleted):
        delete_check = input("Are you sure you want to delete <{}>? [Y/N]".format(file_to_be_deleted))
        while running:
            if delete_check == "Y" or delete_check == "y":
                if os.path.isdir(file_to_be_deleted):
                    os.rmdir(file_to_be_deleted)
                elif os.path.isfile(file_to_be_deleted):
                    os.remove(file_to_be_deleted)
                else:
                    return 0
                return 1
            elif delete_check == "N" or delete_check == "n":
                return 0
            else:
                delete_check = input("Are you sure you want to delete <{}>? [Y/N]".format(file_to_be_deleted))
    else:
        return 0

print(delete_file("hello.txt"))