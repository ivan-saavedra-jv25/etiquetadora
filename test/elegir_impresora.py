import win32print

# Enumerar todas las impresoras disponibles
impresoras = win32print.EnumPrinters(2, None, 1)
printer_name = win32print.GetDefaultPrinter ()

print("Defecto")
print(printer_name)
print()
# Imprimir la lista de impresoras
for impresora in impresoras:
    print(impresora)

    defecto = 'Defecto' if impresora[2] == printer_name else ''
    print("Nombre de la Impresora: {1}  - {0}".format(defecto,  impresora[2]) )
    # print("Descripción de la Impresora:", impresora[1])
    # print("Puerto de la Impresora:", impresora[3])
    
    print()

# Seleccionar una impresora específica por su nombre
nombre_impresora_deseada = "Nombre de la Impresora Deseada"
hprinter = win32print.OpenPrinter(nombre_impresora_deseada)

# Aquí puedes utilizar hprinter para imprimir en la impresora deseada
# ...

# Cerrar la impresora cuando hayas terminado
win32print.ClosePrinter(hprinter)
