import pytesseract as tess

from PIL import Image

tess.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
img = Image.open('wineMenu1.png')
text = tess.image_to_string(img)

print(text)
