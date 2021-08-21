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
                        pixel = (pixelMap[i,j][0] + pixelMap[i,j][2] + pixelMap[i,j][1])/3
                        a = pixelMap[i,j][3]
                        


                        if pixel >= (255/2):
                            pixel = 255
                        else:
                            pixel=0


                        pixelMap[i,j] = (pixel, pixel, pixel, a)

                im.save(img_path, 'png')


                
                print('added filter to ' + img_path)