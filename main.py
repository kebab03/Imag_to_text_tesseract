import pytesseract
from PIL import Image

def extract_text(img_path):
    try:
        img = Image.open(img_path)
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(img, lang='ita', config=custom_config)
        return text
    except Exception as e:
        print(f"Errore durante l'estrazione del testo: {e}")
        return None

img_path = 'C:\\Users\\Sharif\\Pictures\\tesseract\\myp.png'
extracted_text = extract_text(img_path)

if extracted_text:
    print(extracted_text)
else:
    print("Non è stato possibile estrarre il testo.")