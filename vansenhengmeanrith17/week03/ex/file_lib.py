import os
import datetime


class FileLib:
    def current_path(self):
        return os.path.abspath(os.getcwd())

    def current_folder(self):
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

    def read_file(self, file_name):
        if os.path.isfile(file_name):
            f = open(file_name, 'r')
            data = f.read()
            f.close
            return data
        else:
            print("Invalid FILENAME")
            return []

    def write_file(self, file_name, file_content):
        running = True
        if os.path.exists(file_name) and os.path.isfile(file_name):
            replace_check = input(
                "Are you sure you want to replace <{}>? [Y/N]\n>> ".format(file_name))
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
                    replace_check = input(
                        "Are you sure you want to replace <{}>? [Y/N]\n>> ".format(file_name))
        else:
            f = open(file_name, 'w')
            f.write(file_content)
            f.close()
            return 1

    def append_file(self, log):
        path = os.getcwd()
        logfile = path + "\\" + log
        log_input = ""
        f = open(logfile, 'a')
        while log_input != "EXIT":
            log_input = input("$: ")
            f.write("[{}] ".format(datetime.datetime.today().strftime(
                "%d/%m/%Y %H:%M:%S")) + log_input + "\n")
        f.close()

    def delete_file(self, file_to_be_deleted):
        running = True
        if os.path.exists(file_to_be_deleted):
            delete_check = input(
                "Are you sure you want to delete <{}>? [Y/N]".format(file_to_be_deleted))
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
                    delete_check = input(
                        "Are you sure you want to delete <{}>? [Y/N]".format(file_to_be_deleted))
        else:
            return 0

    def auto_folder(self, list_of_folder_names):
        path = os.getcwd()
        new_folder_count = 0
        running = True
        for i in list_of_folder_names:
            check_current_item = path + "\\" + i
            if os.path.exists(check_current_item) and os.path.isdir(check_current_item):
                replace_check = input(
                    "Are you sure you want to replace <{}>? [Y/N]\n>> ".format(i))
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
                        replace_check = input(
                            "Are you sure you want to replace <{}>? [Y/N]\n>> ".format(i))
            else:
                os.mkdir(check_current_item)
                new_folder_count += 1

        if new_folder_count > 0:
            return 1
        else:
            return 0

# print(FileLib().read_file("test.csv"))
