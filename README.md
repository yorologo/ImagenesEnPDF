# Documentación del Proyecto: **ImagenesEnPDF**

## Descripción

**ImagenesEnPDF** es un proyecto que redimensiona una imagen y genera un archivo PDF con la imagen redimensionada colocada por defecto en un diseño de cuadrícula en una página de tamaño Doble Carta (27.9 cm x 43.2 cm). El usuario puede especificar el tamaño de la imagen, el margen de la página y el espacio mínimo entre las imágenes.

## Requisitos

- **Pillow**: Para manipular imágenes.
- **FPDF**: Para crear y manejar archivos PDF.

## Instalación de Dependencias

Para instalar las dependencias necesarias, ejecute:

```bash
pip install pillow fpdf
```

## Variables de Configuración

- `original_image_path`: Ruta del archivo de imagen original (cadena de texto).
- `resized_image_path`: Ruta del archivo de imagen redimensionada (cadena de texto).
- `image_size_cm`: Tamaño de la imagen redimensionada en centímetros (número).
- `min_spacing_cm`: Espacio mínimo entre imágenes en centímetros (número).
- `output_pdf_path`: Ruta del archivo PDF de salida (cadena de texto).
- `page_width_cm`: Ancho de la página en centímetros (número) - Tamaño Doble Carta.
- `page_height_cm`: Alto de la página en centímetros (número) - Tamaño Doble Carta.
- `page_margin_cm`: Margen de la página en centímetros (número).

## Funciones

### `resize_image(original_image_path, resized_image_path, size_cm)`

Redimensiona la imagen original a un tamaño especificado en centímetros y guarda la imagen redimensionada.

**Parámetros:**
- `original_image_path` (str): Ruta de la imagen original.
- `resized_image_path` (str): Ruta para guardar la imagen redimensionada.
- `size_cm` (float): Tamaño deseado de la imagen en centímetros.

**Descripción:**
1. Convierte el tamaño de centímetros a pulgadas.
2. Calcula el tamaño en píxeles basado en una resolución de 300 DPI.
3. Redimensiona y guarda la imagen.

### `create_pdf_with_images(output_pdf_path, image_path, image_size_cm, page_margin_cm, page_height_cm, page_width_cm, min_spacing_cm)`

Crea un archivo PDF con la imagen redimensionada colocada en una cuadrícula en la página especificada.

**Parámetros:**
- `output_pdf_path` (str): Ruta del archivo PDF de salida.
- `image_path` (str): Ruta de la imagen que se va a insertar en el PDF.
- `image_size_cm` (float): Tamaño de la imagen en centímetros.
- `page_margin_cm` (float): Margen de la página en centímetros.
- `page_height_cm` (float): Altura de la página en centímetros.
- `page_width_cm` (float): Ancho de la página en centímetros.
- `min_spacing_cm` (float): Espacio mínimo entre imágenes en centímetros.

**Descripción:**
1. Calcula el número de imágenes que caben horizontal y verticalmente en la página.
2. Calcula el espacio entre las imágenes.
3. Inserta la imagen en la página del PDF en una cuadrícula.
4. Guarda el PDF en el archivo especificado.

### `main()`

Función principal que coordina la redimensión de la imagen y la creación del PDF.

**Descripción:**
1. Llama a `resize_image` para redimensionar la imagen original.
2. Llama a `create_pdf_with_images` para crear el archivo PDF con la imagen redimensionada.

## Ejecución del Script

Para ejecutar el script, simplemente corre el archivo en el entorno Python. Asegúrate de que las rutas de los archivos y los parámetros estén configurados según tus necesidades.

```bash
python nombre_del_script.py
```

Donde `nombre_del_script.py` es el nombre del archivo que contiene el código proporcionado.

## Manejo de Errores

- Si la imagen es demasiado grande para caber en la página con los márgenes y el espacio especificado, se lanzará un `ValueError`.

## Ejemplo de Uso

```python
original_image_path = "imagen_original.png"
resized_image_path = "imagen_redimensionada.png"
image_size_cm = 0.5
min_spacing_cm = 0
output_pdf_path = "output.pdf"
page_width_cm = 27.9
page_height_cm = 43.2
page_margin_cm = 1

main()
```

Este ejemplo redimensionará `imagen_original.png` a 0.5 cm y creará un PDF llamado `output.pdf` con la imagen colocada en una cuadrícula en una página de tamaño Doble Carta.
