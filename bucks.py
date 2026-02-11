import json

file_path = 'ledger.json'

file=open(file_path, 'r')
data=json.load(file)
print("done")
print(json.dumps(data,indent=4))
