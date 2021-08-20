import glob
import os
import PIL.Image
import PIL.ImageFilter

def convert():
    blurAmount = input("How much would you like to blur? (.8 recommended for 16x, 1.5 recommended for 32x) (float/number) ")
    for root, dirs, files in os.walk("./textures"):
        for file in files:
            if file.endswith(".png"):
                img_path = os.path.join(root, file)
                im = PIL.Image.open(img_path)
                im = im.convert('RGBA')
                print('added filter to ' + img_path)
                
                im2 = im.filter(PIL.ImageFilter.GaussianBlur(float(blurAmount)))
                im2.save(img_path, 'png')