angka = []
def tambah_angka():
    user = int(input('Masukkan angka : '))
    angka.append(user)

def hapus_angka():
    user = int(input('Masukkan angka : '))
    angka.remove(user)
    print(f'{user} Telah dihapus!')
    tampilkan_angka()

def tampilkan_angka():
    print(angka)
    
def urutkan_angka():
    angka.sort()
    print('Angka Berhasil Diurutkan')
    tampilkan_angka()

def tambah_angka_berdasar_index():
    user_index = int(input('Index yang ingin ditambah : '))
    user = int(input('Masukkan angka : '))
    angka.insert(user_index,user)
    print(f'{user} Telah ditambahkan!')
    tampilkan_angka()
    
def hapus_angka_berdasar_index():
    user = int(input('Index yang ingin dihapus : '))
    print(f'{angka[user]} Telah dihapus!')
    del angka[user]
    tampilkan_angka()
    