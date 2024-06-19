import tkinter as tk
from tkinter import *
from tkinter import messagebox
root = tk.Tk()

#ScrollBar
Frame1=tk.Frame(root)
Frame1.pack(side = RIGHT)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(root, yscrollcommand= scrollbar.set)
for line in range(100):
    mylist.insert(END, "This is line number " + str(line))

mylist.pack(side = LEFT, fill = BOTH)
scrollbar.config(command = mylist.yview)


#Text
Frame2=tk.Frame(root)
Frame2.pack()

text = Text(root)
text.insert (INSERT,"Hello.....")
text.insert(END,"Bye Bye.....")
text.pack()
text.tag_add("here", "1.0", "1.4")
text.tag_add("start","1.8","1.13")
text.tag_config("here", background="yellow", foreground="blue")
text.tag_config("start", background="black", foreground="green")

#TopLevel / Title
root.title("Tkinter Widgets Tutorial")

#Spinbox
Frame3=tk.Frame(root)
Frame3.pack()
w = Spinbox(Frame3, from_=0, to =20)
w.pack()

#Paned Window
Frame4=tk.Frame(root)
Frame4.pack()

m1 = PanedWindow(Frame4)
m1.pack(fill=BOTH, expand=1)

left = Entry(m1, bd=5)
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)

top=Scale(m2, orient=HORIZONTAL)
m2.add(top)

bottom=Button(m2, text="OK")
m2.add(bottom)

#LabelFrame
Frame5=tk.Frame(root)
Frame5.pack()

labelframe = LabelFrame(Frame5, text = "This is a LabelFrame")
labelframe.pack(fill="both",expand="yes")

left = Label(labelframe, text="Inside the LabelFrame")
left.pack()

#MessageBox
msg = Tk()
msg.geometry("100x100")
msg.title("Tutorial Message Box")
def hello():
    messagebox.showinfo("Say Hello","Hello World")

B1 = Button(msg,text = "Say Hello", command = hello)
B1.place(x=35,y=50)


root.mainloop()

