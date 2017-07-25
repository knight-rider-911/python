from PIL import Image, ImageDraw
blue=86
red=1
green=36
color = (red, green, blue)
img = Image.new('RGB', (100, 50), color)
imgDrawer = ImageDraw.Draw(img)
img.save("/home/eagle/img/red" + str(red) + "green" + str(green) + "blue" + str(blue) + ".png")
print(red, green, blue)

print("end")

