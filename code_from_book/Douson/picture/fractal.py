from PIL import Image, ImageDraw
from math import cos,sin,pi
from pathlib import Path
image = Image.new("RGB", (900,900),(55,54,54))
draw = ImageDraw.Draw(image)
#draw.rectangle((0,0,900,900), fill="white", outline="white")

def to_radan(x):
    return x*pi/180.0

count = 0
while count <11:

    j=1
    alpha=45
    x=(300-count*20)*sin(to_radan(alpha))
    y=(300-count*20)*cos(to_radan(alpha))
    while j <6:
         rombx=(300-count*20)*cos(to_radan(alpha))
         romby=(300-count*20)*sin(to_radan(alpha))
         draw.line(((400 - x, 400 - y), (400 - rombx, 400 - romby)), fill=(30+10*count,255,255-20*count), width=3)
         j+=1
         alpha+=90
         x=rombx
         y=romby
    count+=1

    i = 1
    alpha = 0
    x = (300 - count * 20) * sin(0)
    y = (300 - count * 20) * cos(0)
    while i < 6:
        rombx = (300 - count * 20) * cos(to_radan(alpha))
        romby = (300 - count * 20) * sin(to_radan(alpha))
        draw.line(((400 - x, 400 - y), (400 - rombx, 400 - romby)), fill=(255 - 20 * count, 20 + 20 * count, 180),
                  width=3)
        i += 1
        alpha += 90
        x = rombx
        y = romby


del draw

home_dir = (str(Path.home())+'/picture.png')
image.save(home_dir, "PNG")

