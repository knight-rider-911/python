from PIL import Image, ImageDraw
from math import cos,sin,pi
image = Image.new("RGB", (900,900),(55,54,54))
draw = ImageDraw.Draw(image)
#draw.rectangle((0,0,900,900), fill="white", outline="white")

def to_radan(x):
    return x*pi/180.0

count = 5
while count <11:


    draw.ellipse((450-count*10, 450-count*10, 500+count*10, 500+count*10),  outline="red")
    count+=1



del draw
image.save("d:\\test.png", "PNG")

