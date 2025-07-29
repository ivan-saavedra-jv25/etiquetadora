from tkinter import *
from PIL import ImageTk, Image

ventana = Tk()
ventana.title('Frames en tkinter')


# Creacion de un frame
frame = Frame(ventana, bd=1, relief=SUNKEN, width=600 ,padx=20, pady=20)
#frame.pack(padx=20, pady=20)
frame.grid(row=0, column=0)

# Creacion de un frame
frame2 = Frame(ventana, bd=1, relief=SUNKEN, width=600 ,padx=20, pady=20)
#frame2.pack(padx=20, pady=20)
frame2.grid(row=0, column=2 )


# Creacion de un frame
frame3 = Frame(ventana, bd=1, relief=SUNKEN, width=600 ,padx=20, pady=20)
#frame2.pack(padx=20, pady=20)
frame3.grid(row=1,column=0, columnspan=2 )


# Creacion de widgets al interior de los frames
label = Label(frame, text='Este texto esta dentro del Frame')
label.grid(row=0, column=0)

label2 = Label(frame, text='Este texto esta dentro del Frame')
label2.grid(row=0, column=1)

label23 = Label(frame, text='Este texto esta dentro del Frame')
label23.grid(row=0, column=2)






# Creacion de widgets al interior de los frames
label = Label(frame2, text='Este texto esta dentro del Frame')
label.grid(row=0, column=0)

label2 = Label(frame2, text='Este texto esta dentro del Frame')
label2.grid(row=0, column=1)


label24 = Label(frame3, text='Este texto esta dentro del Frame')
label24.grid(row=0, column=2)


ventana.mainloop()