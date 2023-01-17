from PIL import Image, ImageDraw
from math import cos,sin,pi
import math,random
from pathlib import Path
max_resolution_x=3840
max_resolution_y=2160
image = Image.new("RGB", (max_resolution_x,max_resolution_y),(55,54,54))
draw = ImageDraw.Draw(image)
#draw.rectangle((0,0,900,900), fill="white", outline="white")

def to_radan(x):
    return x*pi/180.0

# count = 0
# while count <100:
#
#     j=1
#     alpha=45
#     x=(max_resolution_x-count*20)*sin(to_radan(alpha))
#     y=(max_resolution_y-count*20)*cos(to_radan(alpha))
#     # print(str(x)+'\n'+str(y))
#     pointx1=max_resolution_x*0.01
#     pointy1=max_resolution_y*0.01+10*(count+3)
#     pointx2=(max_resolution_x*0.99)
#     pointy2=(max_resolution_y*0.01+50*(count+3))*cos(to_radan(alpha))
#     print(str(pointx1)+"  "+ str(pointx2)+"  "+ str(pointx2)+"  "+str(pointy2))
#     draw.line(((pointx1, pointy1), (pointx2, pointy2)), fill=(10*count,255,255-count), width=3)
#     # while j <6:
#     #      rombx=(max_resolution_x-count*20)*cos(to_radan(alpha))
#     #      romby=(max_resolution_y-count*20)*sin(to_radan(alpha))
#     #      draw.line(((max_resolution_x*0.1 - x, max_resolution_y*0.1 - y), (400 - rombx, 400 - romby)), fill=(30+10*count,255,255-20*count), width=3)
#     #      j+=1
#     #      alpha+=90
#     #      x=rombx
#     #      y=romby
#     count+=1
newcount = 0
while (newcount < max_resolution_x*0.98):#or(newcount < max_resolution_y*0.98):
    pointx = max_resolution_x * 0.01 + newcount
    pointy = max_resolution_y * 0.01 + newcount
    draw.line(((pointx, 10*sin(pointx)+100), (pointx, 10*sin(pointx)+1000)), fill=(random.randint(100, 200), random.randint(50, 200), 255), width=3)
    # pointx = max_resolution_x * 0.01+newcount
    # pointy = max_resolution_y * 0.01 + newcount*0.2
    # print(pointx, pointy)
    # draw.line(((pointx, pointy), (pointx, pointy+pointy)), fill=(10,random.randint(50,200),255), width=3)
    # pointx1 = max_resolution_x * 0.01 + newcount
    # pointy1 = max_resolution_y * 0.01 + newcount * 0.2+pointy
    # draw.line(((pointx1, (pointy1+20)), (pointx1, pointy1 + pointy1*0.5)), fill=(random.randint(50, 200), random.randint(50, 200), 255), width=3)
    newcount += 15

del draw

# home_dir = (str(Path.home())+'/picture.png')
home_dir='d:\\tmp\\tmp\\picture1.png'
image.save(home_dir, "PNG")
print(home_dir)
