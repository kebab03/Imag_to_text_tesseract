from PIL import Image
import pytesseract

# Assicurati che Tesseract sia installato e configurato correttamente
# Su alcuni sistemi, potrebbe essere necessario specificare il percorso di Tesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def estrai_testo_da_immagine(percorso_immagine):
    # Apri l'immagine
    immagine = Image.open(percorso_immagine)
    
    # Usa pytesseract per estrarre il testo
    testo = pytesseract.image_to_string(immagine, lang='ita')
    
    return testo

# Esempio di utilizzo
percorso_immagine = 'img.png'
testo_estratto = estrai_testo_da_immagine(percorso_immagine)

print("Testo estratto dall'immagine:")
print(testo_estratto)