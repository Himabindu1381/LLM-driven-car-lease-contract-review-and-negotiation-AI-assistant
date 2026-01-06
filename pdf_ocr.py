import pytesseract
from pdf2image import convert_from_path

# Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Convert scanned PDF to images
pages = convert_from_path(
    r"C:\Users\Hima Bindu\OneDrive\Desktop\ocr\car-loan-bank-copy-agreement.pdf",
    poppler_path=r"C:\Users\Hima Bindu\Downloads\Release-25.12.0-0\poppler-25.12.0\Library\bin"
)

# OCR each page
text = ""
for page in pages:
    text += pytesseract.image_to_string(page)

# Save extracted text
with open("outputofpdf_text.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("PDF text extracted and saved successfully!")
