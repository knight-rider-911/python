from PIL import Image, ImageDraw
image = Image.new("RGBA", (320,320), (0,0,0,0))
draw = ImageDraw.Draw(image)
draw.ellipse((10,10,300,300), fill="blue", outline="red")
draw.rectangle((10,10,200,200), outline="black", fill="yellow")
del draw
image.save("/home/eagle/test.png", "PNG")