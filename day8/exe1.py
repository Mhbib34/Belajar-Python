import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

def hitung_baris():
    for array in arr :
        hasil = sum(array)
        result = np.array([hasil])
        print(result)
    print('\n')
def hitung_kolom():
    kolom = arr.T
    for array in kolom :
        hasil = sum(array)
        result = np.array([hasil])
        print(result)

print(arr)
hitung_baris()
print(arr.T)
hitung_kolom()