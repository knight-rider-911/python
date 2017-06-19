from PIL import Image, ImageDraw
blue=0
red=0
green=0
while red != 16:
    while green !=16:
        while blue !=16:
            color = (red*red, green*green, blue*blue)
            img = Image.new('RGB', (100, 50), color)
            imgDrawer = ImageDraw.Draw(img)
            img.save("/home/eagle/img/red" + str(red) + "green" + str(green) + "blue" + str(blue) + ".png")
            print(red, green, blue)
            blue=blue+1
        blue=0
        green=green+1
        print(red, green, blue)
    print(red, green, blue)
    green=0
    blue-0
    red=red+1

print("end")

