#Importar librería cv2
import cv2

#Leer imagen
img = cv2.imread('ean13_barcode.png')

#Características del texto
texto = "Producto"
ubicacion = (100,200)
font = cv2.FONT_HERSHEY_SIMPLEX
tamañoLetra = 1
colorLetra = (0,0,0)
grosorLetra = 2

#Escribir texto
cv2.putText(img, texto, ubicacion, font, tamañoLetra, colorLetra, grosorLetra)

#Guardar imagen
cv2.imwrite('textoQuito.jpg', img)

#Mostrar imagen
cv2.imshow('imagen',img)
cv2.waitKey(0)
cv2.destroyAllWindows()