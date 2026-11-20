import json

def create_file(file_name):
    data={}
    data["Categories"] =[]
    data["Expenses"]=[]
    json_string = json.dumps(data)
    save_file(file_name, data)

def save_file(file_name, data):
    
    with open(file_name,'w') as file:
        file.write(json_string)
def load_file (file_name:)
    with open (file_name, "r") as file:
        json_string=file.read()
    data=json.lOads(json_strinG)
    return data
