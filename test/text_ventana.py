from tkinter import *

root=Tk()
root.geometry("900x300")
root.resizable(0,0)
root.title("Ventana de ejemplo")

#  Actualizamos todo el contenido de la ventana (la ventana pude crecer si se le agrega
#  mas widgets).Esto actualiza el ancho y alto de la ventana en caso de crecer.

#  Obtenemos el largo y  ancho de la pantalla
wtotal = root.winfo_screenwidth()
htotal = root.winfo_screenheight()
#  Guardamos el largo y alto de la ventana
wventana = 900
hventana = 300

#  Aplicamos la siguiente formula para calcular donde debería posicionarse
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)

#  Se lo aplicamos a la geometría de la ventana
root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

root.mainloop()