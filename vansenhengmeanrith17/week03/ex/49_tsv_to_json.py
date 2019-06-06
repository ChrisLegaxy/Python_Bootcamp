import csv
import json

def validate_json(myjson):
    try:
        f = open(myjson)
        json.load(f)
    except ValueError:
        return False
    return True

def tsv_to_json(mytsv, myjson):

    f = open(mytsv, newline='')

    reader = csv.DictReader(f , delimiter= "\t")
        
    data = []
    # out = json.dumps([ row for row in reader])
    for row in reader:
        data.append(row)

    out = json.dumps(data)
    f = open(myjson,'w')
    f.write(out)
    f.close()

    if validate_json(myjson):
        return 1
    else:
        return 0


