print("\033c")
import numpy as np
import matplotlib.pyplot as plt

x1 = 100; y1 = 200
x2 = 100; y2 = 1000

pd = int(8); pr = 255; pg = 255; pb = 0
lw = int(8); lr = 255; lg = 255; lb = 0

col = 1920
row = 1080

def buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)
    hd = int(pd/2)
    hw = int(lw/2)
    dy = y2 - y1
    dx = x2 - x1

    # Membuat bagian vertikal huruf "B"
    for i in range(x1 - hd, x1 + hd):
        for j in range(y1 - hd, y1 + hd):
            if ((i - x1) ** 2 + (j - y1) ** 2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if ((i - x2) ** 2 + (j - y2) ** 2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    # Membuat bagian horizontal huruf "B"
    for i in range(x1 - hd, x2 + hd):
        for j in range(y1 - hd, y1 + hd):
            if (i <= x1) or (i >= x2):  # Mengatur bagian horizontal huruf "B"
                if ((i - x1) ** 2 + (j - y1) ** 2) < hd ** 2:
                    Gambar[j, i, 0] = pr
                    Gambar[j, i, 1] = pg
                    Gambar[j, i, 2] = pb

    # Menyembunyikan bagian yang tidak terlihat pada huruf "B"
    for i in range(x1 - hd, x1 + hd):
        for j in range(y2 - hd, y2 + hd):
            if ((i - x1) ** 2 + (j - y2) ** 2) < hd ** 2:
                Gambar[j, i, 0] = 0
                Gambar[j, i, 1] = 0
                Gambar[j, i, 2] = 0

    return Gambar

hasil = buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb)

plt.figure()
plt.imshow(hasil)
plt.show()
