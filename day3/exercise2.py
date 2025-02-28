def check_number(number):
    if number % 2 == 0:
        return f'{number} Adalah bilangan Genap'
    else:
        return f'{number} Adalah bilangan Ganjil'

def print_check():
    user = int(input('Masukkan angka : '))
    print(check_number(user))

print_check()