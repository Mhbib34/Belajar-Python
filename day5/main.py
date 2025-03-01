# nama = 'Muhammad Habib'
# pisah = nama.split()
# gabung = '|'.join(pisah)
# ganti = nama.replace('Habib','Farhan')
# print(nama)
# print(pisah)
# print(gabung)
# print(ganti)
import re

text = 'hubungi 123-456-7890'
print(re.findall(r'\d+', text))
print(re.sub(r'\d','X', text))