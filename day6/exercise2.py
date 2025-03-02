import os
def baca_file(fileName):
    try:
        with open(fileName,'r') as file:
            hasil = file.read()
            return hasil
    except FileNotFoundError:
        print('FILE NOT FOUND')
        return None

def buat_file(filename,content):
    if content:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename,'w') as file:
            file.write(content)

content = baca_file('sample.txt')
print(content)
buat_file("./data/tes.txt",content)