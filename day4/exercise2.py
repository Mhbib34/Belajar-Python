import set as ma
def hitung_rata_rata(m):
    nilai_total = sum(m['nilai'].values())
    jumlah_nilai = len(m['nilai'])
    nilai_average = nilai_total /  jumlah_nilai
    print(f"{m['nama']} - Jumlah Nilai anda adalah {nilai_total}, Nilai rata-rata anda adalah {nilai_average}")
    
# hitung_rata_rata()
    
def hitung():
    for m in ma.mahasiswa:
        hitung_rata_rata(m)

hitung()