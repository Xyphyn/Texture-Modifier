import glob
import os
from PIL import Image
import PIL.ImageFilter
from random import randrange as random

def convert():
    for root, dirs, files in os.walk("./textures"):
        for file in files:
            if file.endswith(".png"):
                img_path = os.path.join(root, file)
                im = PIL.Image.open(img_path)
                im = im.convert('RGBA')
                
                pixelMap = im.load()

                for i in range(im.size[0]):
                    for j in range(im.size[1]):
                        pixel1 = pixelMap[i,j]

                        i2 = random(-2,2)
                        j2 = random(-2,2)

                        if i2 > im.size[0]:
                            i2 = im.size[0]
                        if i2 < 0:
                            i2 = 0
                        if j2 > im.size[1]:
                            j2 = im.size[1]
                        if j2 < 0:
                            j2 = 0

                        pixel2 = pixelMap[i2,j2]
                        pixelMap[i2,j2] = pixel1
                        pixelMap[i,j] = pixel2

                im.save(img_path, 'png')


                
                print('added filter to ' + img_path)