import glob
import os
import PIL.Image
import PIL.ImageFilter
from random import randrange as random

def convert():
    for root, dirs, files in os.walk("./textures"):
        for file in files:
            if file.endswith(".png"):
                img_path = os.path.join(root, file)
                im = PIL.Image.open(img_path)
                im = im.convert('RGBA')
                im = im.transpose(PIL.Image.FLIP_TOP_BOTTOM)

                im.save(img_path, 'png')


                
                print('added filter to ' + img_path)