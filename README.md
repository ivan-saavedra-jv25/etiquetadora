
# 🏷️ Etiquetadora - OneCode

**OneCode** es una aplicación de escritorio desarrollada en Python que permite generar etiquetas con código de barras para productos obtenidos desde una API. Cuenta con una interfaz gráfica amigable (Tkinter), opciones de personalización del diseño y capacidad de impresión directa.

---

## 📌 Características principales

- 🔐 Inicio de sesión seguro con credenciales de empresa.
- 🔎 Búsqueda de productos mediante código de barra o código interno.
- 🧾 Visualización y edición del nombre del producto, precio y código de barra.
- 🖼️ Vista previa en tiempo real de la etiqueta.
- 🧩 Personalización de tamaño, grosor y posición del texto en la etiqueta.
- 🖨️ Envío directo a la impresora predeterminada o seleccionada.
- 🧵 Generación de etiquetas en tiras (copias en línea y columnas).

---

## 📁 Estructura del Proyecto

```
etiquetadora/
├── main.py
├── recursos/
│   ├── arial.ttf
│   ├── favicon.png
│   ├── logo-black.png
│   ├── fondo_logo.png
│   ├── configuracion.json
│   ├── codigo_barra.png
│   ├── codigo_barra_final.png
│   ├── block.png
│   └── block_header.png
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tu_usuario/etiquetadora.git
cd etiquetadora
```

2. (Opcional) Crea un entorno virtual:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecuta la aplicación:
```bash
python main.py
```

---

## 📦 Crear ejecutable (Windows)

Para generar un `.exe`:

```bash
pyinstaller --add-data "recursos;recursos" main.py -w --icon=recursos/favicon.ico
```

- `--add-data "recursos;recursos"`: Incluye la carpeta de recursos en el ejecutable.
- `-w`: Ejecuta la app sin consola.
- `--icon`: Asigna el ícono de la app.

El ejecutable se generará en la carpeta `dist/`.

---

## 🖨️ Requisitos del Sistema

- ✅ Windows (uso de `pywin32` para impresión).
- ✅ Python 3.8+
- ❌ No compatible con Linux/MacOS debido al uso de impresión nativa.

---

## 🧪 Credenciales de prueba (por defecto)

- Empresa: `77926573-0`  
> Puedes modificar esto en el código fuente si deseas cambiar el valor por defecto.

---

## 📬 Contacto

Desarrollado por **Iván Saavedra**  
📧 ivanandres.hj@gmail.com

---
