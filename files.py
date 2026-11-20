import json

def create_file(file_name):
    data={}
    data["Categories"] =[]
    data["Expenses"]=[]
    json_string = json.dumps(data)

    with open(file_name,'w') as file:
        file.write(json_string)
