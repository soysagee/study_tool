import pytesseract
from PIL import Image
import logging

# Configura el path a Tesseract si es necesario (solo en Windows)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path, lang='eng'):
    """
    Extrae texto de una imagen utilizando OCR (Tesseract).

    Args:
        image_path (str): Ruta del archivo de imagen.
        lang (str): Idioma para el OCR (por defecto, inglés: 'eng').

    Returns:
        str: Texto extraído de la imagen, o un mensaje de error si falla.
    """
    try:
        # Abre la imagen utilizando PIL
        with Image.open(image_path) as img:
            # Extrae texto utilizando Tesseract OCR
            text = pytesseract.image_to_string(img, lang=lang)
            return text

    except FileNotFoundError:
        logging.error(f"El archivo de imagen no se encontró: {image_path}")
        return f"Error: El archivo de imagen no se encontró en {image_path}."
    except Exception as e:
        logging.error(f"Error al procesar la imagen {image_path}: {e}")
        return f"Error al procesar la imagen: {e}"

# Ejemplo de uso
if __name__ == "__main__":
    image_path = "data/sample_image.png"  # Ruta de ejemplo
    extracted_text = extract_text_from_image(image_path, lang='spa')  # Idioma español
    print("Texto extraído de la imagen:")
    print(extracted_text)