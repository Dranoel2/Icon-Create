from PIL import Image

import os

from resizeimage import resizeimage

import shutil

sizes = [512,128,32,16]

name = input('Name of icns file? ')

os.system('mkdir -p ../{}.iconset'.format(name))

with open('../Graphics/icon.png', 'r+b') as icon:
    with Image.open(icon) as image:
        for size in sizes:
            x = size*2
            final = resizeimage.resize_contain(image, [x,x])
            final.save('../{}.iconset/icon_{}x{}@x2.png'.format(name, x, x), image.format)
            x = size
            final = resizeimage.resize_contain(image, [x,x])
            final.save('../{}.iconset/icon_{}x{}.png'.format(name, x, x), image.format)
            os.system('iconutil -c icns "../{}.iconset"'.format(name))
