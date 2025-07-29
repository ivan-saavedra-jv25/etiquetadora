from tkinter import ttk
import tkinter as tk
from tkinter import PhotoImage
import requests
# from io import BytesIO
# import barcode

import cv2
from tkinter import messagebox
# from PIL import Image

from barcode import EAN13
from barcode import Code128
from barcode.writer import ImageWriter

import win32print
import win32ui
from PIL import Image, ImageWin
import os

import time
from tkinter import messagebox

import code128
import io
from PIL import Image, ImageDraw, ImageFont

import json

import barcode
from barcode.writer import ImageWriter

WIDTH = 1000
HEIGTH = 600
MM_PX = 3.77952755906
TITULO = "OneCode - Codigo de Barra"
# URL = 'http://www.do-re-mi.cl/api'
URL = 'http://3.12.198.210/api'
URL_LOGIN = "{}/login".format(URL)
URL_PRODUCTO = "{}/get/producto/especifico".format(URL)


_base = os.path.abspath(os.getcwd())

_recursos = f"{_base}\\recursos\\"
_fuente = f"{_recursos}arial.ttf"
_file_favicon = f"{_recursos}favicon.png"
_file_codigo_barra = f"{_recursos}codigo_barra.png"
_file_codigo_barra_final = f"{_recursos}codigo_barra_final.png"
_file_block_header = f"{_recursos}block_header.png"
_file_block = f"{_recursos}block.png"
_file_logo = f"{_recursos}logo-black.png"
_file_json = f"{_recursos}configuracion.json"
_file_logo_pie = f"{_recursos}fondo_logo.png"



class Producto:
    def __init__(self, nombre = '', precio = '', codigo = '') -> None:
        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo
        pass
    def get_nombre(self):
        return self.nombre
    def get_precio(self):
        return self.precio
    def get_codigo(self):
        return self.codigo


class Textos:
    tamanio: int

    def __init__(self, _texto, _tamanio: int, _x, _y, _grosor) -> None:
        self.texto = _texto
        self.tamanio = _tamanio
        self.x = _x
        self.y = _y
        self.grosor = _grosor

    def get_texto(self):
        return self.texto

    def set_texto(self, new_texto):
        self.texto = new_texto

    def get_tamanio(self):
        return self.texto

    def set_tamanio(self, new_tamanio):
        self.tamanio = new_tamanio

    def get_x(self):
        return self.texto

    def set_x(self, new_x):
        self.x = new_x

    def get_y(self):
        return self.texto

    def set_y(self, new_y):
        self.y = new_y

    def get_grosor(self):
        return self.grosor

    def set_grosor(self, grosor):
        self.grosor = grosor

    def __str__(self) -> str:
        return f' Texto : {self.texto}  - Tamanio : {self.tamanio} - Eje X : {self.x} - Eje Y : {self.y}'

    pass


class CodeBar:
    textos = []

    def get_label(self) -> tk.Label:
        return self.label

    def set_label(self, _label):
        self.label = _label

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, _codigo):
        self.codigo = _codigo

    def get_filename(self):
        return self.filename

    def set_filename(self, _filename):
        self.filename = _filename

    def get_textos(self) -> list:
        return self.textos

    def set_textos(self, _lista_texto):
        self.textos = _lista_texto

    def get_label_final(self) -> tk.Label:
        return self.label_final

    def set_label_final(self, _label):
        self.label_final = _label

    def get_filename_final(self):
        return self.filename_final

    def set_filename_final(self, _filename):
        self.filename_final = _filename

    pass


class MetaData:
    def __init__(self, ) -> None:
        self.TOKEN = ''
        #self.producto = None -> Producto

    def get_token(self):
        return self.TOKEN

    def set_token(self, _token):
        self.TOKEN = _token

    def get_producto(self) -> Producto:
        return self.producto

    def set_producto(self, _producto):
        self.producto = _producto

    def get_window(self) -> tk.Tk:
        return self.window

    def set_window(self, _window):
        self.window = _window

    def get_diccionario_producto(self):
        return self.dict_producto

    def set_diccionario_producto(self, _diccionario):
        self.dict_producto = _diccionario

    def get_diccionario_precio(self):
        return self.dict_precio

    def set_diccionario_precio(self, _diccionario):
        self.dict_precio = _diccionario

    def get_diccionario_codigo_barra(self):
        return self.dict_codigo_barra

    def set_diccionario_codigo_barra(self, _diccionario):
        self.dict_codigo_barra = _diccionario
    
    def get_posicionamiento(self):
        return self.posicionamiento
    def set_posicionamiento(self, _posicionamiento):
        with open(_file_json, 'w') as archivo:
            json.dump(_posicionamiento, archivo, indent=4)
        self.posicionamiento = _posicionamiento



class CustomImageWriter(ImageWriter):
    def get_font(self, **kwargs):
        # Carga la fuente desde el recurso personalizado
        font_path = _fuente  # Reemplaza con la ruta real a tu recurso
        
        font_size = kwargs.get('font_size', 5)
        return self._load_font(font_path, font_size) # type: ignore
    
meta = MetaData()
code_bar = CodeBar()


def view_print():
    root.destroy()
    window = tk.Tk()
    window.state('zoomed')
    window.title(TITULO)

    meta.set_window(window)
    window = meta.get_window()
    
    window.geometry("%dx%d" % (WIDTH, HEIGTH))

    # Crear un LabelFrame en la parte superior
    label_frame_top = tk.LabelFrame(window)
    
    label_frame_top.pack(fill="x")

    # Agregar contenido al LabelFrame superior
    frame_horizontal = tk.Frame(label_frame_top)
    
    frame_horizontal.pack()

    widgets_labelframe_superiror(frame_horizontal)
    #fin Frame Top

    # Crear un Frame maestro para los LabelFrames inferiores
    frame_inferior = tk.Frame(window)
    frame_inferior.pack(fill="both", expand=True)

    # Crear un Frame para los cuatro LabelFrames inferiores
    frame_label_frames = tk.Frame(frame_inferior)
    
    frame_label_frames.pack(fill="both", expand=True)

    # Crear cuatro LabelFrames dentro del Frame de los LabelFrames inferiores
    label_frame1 = tk.LabelFrame(frame_label_frames, text="Nombre")
    label_frame1.pack(fill="both", expand=True, side="left")
    #Contenido del LabelFrame 1
    widgets_labelframe_nombre_producto(label_frame1)



    label_frame2 = tk.LabelFrame(frame_label_frames, text="Precio")
    label_frame2.pack(fill="both", expand=True, side="left")
    widgets_labelframe_precio_producto(label_frame2)


    label_frame3 = tk.LabelFrame(frame_label_frames, text="Codigo Barra")
    label_frame3.pack(fill="both", expand=True, side="left")
    widgets_labelframe_codigo_producto(label_frame3)

    label_frame4 = tk.LabelFrame(frame_label_frames, text="Preparar Imprecion")
    label_frame4.pack(fill="both", expand=True, side="left")
    widgets_labelframe_preparar_imprecion(label_frame4)


    # Crear un Frame maestro para los dos LabelFrames inferiores adicionales
    frame_label_frames_inferiores = tk.Frame(frame_inferior)
    frame_label_frames_inferiores.pack(fill="both", expand=True)

    # Crear dos LabelFrames adicionales dentro del Frame de los LabelFrames inferiores
    label_frame5 = tk.LabelFrame(frame_label_frames_inferiores, text="Codigo de Barra")
    label_frame5.pack(fill="both", expand=True, side="left")
    

    # Cargar la imagen
    imagen = PhotoImage(file=_file_codigo_barra)
    imagen = imagen.subsample(1, 2)

    # Crear un Label para mostrar la imagen
    labetl_img = tk.Label(label_frame5, image=imagen)
    labetl_img.pack()


    # Cargar la imagen
    imagen3 = PhotoImage(file=_file_logo_pie)
    imagen3 = imagen3.subsample(3, 3)

    # Crear un Label para mostrar la imagen
    labetl_img2 = tk.Label(label_frame5, image=imagen3)
    labetl_img2.pack(fill="both", expand=True, side="top")
  

    label_frame6 = tk.LabelFrame(frame_label_frames_inferiores, text="Tira de Codigos")
    label_frame6.pack(fill="both", expand=True, side="left")

    # Cargar la imagen
    imagen2 = PhotoImage(file=_file_codigo_barra_final)
    imagen2 = imagen2.subsample(4,4)

    # Crear un Label para mostrar la imagen
    labetl_img_final = tk.Label(label_frame6, image=imagen2)
    labetl_img_final.pack()

    code_bar.set_label(labetl_img)
    code_bar.set_label_final(labetl_img_final)


    window.mainloop()

    pass

def widgets_labelframe_superiror(_labelframe):


    etq_producto = tk.Label(_labelframe, text="Buscar Producto :", font=("Arial", 15))
    txt_producto = tk.Entry(_labelframe, font=("Arial", 15))



    combo = ttk.Combobox(_labelframe, state="readonly", font=("Arial", 15), values=["Codigo Barra", "Codigo Producto"])
    combo.current(0)

    boton_producto = tk.Button(_labelframe, font=("Arial", 15), text="Buscar!"  , command=lambda: buscar_producto(txt_producto.get(), combo.get()))


    etq_producto.grid(row=0, column=1, padx=10, pady=10, ipady=7.5, ipadx=20)
    txt_producto.grid(row=0, column=2, columnspan=2, padx=10, pady=10, ipady=7.5, ipadx=60)
    combo.grid(row=0, column=4, padx=10, pady=10, ipady=7.5)
    boton_producto.grid(row=0, column=5, padx=5, pady=10, ipady=7.5, ipadx=30)




    pass

def widgets_labelframe_nombre_producto(_labelframe):

    _padx = 1
    _pady = 2
    

    etq_nombre = tk.Label(_labelframe, text="Nombre Producto :", font=("Arial", 10))
    txt_nombre = tk.Entry(_labelframe, font=("Arial", 10))

    etq_nombre.grid(row=1, column=1  , padx=_padx, pady=_pady)
    txt_nombre.grid(row=1, column=2  , padx=_padx, pady=_pady)

    etq_tamanio = tk.Label(_labelframe, text="Tamaño Letra :", font=("Arial", 10))
    combo_tamanio = ttk.Combobox(_labelframe, state="readonly", values=["1", "2", "3"])
    combo_tamanio.current(0)

    etq_tamanio.grid(row=2, column=1 , padx=_padx, pady=_pady)
    combo_tamanio.grid(row=2, column=2 , padx=_padx, pady=_pady)


    etq_grosor = tk.Label(_labelframe, text="Grosor Letra :", font=("Arial", 10))
    combo_grosor = ttk.Combobox(_labelframe, state="readonly", values=["1", "2", "3"])
    combo_grosor.current(0)

    etq_grosor.grid(row=3, column=1 , padx=_padx, pady=_pady)
    combo_grosor.grid(row=3, column=2 , padx=_padx, pady=_pady)


    etq_eje_x = tk.Label(_labelframe, text="Eje X (Izquier / derecha) :", font=("Arial", 10))
    slider_eje_x = ttk.Scale( _labelframe, from_=0, to=1000, orient='horizontal' )

    

    etq_eje_x.grid(row=4, column=1 , padx=_padx, pady=_pady)
    slider_eje_x.grid(row=4, column=2 , padx=_padx, pady=_pady, sticky='we')

    etq_eje_y = tk.Label(_labelframe, text="Eje Y (Arriba / Abajo) :", font=("Arial", 10))
    slider_eje_y = ttk.Scale( _labelframe, from_=0, to=1000, orient='horizontal' )

    etq_eje_y.grid(row=5, column=1 , padx=_padx, pady=_pady)
    slider_eje_y.grid(row=5, column=2 , padx=_padx, pady=_pady, sticky='we')


    dict_producto = {"nombre": txt_nombre, "tamanio": combo_tamanio, "x": slider_eje_x, "y": slider_eje_y, "grosor": combo_grosor, }

    txt_nombre.bind("<FocusOut>", calculo_producto_posicion)
    combo_tamanio.bind("<FocusOut>", calculo_producto_posicion)
    combo_grosor.bind("<FocusOut>", calculo_producto_posicion)

    slider_eje_x.bind("<ButtonRelease-1>", calculo_producto_posicion)
    slider_eje_y.bind("<ButtonRelease-1>", calculo_producto_posicion)

    meta.set_diccionario_producto(dict_producto)
    





    pass

def widgets_labelframe_precio_producto(_labelframe):

    _padx = 1
    _pady = 2
    

    etq_precio = tk.Label(_labelframe, text="Precio ($) :", font=("Arial", 10))
    txt_precio = tk.Entry(_labelframe, font=("Arial", 10))

    etq_precio.grid(row=1, column=1  , padx=_padx, pady=_pady)
    txt_precio.grid(row=1, column=2  , padx=_padx, pady=_pady)

    etq_tamanio_precio = tk.Label(_labelframe, text="Tamaño Letra :", font=("Arial", 10))
    combo_tamanio_precio = ttk.Combobox(_labelframe, state="readonly", values=["1", "2", "3"])
    combo_tamanio_precio.current(0)

    etq_tamanio_precio.grid(row=2, column=1 , padx=_padx, pady=_pady)
    combo_tamanio_precio.grid(row=2, column=2 , padx=_padx, pady=_pady)


    etq_grosor_precio = tk.Label(_labelframe, text="Grosor Letra :", font=("Arial", 10))
    combo_grosor_precio = ttk.Combobox(_labelframe, state="readonly", values=["1", "2", "3"])
    combo_grosor_precio.current(0)

    etq_grosor_precio.grid(row=3, column=1 , padx=_padx, pady=_pady)
    combo_grosor_precio.grid(row=3, column=2 , padx=_padx, pady=_pady)


    etq_eje_x_precio = tk.Label(_labelframe, text="Eje X (Izquier / derecha) :", font=("Arial", 10))
    slider_eje_x_precio = ttk.Scale( _labelframe, from_=0, to=1000, orient='horizontal' )

    etq_eje_x_precio.grid(row=4, column=1 , padx=_padx, pady=_pady)
    slider_eje_x_precio.grid(row=4, column=2 , padx=_padx, pady=_pady, sticky='we')

    etq_eje_y_precio = tk.Label(_labelframe, text="Eje Y (Arriba / Abajo) :", font=("Arial", 10))
    slider_eje_y_precio = ttk.Scale( _labelframe, from_=0, to=1000, orient='horizontal' )

    etq_eje_y_precio.grid(row=5, column=1 , padx=_padx, pady=_pady)
    slider_eje_y_precio.grid(row=5, column=2 , padx=_padx, pady=_pady, sticky='we')
    

    dict_precio = {"precio": txt_precio, "tamanio": combo_tamanio_precio, "x": slider_eje_x_precio, "y": slider_eje_y_precio, "grosor": combo_grosor_precio, }

    txt_precio.bind("<FocusOut>", calculo_producto_posicion)
    combo_tamanio_precio.bind("<FocusOut>", calculo_producto_posicion)
    combo_grosor_precio.bind("<FocusOut>", calculo_producto_posicion)

    slider_eje_x_precio.bind("<ButtonRelease-1>", calculo_producto_posicion)
    slider_eje_y_precio.bind("<ButtonRelease-1>", calculo_producto_posicion)

    meta.set_diccionario_precio(dict_precio)



    pass

def widgets_labelframe_codigo_producto(_labelframe):

    _padx = 1
    _pady = 2
    

    etq_codigo = tk.Label(_labelframe, text="Codigo de Barra :", font=("Arial", 10))
    txt_codigo = tk.Entry(_labelframe, font=("Arial", 10),)

    etq_codigo.grid(row=1, column=1  , padx=_padx, pady=_pady)
    txt_codigo.grid(row=1, column=2  , padx=_padx, pady=_pady)

    etq_tamanio_codigo = tk.Label(_labelframe, text="Tamaño Letra :", font=("Arial", 10))
    combo_tamanio_codigo = ttk.Combobox(_labelframe, state="readonly", values=["1", "2", "3"])
    combo_tamanio_codigo.current(0)

    etq_tamanio_codigo.grid(row=2, column=1 , padx=_padx, pady=_pady)
    combo_tamanio_codigo.grid(row=2, column=2 , padx=_padx, pady=_pady)


    etq_grosor_codigo = tk.Label(_labelframe, text="Grosor Letra :", font=("Arial", 10))
    combo_grosor_codigo = ttk.Combobox(_labelframe, state="readonly", values=["1", "2", "3"])
    combo_grosor_codigo.current(0)

    etq_grosor_codigo.grid(row=3, column=1 , padx=_padx, pady=_pady)
    combo_grosor_codigo.grid(row=3, column=2 , padx=_padx, pady=_pady)


    etq_eje_x_codigo = tk.Label(_labelframe, text="Eje X (Izquier / derecha) :", font=("Arial", 10))
    slider_eje_x_codigo = ttk.Scale( _labelframe, from_=0, to=1000, orient='horizontal' )

    etq_eje_x_codigo.grid(row=4, column=1 , padx=_padx, pady=_pady)
    slider_eje_x_codigo.grid(row=4, column=2 , padx=_padx, pady=_pady, sticky='we')

    etq_eje_y_codigo = tk.Label(_labelframe, text="Eje Y (Arriba / Abajo) :", font=("Arial", 10))
    slider_eje_y_codigo = ttk.Scale( _labelframe, from_=0, to=1000, orient='horizontal' )

    etq_eje_y_codigo.grid(row=5, column=1 , padx=_padx, pady=_pady)
    slider_eje_y_codigo.grid(row=5, column=2 , padx=_padx, pady=_pady, sticky='we')
    

    dict_codigo = {"codigo": txt_codigo, "tamanio": combo_tamanio_codigo, "x": slider_eje_x_codigo, "y": slider_eje_y_codigo, "grosor": combo_grosor_codigo, }

    txt_codigo.bind("<FocusOut>", calculo_producto_posicion)
    combo_tamanio_codigo.bind("<FocusOut>", calculo_producto_posicion)
    combo_grosor_codigo.bind("<FocusOut>", calculo_producto_posicion)

    slider_eje_x_codigo.bind("<ButtonRelease-1>", calculo_producto_posicion)
    slider_eje_y_codigo.bind("<ButtonRelease-1>", calculo_producto_posicion)

    meta.set_diccionario_codigo_barra(dict_codigo)



    pass

def widgets_labelframe_preparar_imprecion(_labelframe):

    _padx = 1
    _pady = 2

    data_empresoras = generar_listado_impresoras()


    etq_cantidad_horizoltal_papel = tk.Label(_labelframe, text="Cantidad Copia Horizontal :", font=("Arial", 10))
    txt_cantidad_horizoltal_papel = tk.Entry(_labelframe, font=("Arial", 10))
    insert_data_entry(txt_cantidad_horizoltal_papel,3)
    etq_cantidad_horizoltal_papel.grid(row=1, column=1  , padx=_padx, pady=_pady)
    txt_cantidad_horizoltal_papel.grid(row=1, column=2  , padx=_padx, pady=_pady)

    etq_cantidad_linea_papel = tk.Label(_labelframe, text="Cantidad Copia Lineas :", font=("Arial", 10))
    txt_cantidad_linea_papel = tk.Entry(_labelframe, font=("Arial", 10))
    insert_data_entry(txt_cantidad_linea_papel,2)
    etq_cantidad_linea_papel.grid(row=2, column=1  , padx=_padx, pady=_pady)
    txt_cantidad_linea_papel.grid(row=2, column=2  , padx=_padx, pady=_pady)

    etq_impresora = tk.Label(_labelframe, text="Impresora por Defecto :", font=("Arial", 10))
    combo_impresora = ttk.Combobox(_labelframe, state="readonly", values=data_empresoras['lista'])
    combo_impresora.current(data_empresoras['index_default'])

    etq_impresora.grid(row=3, column=1 , padx=_padx, pady=_pady)
    combo_impresora.grid(row=3, column=2 , padx=_padx, pady=_pady)

    dict_preparar = {  "copia_h": txt_cantidad_horizoltal_papel, "cantidad": txt_cantidad_linea_papel, "impresora": combo_impresora, }


    boton_preparar = tk.Button(_labelframe, font=("Arial", 15), text="Preparar" ,command=lambda: calcular_img_impresion(dict_preparar))
    boton_preparar.grid(row=4, column=1, padx=5, pady=10, ipady=4)

    boton_imprimir = tk.Button(_labelframe, font=("Arial", 15), text="Imprimir" , command=lambda: imprimir_etiquetas(dict_preparar))
    boton_imprimir.grid(row=4, column=2, padx=5, pady=10, ipady=4)




    pass

def widgets_labelframe_imagen_codigo(_labelframe):

    # Cargar la imagen
    imagen = PhotoImage(file=_file_codigo_barra)
    imagen = imagen.subsample(1, 2)

    # Crear un Label para mostrar la imagen
    label_imagen = tk.Label(_labelframe, image=imagen)
    label_imagen.pack()


    
    pass

def generar_view_login():
    # empresa

    image3 = tk.PhotoImage(file=_file_logo)
    image3 = image3.subsample(3, 3)
    img_logo = tk.Label(root, image=image3)


    etq_empresa = tk.Label(root, text="Empresa :" ,font=("Arial", 11))
    txt_empresa = tk.Entry(root ,font=("Arial", 11))

    
    
    # usuario
    etq_usuario = tk.Label(root, text="Usuario :" ,font=("Arial", 11))
    txt_usuario = tk.Entry(root ,font=("Arial", 11))
    
    # password
    etq_password = tk.Label(root, text="Password :" ,font=("Arial", 11))
    txt_password = tk.Entry(root, show="*" ,font=("Arial", 11))
    
    
    # Boton
    boton = tk.Button(root, text="Login", command=lambda: request_login(txt_empresa.get(), txt_usuario.get(), txt_password.get()) ,font=("Arial", 11))

    img_logo.grid(row=0, column=1,columnspan=3 ,pady=(0, 30))
    img_logo.image = image3 # type: ignore

    etq_empresa.grid(row=1, column=1, padx=10, pady=5, ipady=1, ipadx=1)
    txt_empresa.grid(row=1, column=2, padx=10, pady=5, ipady=1, ipadx=1)

    etq_usuario.grid(row=2, column=1, padx=10, pady=5, ipady=1, ipadx=1)
    txt_usuario.grid(row=2, column=2, padx=10, pady=5, ipady=1, ipadx=1)

    etq_password.grid(row=3, column=1, padx=10, pady=5, ipady=1, ipadx=1)
    txt_password.grid(row=3, column=2, padx=10, pady=5, ipady=1, ipadx=1)

    boton.grid(row=4, column=2, padx=5, pady=10, ipady=3, ipadx=30 )

    insert_data_entry(txt_empresa, '77926573-0')



    pass


def request_login(_empresa, _usuario, _password):

    # print(f"Empresa : {_empresa}")
    # print(f"Usuario : {_usuario}")
    # print(f"Password : {_password}")

    if _empresa == '' or _usuario == '' or _password == '':
        messagebox.showinfo(message="Todos los Campos son requeridos", title="Informacion!")
        return

    body = {'empresa': _empresa, 'username': _usuario, 'password': _password}

    solicitud = requests.post(URL_LOGIN, json=body)

    if solicitud.status_code == 200:
        json_post = solicitud.json()
        json_post = json_post[0]

        _token = json_post['Token']

        if _token != '':
            meta.set_token(_token)
            view_print()
        else:
            messagebox.showinfo(message="Hubo un Error inesperado", title="Título")
            pass
        pass
    elif solicitud.status_code == 401:
        json_post = solicitud.json()
        messagebox.showinfo(message=json_post['mensaje'], title="Informacion!")

        pass
    pass


def buscar_producto(_codigo, _tipo):
    _tipo = 'barra' if _tipo == 'Codigo Barra' else ''
    _token = meta.get_token()
    header = {'Content-type': 'application/xml', 'codigo': _codigo, 'tipo': _tipo, 'token': _token}

    solicitud = requests.get(URL_PRODUCTO, headers=header)

    if solicitud.status_code == 200:
        json_post = solicitud.json()

        if len(json_post) == 0:
            messagebox.showinfo(message="Produco mal Buscado o Producto no Creado", title="Busqueda de Producto")
            return
        # if len(json_post['codigo_barra']) != 13:
        #     messagebox.showinfo(message="Codigo de barra debe tener 13 Digitos", title="Formato Incorrecto")
        #     return
        
        #print(json_post)
        producto = Producto(nombre = json_post['nombre'], precio = f"${formato_numero(json_post['precio_venta'])}", codigo=json_post['codigo_barra'])
        
        meta.set_producto(producto)

        posicionamiento = get_data_defecto_posicionamiento()
   


        code_bar.set_codigo(producto.get_codigo())

        lista_texto = []

        dict_producto = meta.get_diccionario_producto()
        dict_precio = meta.get_diccionario_precio()
        dict_codigo = meta.get_diccionario_codigo_barra()
        
        

        _nombre = producto.get_nombre()
        _tamanio = posicionamiento['producto']['tamanio']
        _x = posicionamiento['producto']['x']
        _y = posicionamiento['producto']['y']
        _grosor = posicionamiento['producto']['grosor']

        nombre = Textos(_nombre, _tamanio, _x, _y, _grosor)

        insert_data_entry(dict_producto['nombre'], _nombre)
        insert_combobox_data_entry(dict_producto['tamanio'], (_tamanio-1))
        insert_combobox_data_entry(dict_producto['grosor'], (_grosor-1))
        insert_range_data_entry(dict_producto['x'], _x)
        insert_range_data_entry(dict_producto['y'], _y)

        _precio_venta = producto.get_precio()
        _tamanio_precio = posicionamiento['precio']['tamanio']
        _x_precio = posicionamiento['precio']['x']
        _y_precio = posicionamiento['precio']['y']
        _grosor_precio = posicionamiento['precio']['grosor']

        precio = Textos(_precio_venta, _tamanio_precio, _x_precio, _y_precio, _grosor_precio)

        insert_data_entry(dict_precio['precio'], _precio_venta)
        insert_combobox_data_entry(dict_precio['tamanio'], (_tamanio_precio-1))
        insert_combobox_data_entry(dict_precio['grosor'], (_grosor_precio-1))
        insert_range_data_entry(dict_precio['x'], _x_precio)
        insert_range_data_entry(dict_precio['y'], _y_precio)


        _codigo_barra = producto.get_codigo()
        _tamanio_codigo = posicionamiento['codigo']['tamanio']
        _x_codigo = posicionamiento['codigo']['x']
        _y_codigo = posicionamiento['codigo']['y']
        _grosor_codigo = posicionamiento['codigo']['grosor']

        codigo = Textos(_codigo_barra, _tamanio_codigo, _x_codigo, _y_codigo, _grosor_codigo)

        insert_data_entry(dict_codigo['codigo'], _codigo_barra)
        insert_combobox_data_entry(dict_codigo['tamanio'], (_tamanio_codigo-1))
        insert_combobox_data_entry(dict_codigo['grosor'], (_grosor_codigo-1))
        insert_range_data_entry(dict_codigo['x'], _x_codigo)
        insert_range_data_entry(dict_codigo['y'], _y_codigo)


        lista_texto.append(nombre)
        lista_texto.append(precio)
        lista_texto.append(codigo)

        code_bar.set_textos(lista_texto)

        render_img()

    pass


def render_img():
    producto = meta.get_producto()

    filename = generate_code_barr(producto.get_codigo())

    code_bar.set_filename(filename)
    code_bar.set_filename_final(_file_codigo_barra_final)

    _labetl_img = code_bar.get_label()

    img = cv2.imread(filename) # type: ignore
    font = cv2.FONT_HERSHEY_SIMPLEX # type: ignore
    colorLetra = (0, 0, 0)

    lista_texto = code_bar.get_textos()
    for text in lista_texto:
        cv2.putText(img, text.texto, (text.x, text.y), font, text.tamanio, colorLetra, text.grosor) # type: ignore
    cv2.imwrite(filename, img) # type: ignore

    nueva_imagen = tk.PhotoImage(file=filename)
    photoimage = nueva_imagen.subsample(1, 2)

    _labetl_img.config(image=photoimage)

    _labetl_img.image = photoimage # type: ignore
    

    pass


def generate_code_barr(_codigo_barra):

    fullname = _file_codigo_barra

    if len(_codigo_barra) > 13:
        # barcode_image = code128.image(_codigo_barra, height=100)

        EAN = barcode.get_barcode_class('ean13')

        # Define el número para el código de barras (debe tener 12 dígitos para EAN-13)
        number = _codigo_barra

        # Crea el código de barras
        ean = EAN(number, writer=ImageWriter())


        options = { "module_width": 0.5,
                   "module_height": 15.0,
                   "font_size": 10,
                   "text_distance": 2.0,
                   "background": "white",
                   "foreground": "black",
        }
        barcode_image = ean.save('custom_barcode', options)

        # Guarda la imagen del código de barras
        # barcode_image = ean.save('barcode')
    else:
  
        barcode_image = code128.image(_codigo_barra, height=100)

    top_bott_margin = 30
    l_r_margin = 60
    new_height = barcode_image.height + (2 * top_bott_margin)
    new_width = barcode_image.width + (2 * l_r_margin)
    new_image = Image.new( 'RGB', (new_width, new_height), (255, 255, 255)) # type: ignore

    # put barcode on new image
    barcode_y = 50
    barcode_x = 50
    new_image.paste(barcode_image, (barcode_x, barcode_y))

    new_image.save(fullname, 'PNG')

    new_image_aux = Image.new( 'RGB', (new_width, new_height), (255, 255, 255)) # type: ignore
    new_image_aux.save(_file_block, 'PNG')

    new_image_aux2 = Image.new( 'RGB', (new_width, new_height), (255, 255, 255)) # type: ignore
    new_image_aux2.save(_file_block_header, 'PNG')


    imagen1 = cv2.imread(_file_block) # type: ignore
    imagen0 = cv2.imread(_file_block_header) # type: ignore
    imagen2 = cv2.imread(fullname) # type: ignore

    concat_vertical = cv2.vconcat([imagen0, imagen2, imagen1]) # type: ignore

    cv2.imwrite(fullname, concat_vertical) # type: ignore
    return fullname

def generate_code_barr_print(_codigo_barra, barcode_x = 50 ):

    fullname = _file_codigo_barra
  
    if len(_codigo_barra) > 13:
        # barcode_image = code128.image(_codigo_barra, height=100)

        EAN = barcode.get_barcode_class('ean13')

        # Define el número para el código de barras (debe tener 12 dígitos para EAN-13)
        number = _codigo_barra

        # Crea el código de barras
        ean = EAN(number, writer=ImageWriter())

        # Guarda la imagen del código de barras
        barcode_image = ean.save('barcode')
    else:
  
        barcode_image = code128.image(_codigo_barra, height=100)

    top_bott_margin = 30
    l_r_margin = 60
    new_height = barcode_image.height + (2 * top_bott_margin)
    new_width = barcode_image.width + (2 * l_r_margin)
    new_image = Image.new( 'RGB', (new_width, new_height), (255, 255, 255)) # type: ignore

    # put barcode on new image
    barcode_y = 50
    # barcode_x = 50
    new_image.paste(barcode_image, (barcode_x, barcode_y))

    new_image.save(fullname, 'PNG')

    new_image_aux = Image.new( 'RGB', (new_width, new_height), (255, 255, 255)) # type: ignore
    new_image_aux.save(_file_block, 'PNG')

    new_image_aux2 = Image.new( 'RGB', (new_width, new_height), (255, 255, 255)) # type: ignore
    new_image_aux2.save(_file_block_header, 'PNG')


    imagen1 = cv2.imread(_file_block) # type: ignore
    imagen0 = cv2.imread(_file_block_header) # type: ignore
    imagen2 = cv2.imread(fullname) # type: ignore

    concat_vertical = cv2.vconcat([imagen0, imagen2, imagen1]) # type: ignore

    cv2.imwrite(fullname, concat_vertical) # type: ignore

    _labetl_img = code_bar.get_label()

    img = cv2.imread(fullname) # type: ignore
    font = cv2.FONT_HERSHEY_SIMPLEX # type: ignore
    colorLetra = (0, 0, 0)

    lista_texto = code_bar.get_textos()
    for text in lista_texto:
        cv2.putText(img, text.texto, (text.x, text.y), font, text.tamanio, colorLetra, text.grosor) # type: ignore
    cv2.imwrite(fullname, img) # type: ignore

    nueva_imagen = tk.PhotoImage(file=fullname)
    photoimage = nueva_imagen.subsample(1, 2)

    _labetl_img.config(image=photoimage)

    _labetl_img.image = photoimage # type: ignore

    return fullname

def calculo_producto_posicion(event):

    textos = code_bar.get_textos()
    if textos:

        dict_producto = meta.get_diccionario_producto()
        dict_precio   = meta.get_diccionario_precio()
        dict_codigo   = meta.get_diccionario_codigo_barra()

        producto = textos[0]
        precio   = textos[1]
        codigo   = textos[2]

        producto.set_texto(dict_producto['nombre'].get())
        producto.set_tamanio(int(dict_producto['tamanio'].get()))
        producto.set_grosor(int(dict_producto['grosor'].get()))

        producto.set_x(int(dict_producto['x'].get()))
        producto.set_y(int(dict_producto['y'].get()))


        precio.set_tamanio(int(dict_precio['tamanio'].get()))
        precio.set_grosor(int(dict_precio['grosor'].get()))
        precio.set_x(int(dict_precio['x'].get()))
        precio.set_y(int(dict_precio['y'].get()))

        codigo.set_tamanio(int(dict_codigo['tamanio'].get()))
        codigo.set_grosor(int(dict_codigo['grosor'].get()))

        codigo.set_x(int(dict_codigo['x'].get()))
        codigo.set_y(int(dict_codigo['y'].get()))

        json = meta.get_posicionamiento()

        json['producto']['tamanio'] = int(dict_producto['tamanio'].get())
        json['producto']['grosor'] = int(dict_producto['grosor'].get())
        json['producto']['x'] = int(dict_producto['x'].get())
        json['producto']['y'] = int(dict_producto['y'].get())

        json['precio']['tamanio'] = int(dict_precio['tamanio'].get())
        json['precio']['grosor'] = int(dict_precio['grosor'].get())
        json['precio']['x'] = int(dict_precio['x'].get())
        json['precio']['y'] = int(dict_precio['y'].get())


        json['codigo']['tamanio'] = int(dict_codigo['tamanio'].get())
        json['codigo']['grosor'] = int(dict_codigo['grosor'].get())
        json['codigo']['x'] = int(dict_codigo['x'].get())
        json['codigo']['y'] = int(dict_codigo['y'].get())


        meta.set_posicionamiento(json)

        render_img()

    pass


def calcular_img_impresion(dict_preparar):
    render_img()
    _labetl_img_final = code_bar.get_label_final()

    _cantidad = int(dict_preparar['copia_h'].get())


    _alto_mm = 75
    _ancho_mm = 150

    _alto_mm = calcular_mm_to_px(_alto_mm)
    _ancho_mm = calcular_mm_to_px(_ancho_mm)

    if _cantidad > 3:
        messagebox.showinfo(message="Cantidad no puede ser mayor a 3 por ahora", title="Alerta!")
        #insert_data_entry(dict_preparar['copia_h'], 1)
        return

    filename_final = code_bar.get_filename_final()
    filename = code_bar.get_filename()

    # image = Image.open(filename)
    # new_image = image.resize((_ancho_mm, _alto_mm))
    # new_image.save(filename)

    # imagen1 = cv2.imread(filename) # type: ignore
    array_img = []

    # for x in range(_cantidad):
    #     array_img.append(imagen1)

    _codigo_barra = code_bar.get_codigo()
    barcode_x = 70
    for x in range(_cantidad):
        file_name_aux = generate_code_barr_print(_codigo_barra, barcode_x)
        # barcode_x = barcode_x -25

        imagen_aux = cv2.imread(file_name_aux) # type: ignore
        array_img.append(imagen_aux)
        pass

    concat_vertical = cv2.hconcat(array_img) # type: ignore
    cv2.imwrite(filename_final, concat_vertical) # type: ignore

    imagen1 = cv2.imread(filename_final) # type: ignore
    array_img = []
    for x in range(3):
        array_img.append(imagen1)

    concat_vertical = cv2.vconcat(array_img) # type: ignore
    cv2.imwrite(filename_final, concat_vertical) # type: ignore

    cv2.waitKey(0) # type: ignore
    cv2.destroyAllWindows() # type: ignore

    nueva_imagen_final = tk.PhotoImage(file=filename_final)
    photoimage_final = nueva_imagen_final.subsample(4, 4)

    _labetl_img_final.config(image=photoimage_final)

    _labetl_img_final.image = photoimage_final # type: ignore

    pass


def insert_data_entry(_entry, _value):
    _entry.delete(0, tk.END)
    _entry.insert(0, _value)
def insert_range_data_entry(_entry, _value):
    _entry.set(_value)
    pass
def insert_combobox_data_entry(_entry, _value):
    _entry.current(_value)
    pass
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

def calcular_mm_to_px(mm):
    return int(MM_PX * mm)


def formato_numero(_valor):
    return '{:,.0f}'.format(_valor).replace(",", "@").replace(".", ",").replace("@", ".")

def imprimir_etiquetas(dict_preparar):

    _cantidad = int(dict_preparar['cantidad'].get())
    _impresora = dict_preparar['impresora'].get()
    
    if 'PDF' in _impresora:
        _cantidad = 1
    
    for x in range(_cantidad):
        try:    
            PHYSICALWIDTH = 110
            PHYSICALHEIGHT = 111

            #printer_name = win32print.GetDefaultPrinter()
            printer_name = _impresora


        
            file_name = code_bar.get_filename_final()

            hDC = win32ui.CreateDC ()
            hDC.CreatePrinterDC (printer_name) # type: ignore
            printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT) # type: ignore

            bmp = Image.open (file_name)

            hDC.StartDoc (file_name) # type: ignore
            hDC.StartPage () # type: ignore

            dib = ImageWin.Dib (bmp)
            dib.draw (hDC.GetHandleOutput (), (0,0,printer_size[0],printer_size[1])) # type: ignore

            hDC.EndPage () # type: ignore
            hDC.EndDoc () # type: ignore
            hDC.DeleteDC () # type: ignore
            time.sleep(300/1000)
            pass
        except Exception:
            break
    pass


def get_data_defecto_posicionamiento():
    data = None
    with open(_file_json, 'r') as archivo:
        data = json.load(archivo)
        meta.set_posicionamiento(data)
    return data

# Creamos una instancia de la clase Tk
root = tk.Tk()

root.resizable(0,0) # type: ignore

wtotal = root.winfo_screenwidth()
htotal = root.winfo_screenheight()
#  Guardamos el largo y alto de la ventana
wventana = 320
hventana = 350

#  Aplicamos la siguiente formula para calcular donde debería posicionarse
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)

#  Se lo aplicamos a la geometría de la ventana
root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

root.title(TITULO)

icono = tk.PhotoImage(file=_file_favicon)
root.iconphoto(True, icono)



generar_view_login()
# Iniciamos el loop de la ventana
root.mainloop()
