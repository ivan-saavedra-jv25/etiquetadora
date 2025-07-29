import json

# Leer el archivo JSON
with open('datos.json', 'r') as archivo:
    datos = json.load(archivo)

# Mostrar los datos leídos
print("Datos originales:")
print(datos)

# Modificar los datos
datos['edad'] = 30
datos['ciudad'] = 'Otro ??lugar'
datos['producto']['grosor'] = 30

# Mostrar los datos modificados
print("\nDatos modificados:")
print(datos)

# Escribir los datos modificados de vuelta al archivo JSON
with open('datos.json', 'w') as archivo:
    json.dump(datos, archivo, indent=4)