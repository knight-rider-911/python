from PIL import Image, ImageDraw
blue=0
red=0
green=0
while red != 16:
    while green !=16:
        while blue !=16:
            color = (red, green, blue)
            img = Image.new('RGB', (100, 50), color)
            imgDrawer = ImageDraw.Draw(img)
            img.save("/home/eagle/img/h" +str(red)+str(green)+str(blue) + "-e.png")
            blue=blue+1
        green=green+1
    red=red+1

