from PIL import Image
im = Image.open("images/logo.png")
# print attributes
print(im.size, im.format, im.mode)
im.show()
from PIL import ImageFilter
original = Image.open("images/Napoli.jpeg")
blured = original.filter(ImageFilter.BLUR)
original.show()
blured.show()
blured.save("images/blured.jpeg")
