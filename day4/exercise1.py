def coba(input):
    daftar_set = set(input)
    daftar_list = list(daftar_set)[::-1]
    return daftar_list

nilai_awal = [1,2,3,3,4,4,5,6,7]
hasil = coba(nilai_awal)
print(f"nilai awal {nilai_awal}")
print(f"setelah di balik dan menghapus duplikat {hasil}")
