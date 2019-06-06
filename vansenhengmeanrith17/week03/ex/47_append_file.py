import os
import datetime

def append_file(log):
    path = os.getcwd()
    logfile = path + "\\" + log
    log_input = ""
    f = open(logfile, 'a')
    while log_input != "EXIT":
        log_input = input("$: ")
        f.write("[{}] ".format(datetime.datetime.today().strftime("%d/%m/%Y %H:%M:%S")) + log_input + "\n")
    f.close()