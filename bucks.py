import json
def print_json(name):
    print(json.dumps(json.load(open(name,'r'))))
def edit_json(data,filename):
    file=open(filename,'r+')
    filedata=json.load(file)
    filedata["transactions"].append(data)
    file.seek(0)
    json.dump(filedata,file,indent=4)
    file.truncate()
transaction={"from":"Braden","to":"Simonne","amount":15}
edit_json(transaction,"ledger.json")
#This is a test of the gitting

