from PIL import Image
size=(256,256)
im = Image.open("images/Napoli.jpeg")
im.thumbnail(size)
im.show()
im.save("images/napoli.small.jpeg")
gray_scale = im.convert('L')
gray_scale.show()
