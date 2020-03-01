from PIL import Image

from resizeimage import resizeimage

sizes = [512,128,32,16]

name = input('Name of icns file?')

with open('../Graphics/icon.png', 'r+b') as icon:
    with Image.open(icon) as image:
        for size in sizes:
            x = size*2
            final = resizeimage.resize_contain(image, [x,x])
            file.save('../{}.iconset/icon_{}x{}@x2.png'.format(name, x, x), image.format)
            x = size
            final = resizeimage.resize_contain(image, [x,x])
            file.save('../{}.iconset/icon_{}x{}.png'.format(name, x, x), image.format)
