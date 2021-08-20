import glob
import os
import PIL.Image
import PIL.ImageColor

def convert():
    for root, dirs, files in os.walk("./textures"):
        for file in files:
            if file.endswith(".png"):
                img_path = os.path.join(root, file)
                im = PIL.Image.open(img_path)
                im = im.convert('LA')
                
                print('added effect to ' + img_path)
                
                im.save(img_path, 'png')