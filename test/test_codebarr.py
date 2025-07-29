# from io import BytesIO
# import barcode
# from barcode.writer import ImageWriter


# EAN = barcode.get_barcode_class('ean13')
# my_ean = EAN('5901234123457', writer=ImageWriter(), render={'module_width': 0.2, 'module_height': 5 })



# fullname = my_ean.save('ean13_barcode')

# fp = BytesIO()
# my_ean.write(fp)

# with open("ean13_barcode.png", "wb") as f:
#     my_ean.write(f)  # Pillow (ImageWriter) produces RAW format here

from barcode import EAN13
from barcode.writer import ImageWriter

# Establecemos el directorio donde será guardado

render_options = {
            'module_width': 0.2,
            'module_height': 2,
            'text_distance': 1.5,
            'font_size': 4,
        }
# Establecemos el numero del código de barras
# Importante: el modelo EAN debe tener 12 digitos
numero = "202198447392"


#Generamos el código con un formato EAN13
mi_codigo = EAN13(numero, writer=ImageWriter())
mi_codigo = mi_codigo.render(render_options)

#Guardamos la imagen en el directorio previamente declarado
mi_codigo.save("ean13_barcode.png")

print(mi_codigo)