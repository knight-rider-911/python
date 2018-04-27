from PIL import Image, ImageDraw
from math import cos,sin,pi
image = Image.new("RGB", (450,450),(55,54,54))
draw = ImageDraw.Draw(image)
#draw.rectangle((0,0,900,900), fill="white", outline="white")

def to_radan(x):
    return x*pi/180.0

count = 200
while count >1:
	draw.rectangle((200-count, 200-count, 255+count, 250+count), \
		fill=(255-count,255-(count//2),255-(count//2)), \
		outline=(255-count,255-(count//2),255-(count//2)))
	count-=1
del draw
image.save("d:\est.png", "PNG")

