import fitz  # PyMuPDF
import logging

def extract_text_from_pdf(pdf_path):
    """
    Extrae texto de un archivo PDF.

    Args:
        pdf_path (str): Ruta del archivo PDF.

    Returns:
        dict: Un diccionario con el texto extraído por página.
    """
    try:
        pdf_document = fitz.open(pdf_path)
        extracted_text = {}

        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            extracted_text[page_num + 1] = page.get_text()

        pdf_document.close()
        return extracted_text

    except Exception as e:
        logging.error(f"Error al procesar el PDF {pdf_path}: {e}")
        return {}