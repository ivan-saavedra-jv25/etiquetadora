import tkinter as tk

# Función que se ejecuta al hacer clic en el botón
def reemplazar_ventana(nombre, apellido):
    # Destruimos la ventana actual
    ventana.destroy()

    # Creamos una nueva ventana
    nueva_ventana = tk.Tk()

    # Creamos un label y lo mostramos en la nueva ventana
    label = tk.Label(nueva_ventana, text=f"¡Hola {nombre} {apellido}!")
    label.pack()

# Creamos una instancia de la clase Tk
ventana = tk.Tk()

# Creamos los campos de texto
campo_nombre = tk.Entry(ventana)
campo_apellido = tk.Entry(ventana)

# Creamos una etiqueta para cada campo de texto
etiqueta_nombre = tk.Label(ventana, text="Nombre:")
etiqueta_apellido = tk.Label(ventana, text="Apellido:")

# Creamos un botón que llama a la función reemplazar_ventana al hacer clic
boton = tk.Button(ventana, text="Aceptar", command=lambda: reemplazar_ventana(campo_nombre.get(), campo_apellido.get()))

# Mostramos los campos de texto, etiquetas y botón en la ventana
etiqueta_nombre.pack()
campo_nombre.pack()
etiqueta_apellido.pack()
campo_apellido.pack()
boton.pack()

# Iniciamos el loop de la ventana
ventana.mainloop()
