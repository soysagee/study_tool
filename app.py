import sys
print("Rutas en sys.path:")
print("\n".join(sys.path))
from modules.pdf_reader import extract_text_from_pdf
from modules.ocr_module import extract_text_from_image

def main():
    print("Bienvenido a tu herramienta de estudio científico.")

    # Prueba 1: Extraer texto de un PDF
    pdf_path = "data/sample.pdf"
    pdf_text = extract_text_from_pdf(pdf_path)
    if pdf_text:
        print("Texto extraído del PDF:")
        for page, content in pdf_text.items():
            print(f"\nPágina {page}:\n{content}")
    else:
        print("No se pudo extraer texto del PDF.")

    # Prueba 2: Extraer texto de una imagen
    image_path = "data/sample_image.png"
    image_text = extract_text_from_image(image_path, lang='spa')  # Idioma español
    print("\nTexto extraído de la imagen:")
    print(image_text)

if __name__ == "__main__":
    main()