import tkinter as tk
import tkinter.ttk as ttk
from tkinter import simpledialog

root = tk.Tk()
data = [
   ["Bandar",26,12000000],
   ["Jaki",31,9000000],
   ["Jore",18,7500000],
   ["Arfi",22, 10000000],
]
index=0
def read_data():
   for index, line in enumerate(data):
      tree.insert('', tk.END, iid = index,
         text = line[0], values = line[1:])
columns = ("umur", "gaji")

tree= ttk.Treeview(root, columns=columns ,height = 20)
tree.pack(padx = 5, pady = 5)

tree.heading('#0', text='Nama')
tree.heading('umur', text='Umur')
tree.heading('gaji', text='Gaji')

read_data()
root.mainloop()