# Generador de PDF con Cuadrícula de Imágenes

## Descripción

Este script permite redimensionar una imagen manteniendo su proporción original y generar un archivo PDF que contiene una cuadrícula de esta imagen repetida. Puedes especificar las dimensiones deseadas de la imagen (ancho o altura), los márgenes, el espaciado entre imágenes y las dimensiones de la página del PDF. Es especialmente útil para crear hojas con múltiples imágenes distribuidas uniformemente.

---

## Requisitos

- **Python 3.x**
- **Pillow**: Biblioteca para manipulación de imágenes.
- **FPDF**: Biblioteca para generar archivos PDF.

### Instalación de Dependencias

Ejecuta los siguientes comandos para instalar las dependencias necesarias:

```bash
pip install pillow fpdf
```

---

## Uso

El script se ejecuta desde la línea de comandos y acepta varios argumentos que permiten personalizar su funcionamiento.

### Ejecución Básica

```bash
python script.py -i <ruta_imagen>
```

### Argumentos Disponibles

- `-i`, `--input_image` **(obligatorio)**: Ruta de la imagen original que deseas redimensionar e insertar en el PDF.
- `-o`, `--output_pdf`: Nombre o ruta del archivo PDF de salida. Por defecto es `output.pdf`.
- `-w`, `--width`: Ancho deseado de la imagen en centímetros.
- `-he`, `--height`: Altura deseada de la imagen en centímetros.
- `-sp`, `--spacing`: Espacio mínimo entre imágenes en centímetros. Por defecto es `1.0` cm.
- `-pw`, `--page_width`: Ancho de la página del PDF en centímetros. Por defecto es `27.9` cm.
- `-ph`, `--page_height`: Altura de la página del PDF en centímetros. Por defecto es `43.2` cm.
- `-m`, `--margin`: Tamaño de los márgenes de la página en centímetros. Por defecto es `1.0` cm.

### Notas sobre los Argumentos

- **Dimensiones de la Imagen**:
  - Si solo especificas el ancho (`--width`), la altura se calculará automáticamente para mantener la proporción original.
  - Si solo especificas la altura (`--height`), el ancho se calculará proporcionalmente.
  - Si especificas tanto el ancho como la altura, la imagen se redimensionará exactamente a esas dimensiones (esto puede distorsionar la imagen si las proporciones no coinciden).
  - Si no especificas ni el ancho ni la altura, la imagen conservará su tamaño original.

---

## Ejemplos de Uso

### 1. Redimensionar una imagen especificando solo el ancho

```bash
python script.py -i imagen_original.jpg -w 5
```

- Redimensiona `imagen_original.jpg` para que tenga un ancho de **5 cm**.
- La altura se ajustará proporcionalmente.
- Genera un PDF `output.pdf` con una cuadrícula de la imagen.

### 2. Redimensionar una imagen especificando solo la altura

```bash
python script.py -i imagen_original.jpg --height 7
```

- Redimensiona la imagen para que tenga una altura de **7 cm**.
- El ancho se ajustará proporcionalmente.

### 3. Especificar ancho y altura exactos

```bash
python script.py -i imagen_original.jpg -w 5 --height 7
```

- Redimensiona la imagen a un ancho de **5 cm** y una altura de **7 cm**.
- Esto puede distorsionar la imagen si las proporciones no coinciden con las originales.

### 4. Generar un PDF con espaciado personalizado y dimensiones de página específicas

```bash
python script.py -i imagen_original.jpg -o mi_pdf.pdf -w 6 --spacing 2 -pw 21.59 -ph 27.94 -m 2
```

- Genera un PDF llamado `mi_pdf.pdf`.
- Redimensiona la imagen a un ancho de **6 cm**.
- Establece un espaciado mínimo entre imágenes de **2 cm**.
- Configura el tamaño de página a **21.59 cm x 27.94 cm** (tamaño carta).
- Establece márgenes de **2 cm**.

---

## Funcionalidades del Script

### 1. Redimensionamiento de Imágenes

La función `resize_image` se encarga de redimensionar la imagen original según los parámetros proporcionados:

- **Mantiene la proporción**: Al especificar solo una dimensión (ancho o altura), calcula la otra manteniendo la relación de aspecto original.
- **Redimensionamiento exacto**: Si se proporcionan ambas dimensiones, ajusta la imagen a esas medidas específicas (puede distorsionar la imagen).
- **Sin cambios**: Si no se proporcionan dimensiones, la imagen conserva su tamaño original.

### 2. Generación del PDF con Cuadrícula de Imágenes

La función `create_pdf_with_images` crea un PDF que contiene una cuadrícula de la imagen redimensionada:

- **Distribución Automática**: Calcula cuántas imágenes caben horizontal y verticalmente en la página, considerando los márgenes y el espaciado mínimo.
- **Espaciado Uniforme**: Ajusta el espacio entre las imágenes para distribuirlas uniformemente en la página.
- **Centrado**: Centra la cuadrícula de imágenes en la página.
- **Márgenes Personalizables**: Permite especificar márgenes personalizados alrededor de la página.

---

## Explicación de las Funciones

### `parse_arguments()`

- **Descripción**: Maneja y procesa los argumentos proporcionados en la línea de comandos utilizando la biblioteca `argparse`.
- **Retorna**: Un objeto con todos los argumentos y sus valores.

### `resize_image(original_image_path, resized_image_path, width_cm=None, height_cm=None)`

- **Descripción**: Redimensiona la imagen original según las dimensiones especificadas.
- **Parámetros**:
  - `original_image_path`: Ruta de la imagen original.
  - `resized_image_path`: Ruta donde se guardará la imagen redimensionada.
  - `width_cm`: Ancho deseado en centímetros.
  - `height_cm`: Altura deseada en centímetros.
- **Retorna**: Las dimensiones finales de la imagen en centímetros (ancho y altura).

### `create_pdf_with_images(output_pdf_path, image_path, image_width_cm, image_height_cm, page_margin_cm, page_height_cm, page_width_cm, min_spacing_cm)`

- **Descripción**: Crea el PDF con la cuadrícula de imágenes.
- **Parámetros**:
  - `output_pdf_path`: Ruta y nombre del archivo PDF de salida.
  - `image_path`: Ruta de la imagen redimensionada.
  - `image_width_cm`: Ancho de la imagen en centímetros.
  - `image_height_cm`: Altura de la imagen en centímetros.
  - `page_margin_cm`: Tamaño de los márgenes de la página en centímetros.
  - `page_height_cm`: Altura de la página en centímetros.
  - `page_width_cm`: Ancho de la página en centímetros.
  - `min_spacing_cm`: Espacio mínimo entre las imágenes en centímetros.

### `main()`

- **Descripción**: Función principal que coordina el proceso.
- **Pasos**:
  1. Procesa los argumentos de la línea de comandos.
  2. Redimensiona la imagen utilizando `resize_image`.
  3. Genera el PDF con la cuadrícula de imágenes utilizando `create_pdf_with_images`.

---

## Detalles Técnicos

- **Relación de Aspecto**: El script calcula y mantiene la relación de aspecto original de la imagen al redimensionar, a menos que se especifiquen ambas dimensiones.
- **Resolución**: Se utiliza una resolución de **300 DPI** para asegurar una calidad adecuada para impresión.
- **Unidades**: Todas las dimensiones se manejan en centímetros, facilitando la configuración y comprensión.
- **Manejo de Errores**: Si la imagen es demasiado grande para caber en la página con los márgenes y espaciado especificados, el script lanza un `ValueError` con un mensaje descriptivo.

---

## Notas Importantes

- **Imagen Temporal**: El script genera una imagen temporal redimensionada llamada `temp_resized_image.png`. Si deseas eliminarla después de generar el PDF, puedes modificar el script para que lo haga automáticamente.
- **Distorsión de la Imagen**: Si especificas tanto el ancho como la altura y estas dimensiones no mantienen la proporción original, la imagen resultante estará distorsionada.
- **Espaciado Real**: El script intentará ajustar el espaciado entre imágenes para que las imágenes se distribuyan uniformemente en la página, pudiendo ser mayor que el espaciado mínimo si hay espacio adicional.
- **Orientación de la Página**: La orientación predeterminada es vertical (`'P'` para "Portrait"). Si deseas cambiarla a horizontal, puedes modificar el parámetro en la creación del objeto `FPDF`.

---

## Posibles Mejoras

- **Soporte para Múltiples Imágenes**: Actualmente, el script trabaja con una sola imagen repetida en la cuadrícula. Se podría ampliar para soportar una lista de imágenes diferentes.
- **Opciones de Calidad**: Permitir al usuario especificar la calidad o el formato de la imagen redimensionada.
- **Interfaz Gráfica**: Implementar una interfaz gráfica para facilitar el uso a usuarios no familiarizados con la línea de comandos.

---

## Conclusión

Este script es una herramienta versátil para generar PDFs con cuadrículas de imágenes redimensionadas manteniendo la proporción original. Su configuración flexible a través de argumentos de línea de comandos lo hace adaptable a diversas necesidades, ya sea para impresión de fotografías, creación de etiquetas, tarjetas u otros materiales gráficos.
