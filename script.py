import argparse
from PIL import Image
from fpdf import FPDF

def parse_arguments():
    parser = argparse.ArgumentParser(description="Redimensionar imágenes y generar un PDF con una cuadrícula de imágenes.")
    parser.add_argument("-i", "--input_image", required=True, help="Ruta de la imagen original.")
    parser.add_argument("-o", "--output_pdf", default="output.pdf", help="Nombre del archivo PDF de salida (por defecto: output.pdf).")
    parser.add_argument("-w", "--width", type=float, help="Ancho deseado de la imagen en cm.")
    parser.add_argument("-he", "--height", type=float, help="Altura deseada de la imagen en cm.")
    parser.add_argument("-sp", "--spacing", type=float, default=1.0, help="Espacio mínimo entre imágenes en cm (por defecto: 1.0 cm).")
    parser.add_argument("-pw", "--page_width", type=float, default=27.9, help="Ancho de la página en cm (por defecto: 27.9 cm).")
    parser.add_argument("-ph", "--page_height", type=float, default=43.2, help="Altura de la página en cm (por defecto: 43.2 cm).")
    parser.add_argument("-m", "--margin", type=float, default=1.0, help="Márgenes de la página en cm (por defecto: 1.0 cm).")
    return parser.parse_args()

def resize_image(original_image_path, resized_image_path, width_cm=None, height_cm=None):
    dpi = 300
    img = Image.open(original_image_path)
    width_px, height_px = img.size
    aspect_ratio = width_px / height_px

    if width_cm and not height_cm:
        # Si solo se proporciona el ancho, calcular la altura proporcional
        width_inch = width_cm / 2.54
        width_px = int(width_inch * dpi)
        height_px = int(width_px / aspect_ratio)
    elif height_cm and not width_cm:
        # Si solo se proporciona la altura, calcular el ancho proporcional
        height_inch = height_cm / 2.54
        height_px = int(height_inch * dpi)
        width_px = int(height_px * aspect_ratio)
    elif width_cm and height_cm:
        # Si se proporcionan ambas dimensiones, ajustarlas directamente
        width_inch = width_cm / 2.54
        height_inch = height_cm / 2.54
        width_px = int(width_inch * dpi)
        height_px = int(height_inch * dpi)
    else:
        # Si no se proporcionan dimensiones, mantener el tamaño original
        width_px = width_px
        height_px = height_px

    img = img.resize((width_px, height_px), Image.LANCZOS)
    img.save(resized_image_path)

    # Convertir dimensiones redimensionadas a cm
    final_width_cm = (width_px / dpi) * 2.54
    final_height_cm = (height_px / dpi) * 2.54

    return final_width_cm, final_height_cm

def create_pdf_with_images(output_pdf_path, image_path, image_width_cm, image_height_cm, page_margin_cm, page_height_cm, page_width_cm, min_spacing_cm):
    pdf = FPDF('P', 'cm', (page_width_cm, page_height_cm))
    pdf.set_margins(page_margin_cm, page_margin_cm, page_margin_cm)
    pdf.add_page()

    # Área utilizable en la página
    usable_width = page_width_cm - 2 * page_margin_cm
    usable_height = page_height_cm - 2 * page_margin_cm

    # Calcular el número de imágenes que caben horizontal y verticalmente
    n_cols = int((usable_width + min_spacing_cm) / (image_width_cm + min_spacing_cm))
    n_rows = int((usable_height + min_spacing_cm) / (image_height_cm + min_spacing_cm))

    if n_cols < 1 or n_rows < 1:
        raise ValueError("La imagen es demasiado grande para caber en la página con los márgenes y el espacio especificado.")

    # Calcular espacio real entre imágenes
    total_images_width = n_cols * image_width_cm
    total_spacing_x = usable_width - total_images_width
    spacing_x = total_spacing_x / (n_cols - 1) if n_cols > 1 else 0

    total_images_height = n_rows * image_height_cm
    total_spacing_y = usable_height - total_images_height
    spacing_y = total_spacing_y / (n_rows - 1) if n_rows > 1 else 0

    # Posición inicial para centrar las imágenes
    start_x = page_margin_cm + (usable_width - (n_cols * image_width_cm + (n_cols - 1) * spacing_x)) / 2
    start_y = page_margin_cm + (usable_height - (n_rows * image_height_cm + (n_rows - 1) * spacing_y)) / 2

    # Insertar imágenes en el PDF
    y = start_y
    for row in range(n_rows):
        x = start_x
        for col in range(n_cols):
            pdf.image(image_path, x, y, image_width_cm, image_height_cm)
            x += image_width_cm + spacing_x
        y += image_height_cm + spacing_y

    pdf.output(output_pdf_path, "F")
    print(f"PDF generado exitosamente en '{output_pdf_path}'.")

def main():
    args = parse_arguments()

    resized_image_path = "temp_resized_image.png"  # Imagen redimensionada temporal

    # Redimensionar la imagen
    image_width_cm, image_height_cm = resize_image(
        args.input_image, 
        resized_image_path, 
        width_cm=args.width, 
        height_cm=args.height
    )

    # Crear el PDF con las imágenes
    create_pdf_with_images(
        args.output_pdf,
        resized_image_path,
        image_width_cm,
        image_height_cm,
        args.margin,
        args.page_height,
        args.page_width,
        args.spacing
    )

if __name__ == "__main__":
    main()
