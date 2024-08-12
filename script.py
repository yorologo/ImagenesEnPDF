from PIL import Image
from fpdf import FPDF

# Imagen
original_image_path = "imagen_original.png"
resized_image_path = "imagen_redimensionada.png"
image_size_cm = 0.5
min_spacing_cm = 0  # Espacio mínimo entre imágenes

# PDF
output_pdf_path = "output.pdf"
page_width_cm = 27.9  # Tamaño Doble Carta en cm (ancho)
page_height_cm = 43.2 # Tamaño Doble Carta en cm (alto)
page_margin_cm = 1

def resize_image(original_image_path, resized_image_path, size_cm):
    size_inch = size_cm / 2.54
    img = Image.open(original_image_path)
    dpi = 300
    size_px = (int(size_inch * dpi), int(size_inch * dpi))
    img = img.resize(size_px, Image.LANCZOS)
    img.save(resized_image_path)

def create_pdf_with_images(output_pdf_path, image_path, image_size_cm, page_margin_cm, page_height_cm, page_width_cm, min_spacing_cm):
    pdf = FPDF('L', 'cm', (page_height_cm, page_width_cm))
    pdf.add_page()

    image_width_cm, image_height_cm = image_size_cm, image_size_cm

    num_images_x = int((page_width_cm - 2 * page_margin_cm + min_spacing_cm) / (image_width_cm + min_spacing_cm))
    num_images_y = int((page_height_cm - 2 * page_margin_cm + min_spacing_cm) / (image_height_cm + min_spacing_cm))

    if num_images_x == 0 or num_images_y == 0:
        raise ValueError("Image size too large to fit on the page with the specified margins.")

    total_image_width_cm = num_images_x * image_width_cm
    total_image_height_cm = num_images_y * image_height_cm

    spacing_x = (page_width_cm - 2 * page_margin_cm - total_image_width_cm) / (num_images_x - 1) if num_images_x > 1 else 0
    spacing_y = (page_height_cm - 2 * page_margin_cm - total_image_height_cm) / (num_images_y - 1) if num_images_y > 1 else 0

    if spacing_x < min_spacing_cm:
        spacing_x = min_spacing_cm
    if spacing_y < min_spacing_cm:
        spacing_y = min_spacing_cm

    x_start = page_margin_cm
    y_start = page_margin_cm

    for row in range(num_images_y):
        y = y_start + row * (image_height_cm + spacing_y)
        for col in range(num_images_x):
            x = x_start + col * (image_width_cm + spacing_x)
            pdf.image(image_path, x, y, image_width_cm, image_height_cm)

    pdf.output(output_pdf_path, "F")

def main():
    # Redimensionar la imagen
    resize_image(original_image_path, resized_image_path, image_size_cm)

    # Crear el PDF con la imagen redimensionada
    create_pdf_with_images(output_pdf_path, resized_image_path, image_size_cm, page_margin_cm, page_height_cm, page_width_cm, min_spacing_cm)

if __name__ == "__main__":
    main()
