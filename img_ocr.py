import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = Image.open(r"C:\Users\Hima Bindu\OneDrive\Desktop\ocr\loan-agreement-image.jpg")

extracted_text = pytesseract.image_to_string(image)

with open("output_text.txt", "w", encoding="utf-8") as file:
    file.write(extracted_text)

print("Text extracted and saved successfully!!!")
