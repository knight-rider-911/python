from PIL import Image, ImageDraw
from math import cos,sin,pi
image = Image.new("RGB", (900,900),(55,54,54))
draw = ImageDraw.Draw(image)
#draw.rectangle((0,0,900,900), fill="white", outline="white")

def to_radan(x):
    return x*pi/180.0

count = 200
while count >1:
	draw.ellipse((250-count, 255-count, 255+count, 250+count), \
		fill=(255-count,0+count,255-count), \
		outline=(255-count,0+count,255-count))
	count-=1
del draw
image.save("/home/eagle/est.png", "PNG")

