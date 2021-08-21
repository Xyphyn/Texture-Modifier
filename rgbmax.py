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
                        r = pixelMap[i,j][0]
                        g = pixelMap[i,j][1]
                        b = pixelMap[i,j][2]
                        a = pixelMap[i,j][3]
                        


                        if r >= (255/2):
                            r = 255
                        else:
                            r=0

                        if b >= (255/2):
                            b = 255
                        else:
                            b=0

                            
                        if g >= (255/2):
                            g = 255
                        else:
                            g=0

                        pixelMap[i,j] = (r, g, b, a)

                im.save(img_path, 'png')


                
                print('added filter to ' + img_path)