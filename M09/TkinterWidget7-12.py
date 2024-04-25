import tkinter as tk
from tkinter import *
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def sel():
   selection = "You selected the option " + str(intvar.get())
   label.config(text = selection)

def sel2():
   selection = "Value = " + str(dblvar.get())
   label.config(text = selection)


root = Tk()
var = StringVar()
intvar = IntVar()
dblvar = DoubleVar()
Frame1 = tk.Frame(root)
Frame1.pack()

#ListBox
Lb1 = Listbox(Frame1)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")

Lb1.pack()

#Menu
Frame2 = tk.Frame(root)
Frame2.pack()
mb = Menubutton(Frame2, text="Presensi", relief=RAISED)
mb.grid()
mb.menu = Menu(mb,tearoff=0)
mb["menu"] = mb.menu

hadirVar = IntVar()
absenVar = IntVar()
mb.menu.add_checkbutton (label="Hadir", variable=hadirVar)
mb.menu.add_checkbutton (label="Absen", variable=absenVar)
mb.pack()

#MenuList
topframe = tk.Frame(root)
topframe.pack(side=TOP)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

#Message
Frame3 = tk.Frame(root)
Frame3.pack()

label = Message(Frame3,textvariable=var, relief=RAISED)
var.set("KAMIS 25 APRIL 2024")
label.pack()

#RadioButton
Frame4 = tk.Frame(root)
Frame4.pack()
R1 = Radiobutton(Frame4, text="Pilihan 1", variable=intvar, value=1, command=sel)
R2 = Radiobutton(Frame4, text="Pilihan 2", variable=intvar, value=2, command=sel)
R3 = Radiobutton(Frame4, text="Pilihan 3", variable=intvar, value=3, command=sel)
R1.pack(anchor = W)
R2.pack(anchor = W)
R3.pack(anchor = W)

#Scale
Frame5 = tk.Frame()
Frame5.pack()
scale = Scale(Frame5, variable=dblvar)
scale.pack(anchor = CENTER)

button = Button(Frame5, text="Get Scale Value", command=sel2)
button.pack(anchor = CENTER)
label = Label(root)
label.pack()

root.mainloop()