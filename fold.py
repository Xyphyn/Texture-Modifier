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
                im2 = im
                
                pixelMap = im.load()
                pixelMap2 = im2.load()

                for i in range(im.size[0]):
                    for j in range(im.size[1]):
                        pixel1 = pixelMap[i,j]
                        pixelMap2[i,(im.size[1] - j)-1] = pixel1
                pixelMap = pixelMap2
                        
                        

                im.save(img_path, 'png')


                
                print('added filter to ' + img_path)