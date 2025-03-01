import main as tes

while True :
    print('Menu')
    print('1.Tambah angka')
    print('2.Hapus angka')
    print('3.Tambah Berdasar Index')
    print('4.Hapus Berdasar Index')
    print('5.Tampilkan Angka')
    print('6.Urutkan Angka')
    print('7.Exit')
    user = int(input('Pilih [1,2,3,4,5,6,7] '))
    
    if user == 1:
        tes.tambah_angka()
    elif user == 2:
        tes.hapus_angka()
    elif user == 3:
        tes.tambah_angka_berdasar_index()
    elif user == 4:
        tes.hapus_angka_berdasar_index()
    elif user == 5:
        tes.tampilkan_angka()
    elif user == 6:
        tes.urutkan_angka()
    elif user == 7:
        print('Exiting Program')
        break
    else:
        print('Anda salah memasukkan angka!')