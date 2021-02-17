import tesserocr
import pytesseract
from PIL import Image
image = Image.open('3.jpg')
print(tesserocr.image_to_text(image))
