from PIL import Image, ImageDraw
import math
image = Image.new("RGBA", (900,900), (0,0,0,0))
draw = ImageDraw.Draw(image)
#draw.ellipse((10,10,30,300), fill="blue", outline="red")
draw.rectangle((0,0,1520,1520), fill="white", outline="white")
#draw.rectangle((30,30,180,180), outline="black")
"""step=10
while step<150:
    draw.rectangle(((160-step)*math.sin(45), (160-step)*math.cos(45),
                    (160+step), (160+step)), outline="red")
    step=step+10
draw.rectangle((300, 300, 320, 320), outline="black")
draw.line(((200, 200), (300,200)), fill="red", width=10)
draw.line(((300, 200), (300,300)), fill="red", width=10)
draw.line(((300, 300), (200,300)), fill="red", width=10)
draw.line(((200, 300), (200,200)), fill="red", width=10)

draw.line(((200, 200), (300*math.cos(45),200*math.cos(45))), fill="green", width=5)
draw.line(((300*math.cos(45), 200*math.cos(45)), (300*math.cos(45),300*math.cos(45))), fill="green", width=10)

draw.line(((150.5, 0), (150, 300)), fill=(255, 0, 0), width=20)"""
count = 0
while count <11:
    i=1
    alpha=0
    x=(300-count*20)*math.sin(0/math.pi)
    y=(300-count*20)*math.cos(0/math.pi)
    while i <6:
        rombx=(300-count*20)*math.cos((alpha*math.pi)/180)
        romby=(300-count*20)*math.sin((alpha*math.pi)/180)
        draw.line(((400 - x, 400 - y), (400 - rombx, 400 - romby)), fill="red", width=3)
        i=i+1
        alpha=alpha+90
        x=rombx
        y=romby

    j=1
    alpha=45
    x=(300-count*20)*math.sin((alpha*math.pi)/180)
    y=(300-count*20)*math.cos((alpha*math.pi)/180)
    while j <6:
         rombx=(300-count*20)*math.cos((alpha*math.pi)/180)
         romby=(300-count*20)*math.sin((alpha*math.pi)/180)
         draw.line(((400 - x, 400 - y), (400 - rombx, 400 - romby)), fill="red", width=3)
         j=j+1
         alpha=alpha+90
         x=rombx
         y=romby
    count=count+1

del draw
image.save("/home/eagle/test.png", "PNG")

