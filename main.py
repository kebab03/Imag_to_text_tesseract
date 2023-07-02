import pytesseract
from PIL import Image
import os

# Set the TESSDATA_PREFIX environment variable
os.environ['TESSDATA_PREFIX'] = r"C:\Tesseract-OCR\tessdata"

# Define the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract-OCR\tesseract.exe"
string = r"C:\Users\user\Pictures\Camera Roll"
# replace all instances of 'r' (old) with 'e' (new)
new_string = string.replace("\\", "/")
print("new_string:::-",new_string)
fil="2023-07-01 04_05_29-How to use ScreenManager and Screens with Kivy and KivyMD _ Python _ Kivy _ Kivy.png"
prin=new_string+"/"+fil
print("prin:-",prin)
# Open the image and store it in an image object
img = Image.open(prin)

# Extract text from the image
text = pytesseract.image_to_string(img)

# Display the extracted text
print(text)
