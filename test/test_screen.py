import tkinter as tk


def alinear_esquina_superior_izquierda(r):
    r.geometry("+0+0")


def alinear_esquina_inferior_derecha(r):
    r.geometry("-0-0")


def alinear_esquina_inferior_izquierda(r):
    r.geometry("+0-0")


def alinear_esquina_superior_derecha(r):
    r.geometry("-0+0")


def centrar(r):
    altura = r.winfo_reqheight()
    anchura = r.winfo_reqwidth()
    altura_pantalla = r.winfo_screenheight()
    anchura_pantalla = r.winfo_screenwidth()
    print(f"Altura: {altura}\nAnchura: {anchura}\nAltura de pantalla: {altura_pantalla}\nAnchura de pantalla: {anchura_pantalla}")
    x = (anchura_pantalla // 2) - (anchura//2)
    y = (altura_pantalla//2) - (altura//2)
    r.geometry(f"+{x}+{y}")


raiz = tk.Tk()
raiz.etiqueta = tk.Label( raiz, text="Me gusta estar centrado\nparzibyte.me")
raiz.etiqueta.pack(side="top")
app = tk.Frame()
app.pack()
raiz.update()
centrar(raiz)
app.mainloop()