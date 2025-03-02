import json
def say_hello(fileName):
    try:
        with open(fileName,'r') as file:
            hasil = json.load(file)
            for hello in hasil:
                print(f"Hallo {hello['name']}, Kamu hari ini berumur {hello['age']} tahun!")
                if hello['age'] <= 20:
                    print(f'{hello['name']} Kamu masih dibawah umur!')
    except FileNotFoundError:
        print('FILE NOT FOUND')

say_hello("./data/tes.json")