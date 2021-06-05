import tesserocr
from PIL import Image

image = Image.open('demo.jpg')
print(tesserocr.image_to_text(image))
