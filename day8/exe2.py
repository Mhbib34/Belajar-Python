import random
import numpy as np
array = [random.random() for _ in range(10)]
print(array)
print(f'Array Setelah Di urutkan : {sorted(array)}')
print(f'Angka terbesar di Array : {np.max(array)}')
print(f'Angka terkecil di Array : {np.min(array)}')


