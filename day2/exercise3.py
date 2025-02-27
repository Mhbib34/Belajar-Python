angka = []
while True:
    user = int(input('Masukkan angka :'))
    angka.append(user)
    if user == 0 :
        angka.remove(0)
        break

angka.sort()
print(angka)
print(f'Angka yang paling besar adalah {angka[-1]}')