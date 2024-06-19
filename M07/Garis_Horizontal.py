print("\033c")  # Untuk membersihkan konsol
import numpy as np
import matplotlib.pyplot as plt

# Koordinat dua titik untuk garis horizontal
x1_h = 100
y1_h = 300
x2_h = 800
y2_h = 300

# Ketebalan garis yang diinginkan pengguna
lw = int(10)

# Menghitung setengah ketebalan garis
hw = int(lw / 2)

# Fungsi untuk menggambar titik tebal
def draw_thick_point(x, y, color, thickness):
    for i in range(x - thickness, x + thickness):
        for j in range(y - thickness, y + thickness):
            if (i >= 0 and i < col and j >= 0 and j < row):
                if ((i - x)**2 + (j - y)**2) < thickness**2:
                    Gambar[j, i] = color

# Fungsi untuk menggambar titik
def draw_point(x, y, color):
    for i in range(x - hw, x + hw):
        for j in range(y - hw, y + hw):
            if (i >= 0 and i < col and j >= 0 and j < row):
                if ((i - x)**2 + (j - y)**2) < hw**2:
                    Gambar[j, i] = color

# Menentukan ukuran kanvas
row = int(5 / 7 * 1080)
col = int(5 / 7 * 1920)
print('col, row = ', col, ', ', row)

# Mempersiapkan kanvas hitam
Gambar = np.zeros(shape=(row, col, 3), dtype=np.int16)

# Gambar garis horizontal
for x in range(x1_h, x2_h + 1):  # Melangkah melalui setiap koordinat x
    y = y1_h  # Koordinat y konstan
    draw_point(x, y, [255, 0, 0])  # Menggambar titik merah

# Menggambar titik tebal pada koordinat awal dan akhir garis horizontal
draw_thick_point(x1_h, y1_h, [255, 0, 0], hw * 2)  # Menggambar titik merah tebal
draw_thick_point(x2_h, y2_h, [255, 0, 0], hw * 2)  # Menggambar titik merah tebal

plt.figure()
plt.imshow(Gambar)
plt.show()
