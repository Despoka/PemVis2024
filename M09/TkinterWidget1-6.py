import tkinter as tk
from tkinter import *
root = tk.Tk()
var = StringVar()
Frameku = tk.Frame(root, bg = 'blue')
Frameku.place(relwidth = 1, relheight = 1)

#Label
topframe = Frame(root)
topframe.pack(side = TOP)
label = Label(topframe, textvariable=var, relief=RAISED)
var.set("Mata Kuliah Pemrograman Visual Minggu 9")
label.pack()

#Check Mark
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(Frameku, text ="Masuk", variable = CheckVar1, onvalue = 1, offvalue = 0, height = 5, width = 10)
C2 = Checkbutton(Frameku, text ="Absen", variable = CheckVar2, onvalue = 1, offvalue = 0, height = 5, width = 10)
C1.pack(side='top', anchor='center', pady=10)
C2.pack(side='top', anchor='center', pady=10)

#Entry
L1 = Label(Frameku, text="Masukkan NIM anda dibawah")
L1.pack(side='top', anchor='center')
Entryku = tk.Entry(Frameku, bg = 'grey')
Entryku.pack(side='top', anchor='center', pady=10)

#Button
Tombolku = tk.Button(Frameku, text = "Tes Tombol", bg = 'white', fg = 'black')
Tombolku.pack(side='top', anchor='center', pady=10)


#Frame
bottomframe = Frame(root, bg='grey')
bottomframe.pack()

bottomframe = Frame(root)
bottomframe.pack (side = BOTTOM)

redbutton = Button(bottomframe, text="red", fg="red")
redbutton.pack(side = LEFT)

greenbutton = Button(bottomframe, text="green", fg="green")
greenbutton.pack(side = LEFT)

bluebutton = Button(bottomframe, text="blue", fg="blue")
bluebutton.pack(side = LEFT)

blackbutton = Button(bottomframe, text="black", fg="black")
blackbutton.pack(side = BOTTOM)




root.mainloop()