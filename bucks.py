import json
def print_json(name):
    print(json.dumps(json.load(open(name,'r'))))
def edit_json(data,filename):
    file=load(filename,'r')
    filedata=json.load(file)
    filedata["transactions"].append(data)
    file.seek(0)
    json.dump(filedata,file)
transaction={"from":"Braden","to":"Simonne","amount":15}

