def factorial(a):
    angka = 1
    for i in range(1, a +1):
        angka *= i
    return angka

print('Welcome to the calculator \n')
while True:
    print('Menu')
    print('1.Tambah')
    print('2.Kurang')
    print('3.Kali')
    print('4.Bagi')
    print('5.Modulus')
    print('6.Faktorial')
    print('7.Exit') 
    user = int(input('Pilih menu [1,2,3,4,5,6,7] '))
    
    
    if user == 7:
        print('Exiting Program')
        break
    
    if user == 1:
        hasil = angka1 + angka2
        print(f'Hasilnya adalah {hasil} \n')
    elif user == 2:
        hasil = angka1 - angka2
        print(f'Hasilnya adalah {hasil} \n')
    elif user == 3:
        hasil = angka1 * angka2
        print(f'Hasilnya adalah {hasil} \n')
    elif user == 4:
        hasil = angka1 / angka2
        print(f'Hasilnya adalah {hasil} \n')
    elif user == 5:
        hasil = angka1 % angka2
        print(f'Hasilnya adalah {hasil} \n')
    elif user == 6:
        angka1 = int(input('Masukkan angka : '))
        print(f'Hasilnya adalah {factorial(angka1)} \n')
        continue
    else:
        print('Anda SALAH memasukkan angka')
        break
    
    angka1 = int(input('Masukkan angka pertama : '))
    angka2 = int(input('Masukkan angka kedua : '))