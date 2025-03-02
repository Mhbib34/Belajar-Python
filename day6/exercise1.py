def buat_file(fileName,items):
    with open(fileName,'w') as file:
        for item in items:
            file.write(item + "\n")

def baca_file(fileName):
    try:
        with open(fileName,'r') as file:
            hasil = file.readlines()
            for item in hasil:
                print(item.strip())
    except FileNotFoundError:
        print('File not found!')

buah = ['apple','banana','grape','kiwi']
buat_file("buah.txt",buah)
baca_file("buah.txt")