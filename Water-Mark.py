from PIL import Image, ImageFilter,ImageDraw
im = Image.open("images/ball.jpg")
logo = Image.open("images/logo.png")
cp = im.copy()
position = (im.width-logo.width, im.height-logo.height)
cp.paste( logo, position)
cp.show()