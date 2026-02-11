import json
def open_file(name):
    file=open(name, 'r')
    return file
def print_json(name):
    print(json.dumps(json.load(open_file(name))))
print_json("ledger.json")
