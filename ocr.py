import pytesseract
from pdf2image import convert_from_path
import tempfile
import os

# Tesseract path (correct for your system)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Poppler path (fixed)
POPPLER_PATH = r"C:\poppler\Library\bin"


def extract_text(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.file.read())
        tmp_path = tmp.name

    pages = convert_from_path(tmp_path, poppler_path=POPPLER_PATH)

    text = ""
    for page in pages:
        text += pytesseract.image_to_string(page)

    os.remove(tmp_path)
    return text
