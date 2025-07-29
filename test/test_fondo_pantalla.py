from tkinter import *

root = Tk()

imagen= PhotoImage(file="fondo.png")

Label(root, image=imagen, bd=0).pack()

root.mainloop()