import os
import PIL.Image
import PIL.ImageColor
import random
import math
import shutil
import fnmatch

def convert():
    cwd = os.getcwd()
    for root, dirs, files in os.walk("./textures"):
        
        fileCounter = 0

        for file in files:
            if file.endswith(".ogg"):
                randomFiles = fnmatch.filter(os.listdir(root), "*.ogg")
                fileCounter = fileCounter + 1
                randomFile = random.choice(randomFiles)

                if not fileCounter == len(files):
                    while os.path.join(root, randomFile) == os.path.join(root, file):
                        randomFiles2 = randomFiles
                        randomFile = random.choice(randomFiles2)
                        print(os.path.join(root, randomFile) + " " + os.path.join(root, file))
                    ogg_path = os.path.join(root, file)
                    ogg_path2 = os.path.join(root, randomFile)

                    print("swapping " + ogg_path + " with " + ogg_path2)

                    shutil.copy(ogg_path2, os.path.join(cwd, "test.ogg"))

                    shutil.copy(ogg_path,ogg_path2)
                    shutil.copy(os.path.join(cwd, "test.ogg"), ogg_path)