import os
import json
def create_file(fileName,content):
    try:
        os.makedirs(os.path.dirname(fileName), exist_ok=True)
        with open(fileName,'r') as file:
            result = json.load(file)
    except FileNotFoundError:
        result = []
        
    result.append(content)
    
    with open(fileName,'w') as file:
        json.dump(result,file)
        
def content(name,age):
    return {"name": name,"age":age}
    
input_name = input('Enter your name : ')
input_age = int(input('Enter your age : '))
user_content = content(input_name,input_age)
create_file('./data/tes.json', user_content)
