from PIL import Image, ImageFilter,ImageDraw
im = Image.open("images/ball.jpg")
im_rotated = im.rotate(90)
im_rotated.show()