# Inisialisasi matriks kosong
matrix = []

# Membuat matriks 5x5 menggunakan append
for i in range(5):
    baris = []
    for j in range(5):
        baris.append(i * 5 + j + 1)  # Mengisi dengan angka 1-25
    matrix.append(baris)

# Menampilkan matriks
for baris in matrix:
    print(baris)