# Ubah element list
## ubah elemen ke-4 dengan nilai lainnya
from typing import overload


Olahraga = ['Futsal', 'Sepak Bola', 'Lari', 'Renang', 'Kasti', 'Badminton']
print()
print("List sebelum di ubah :", Olahraga)
print()
Olahraga[4] = 'Aerobik'
print("List sesudah di ubah :", Olahraga)
print()

## ubah elemen ke 4 sampai dengan elemen terakhir
Olahraga[4:] = ["Senam", "Karambol"]
print("Ubah element ke-4 hingga akhir :", Olahraga)
print()