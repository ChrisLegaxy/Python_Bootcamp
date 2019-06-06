import json
import os
import csv
import pandas as pd

def validate_json(myjson):
    try:
        f = open(myjson)
        json.load(f)
    except ValueError:
        return False
    return True

def json_to_tsv(myjson, mytsv):
    if os.path.exists(myjson): 
        if validate_json(myjson):
            json_file = open(myjson)
            json_file_loaded = json.load(json_file)
            f = open(mytsv,"w", newline='')
            json_file_header = list(json_file_loaded[0].keys())
            writer = csv.DictWriter (f, fieldnames = json_file_header, delimiter="\t")
            writer.writeheader()
            writer.writerows(json_file_loaded)
            f.close()
            return 1
    return 0