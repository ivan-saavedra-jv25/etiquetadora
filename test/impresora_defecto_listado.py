import win32print

def generar_listado_impresoras():

    impresoras  = win32print.EnumPrinters(2, None, 1)
    printer_name = win32print.GetDefaultPrinter()
    listado = []
    index_default = 0
    index = 0
    for impresora in impresoras:
        listado.append(impresora[2])
        if impresora[2] == printer_name:
            index_default = index
        
        index = index + 1

    return {  'lista': listado ,  'index_default': index_default }


data_empresoras = generar_listado_impresoras()

print("impresoras ")
print(data_empresoras['lista'])