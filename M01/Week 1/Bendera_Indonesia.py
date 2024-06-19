import numpy as np
import matplotlib.pyplot as plt

# Ukuran gambar
row = int(1080)
col = int(1920)

# Hitam (bagian merah)
Rrow1 = int(0.25 * row)
Rrow2 = int(0.5 * row)
Rcol1 = int(0.25 * col)
Rcol2 = int(0.75 * col)

# Putih (bagian putih)
Wrow1 = int(0.5 * row) + 1
Wrow2 = int(0.75 * row) + 1
Wcol1 = int(0.25 * col)
Wcol2 = int(0.75 * col)

# Membuat gambar bendera
Gambar = np.zeros((row, col, 3), dtype=np.int16)

# Mengisi bagian merah
for i in range(Rrow1, Rrow2):
    for j in range(Rcol1, Rcol2):
        Gambar[i, j, 0] = 255

# Mengisi bagian putih
for i in range(Wrow1, Wrow2):
    for j in range(Wcol1, Wcol2):
        Gambar[i, j, :] = 255

# Menampilkan gambar
plt.imshow(Gambar)
plt.show()
