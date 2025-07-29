import tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# Position text in frame
Label(root, text = 'Position image on button', font =('<font_name>', 11)).pack(side = TOP, padx = 10, pady = 50)

# Create a photoimage object of the image in the path
photo = PhotoImage(file = "123456789123456789.png")

# Resize image to fit on button
photoimage = photo.subsample(1, 2)

# Position image on button
Label(root, image = photoimage,).pack(side = BOTTOM, pady = 50)
mainloop()