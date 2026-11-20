import json

def create_file(file_name):
    data={}
    data["Categories"] =[]
    data["Expenses"]=[]
    save_file(file_name, data)
def save_file(file_name, data):
    json_string = json.dumps(data)
    with open(file_name,'w') as file:
        file.write(json_string)
def load_file (file_name):
    with open (file_name, "r") as file:
        json_string=file.read()
    data=json.loads(json_strinG)
    return data
