# M10/Project.py

import tkinter as tk
from tkinter.simpledialog import askinteger
from tkinter import messagebox

def draw_circle():
    canvas.delete("all")  #Menghapus bangun ruang yang lain
    radius = askinteger("Ukuran Lingkaran", "Masukkan Jari Jari Lingkaran:")
    canvas.create_oval(100-radius, 100-radius, 100+radius, 100+radius, outline="black", fill="red")
    luas = 3.14 * radius * radius
    messagebox.showinfo("Hasil", f"Luas lingkaran adalah: {luas}")

def draw_rectangle():
    canvas.delete("all")  # Menghapus bangun ruang yang lain
    width = askinteger("Ukuran Segiempat", "Masukkan Lebar Segiempat:")
    height = askinteger("Ukuran Segiempat", "Masukkan Tinggi Segiempat:")
    canvas.create_rectangle(100-width/2, 100-height/2, 100+width/2, 100+height/2, outline="black", fill="blue")
    luas = width * height
    messagebox.showinfo("Hasil", f"Luas Segiempat Adalah: {luas}")

def draw_triangle():
    canvas.delete("all")  # Menghapus bangun ruang yang lain
    base = askinteger("Ukuran Segitiga", "Masukkan Lebar Segitiga:")
    height = askinteger("Ukuran Segitiga", "Masukkan Tinggi Segitiga:")
    canvas.create_polygon(100-base/2, 100+height/2, 100+base/2, 100+height/2, 100, 100-height/2, outline="black", fill="green")
    luas = 0.5 * base * height
    messagebox.showinfo("Hasil", f"Luas Segitiga adalah: {luas}")

def draw_parallelogram():
    canvas.delete("all")  # Menghapus bangun ruang yang lain
    base = askinteger("Ukuran Jajargenjang", "Masukkan Lebar Jajargenjang:")
    height = askinteger("Ukuran Jajargenjang", "Masukkan Tinggi Jajargenjang:")
    canvas.create_polygon(100-base/2, 100+height/2, 100+base/2, 100+height/2, 100+base/2-50, 100-height/2, 100-base/2-50, 100-height/2, outline="black", fill="yellow")
    luas = base * height
    messagebox.showinfo("Hasil", f"Luas Jajargenjang Adalah: {luas}")

root = tk.Tk()
root.title("Aplikasi Menggambar Objek 2 Dimensi")

title_label = tk.Label(root, text="Silahkan Pilih", font=("Helvetica", 16))
title_label.pack()

scrollbar = tk.Scrollbar(root, orient="vertical")
scrollbar.pack(side="right", fill="y")

canvas = tk.Canvas(root, width=200, height=200, yscrollcommand=scrollbar.set)
canvas.pack()

scrollbar.config(command=canvas.yview)

circle_button = tk.Button(root, text="Buat Lingkaran", command=draw_circle)
circle_button.pack()

rectangle_button = tk.Button(root, text="Buat Segiempat", command=draw_rectangle)
rectangle_button.pack()

triangle_button = tk.Button(root, text="Buat Segitiga", command=draw_triangle)
triangle_button.pack()

parallelogram_button = tk.Button(root, text="Buat Jajargenjang", command=draw_parallelogram)
parallelogram_button.pack()

root.mainloop()