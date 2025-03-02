import json
try:
    with open('tes.json','r') as file :
        content = json.load(file)
        for hasil in content:
            print(f"Nama saya {hasil['nama']} umur saya {hasil['umur']}, saya berasal dari {hasil['alamat']} ")
except FileNotFoundError:
    print('404 : FILE NOT FOUND!')